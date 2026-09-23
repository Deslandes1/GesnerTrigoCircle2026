"""
GESNER TRIGONOMETRY CIRCLE
Built by Gesner Deslandes · Software Engineer
Contact: (509)-47385663

Interactive unit circle with:
- Drag / slider angle control (degrees & radians)
- Live sin, cos, tan, cot values (decimal + exact)
- Special-angle table (0° to 360°)
- Concept cards and real-world application cards
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import math

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Gesner Trigonometry Circle",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
# CUSTOM CSS  (dark gold theme matching the HTML version)
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(1000px 600px at 50% -10%, rgba(58,160,255,.18), transparent 65%),
                    radial-gradient(800px 500px at 10% 110%, rgba(255,217,59,.08), transparent 60%),
                    radial-gradient(800px 500px at 90% 110%, rgba(168,107,255,.08), transparent 60%),
                    #070b14;
        color: #eaf1ff;
    }
    h1, h2, h3 { color: #ffd93b !important; letter-spacing: 2px; }
    .main-title {
        font-family: Georgia, serif;
        font-size: clamp(1.5rem, 4.5vw, 2.6rem);
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #ffd93b, #ff9f00, #c8811a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-weight: 900;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #ffe680;
        font-size: 0.9rem;
        margin-bottom: 4px;
    }
    .author {
        text-align: center;
        font-family: Georgia, serif;
        color: #ffd93b;
        font-weight: 900;
        letter-spacing: 2px;
        font-size: 0.95rem;
    }
    .contact {
        text-align: center;
        color: #8fa9d1;
        font-size: 0.8rem;
        letter-spacing: 1.5px;
        font-weight: 800;
        margin-bottom: 18px;
    }
    .val-card {
        border-radius: 14px;
        padding: 14px 16px;
        background: linear-gradient(180deg, rgba(10,16,30,.9), rgba(6,10,20,.9));
        border: 2px solid rgba(148,163,255,.22);
        margin-bottom: 10px;
    }
    .val-name {
        font-size: 0.62rem; font-weight: 900; letter-spacing: 2.2px;
        text-transform: uppercase; color: #8fa9d1; margin-bottom: 6px;
    }
    .val-num {
        font-family: 'Courier New', monospace; font-size: 1.5rem;
        font-weight: 900; color: #fff; line-height: 1.1;
    }
    .val-exact {
        font-family: 'Courier New', monospace; font-size: 0.8rem;
        font-weight: 900; color: #ffe680; margin-top: 4px;
    }
    .info-box {
        border-radius: 12px; padding: 10px 12px;
        background: rgba(10,16,30,.6);
        border: 1.5px solid rgba(148,163,255,.20);
        margin-bottom: 8px;
    }
    .info-k {
        font-size: 0.58rem; font-weight: 900; letter-spacing: 1.9px;
        text-transform: uppercase; color: #8fa9d1; margin-bottom: 4px;
    }
    .info-v {
        font-family: 'Courier New', monospace; font-size: 1rem;
        font-weight: 900; color: #fff5c4;
    }
    .card {
        border-radius: 16px; padding: 16px 18px;
        background: linear-gradient(180deg, rgba(20,30,52,.94), rgba(12,18,32,.94));
        border: 2px solid rgba(148,163,255,.20);
        margin-bottom: 12px;
    }
    .card h3 { margin: 0 0 8px; font-size: 1rem; }
    .card p { font-size: 0.86rem; line-height: 1.6; color: #c8d6f0; margin: 0 0 8px; }
    .formula {
        font-family: 'Courier New', monospace; font-size: 1rem;
        font-weight: 900; padding: 8px 12px; border-radius: 10px;
        text-align: center; background: rgba(6,10,20,.8);
        border: 1.5px solid rgba(148,163,255,.22); color: #fff5c4;
    }
    .big-lesson {
        padding: 16px 20px; border-radius: 14px; text-align: center;
        background: linear-gradient(135deg, rgba(255,217,59,.16), rgba(255,159,0,.08));
        border: 2.5px solid rgba(255,217,59,.5);
        font-size: 0.95rem; font-weight: 900; line-height: 1.6; color: #fff5c4;
    }
    .question-strip {
        padding: 14px 18px; border-radius: 14px; text-align: center;
        background: rgba(58,160,255,.09);
        border: 2px solid rgba(58,160,255,.42);
        font-size: 0.9rem; font-weight: 900; color: #bcd9ff;
    }
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="subtitle">Where Trigonometry Becomes Visual · Drag · Search · Explore</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">GESNER TRIGONOMETRY CIRCLE</div>', unsafe_allow_html=True)
st.markdown('<div class="author">BUILT BY GESNER DESLANDES · SOFTWARE ENGINEER</div>', unsafe_allow_html=True)
st.markdown('<div class="contact">📞 (509)-47385663</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# SPECIAL ANGLES DATA
# ─────────────────────────────────────────────────────────────
SPECIAL = {
    0:   {"rad": "0",      "sin": "0",      "cos": "1",       "tan": "0",        "cot": "∞"},
    30:  {"rad": "π/6",    "sin": "1/2",    "cos": "√3/2",    "tan": "√3/3",     "cot": "√3"},
    45:  {"rad": "π/4",    "sin": "√2/2",   "cos": "√2/2",    "tan": "1",        "cot": "1"},
    60:  {"rad": "π/3",    "sin": "√3/2",   "cos": "1/2",     "tan": "√3",       "cot": "√3/3"},
    90:  {"rad": "π/2",    "sin": "1",      "cos": "0",       "tan": "∞",        "cot": "0"},
    120: {"rad": "2π/3",   "sin": "√3/2",   "cos": "−1/2",    "tan": "−√3",      "cot": "−√3/3"},
    135: {"rad": "3π/4",   "sin": "√2/2",   "cos": "−√2/2",   "tan": "−1",       "cot": "−1"},
    150: {"rad": "5π/6",   "sin": "1/2",    "cos": "−√3/2",   "tan": "−√3/3",    "cot": "−√3"},
    180: {"rad": "π",      "sin": "0",      "cos": "−1",      "tan": "0",        "cot": "∞"},
    210: {"rad": "7π/6",   "sin": "−1/2",   "cos": "−√3/2",   "tan": "√3/3",     "cot": "√3"},
    225: {"rad": "5π/4",   "sin": "−√2/2",  "cos": "−√2/2",   "tan": "1",        "cot": "1"},
    240: {"rad": "4π/3",   "sin": "−√3/2",  "cos": "−1/2",    "tan": "√3",       "cot": "√3/3"},
    270: {"rad": "3π/2",   "sin": "−1",     "cos": "0",       "tan": "∞",        "cot": "0"},
    300: {"rad": "5π/3",   "sin": "−√3/2",  "cos": "1/2",     "tan": "−√3",      "cot": "−√3/3"},
    315: {"rad": "7π/4",   "sin": "−√2/2",  "cos": "√2/2",    "tan": "−1",       "cot": "−1"},
    330: {"rad": "11π/6",  "sin": "−1/2",   "cos": "√3/2",    "tan": "−√3/3",    "cot": "−√3"},
    360: {"rad": "2π",     "sin": "0",      "cos": "1",       "tan": "0",        "cot": "∞"},
}

# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def fmt(v, dp=4):
    if v is None or (isinstance(v, float) and not math.isfinite(v)):
        return "undefined"
    r = round(v, dp)
    if r == 0:
        return "0"
    return f"{r:.{dp}f}"

def quadrant_of(deg):
    a = deg % 360
    if a in (0, 90, 180, 270):
        return "Axis"
    if a < 90:
        return "I"
    if a < 180:
        return "II"
    if a < 270:
        return "III"
    return "IV"

def reference_angle(deg):
    a = deg % 360
    if a <= 90:
        return a
    if a <= 180:
        return 180 - a
    if a <= 270:
        return a - 180
    return 360 - a

def exact_for(deg):
    a = round(deg) % 360
    if abs(deg - round(deg)) > 1e-6:
        return None
    return SPECIAL.get(a)

# ─────────────────────────────────────────────────────────────
# BUILD PLOTLY FIGURE
# ─────────────────────────────────────────────────────────────
def build_figure(deg, show_sin, show_cos, show_tan, show_grid):
    rad = math.radians(deg)
    cos_t, sin_t = math.cos(rad), math.sin(rad)
    tan_undef = abs(cos_t) < 1e-10
    tan_t = None if tan_undef else sin_t / cos_t

    fig = go.Figure()

    # ── Unit circle ──
    theta = np.linspace(0, 2 * np.pi, 400)
    fig.add_trace(go.Scatter(
        x=np.cos(theta), y=np.sin(theta),
        mode="lines",
        line=dict(color="rgba(58,160,255,0.6)", width=3),
        name="Unit circle",
        hoverinfo="skip",
    ))

    # ── Axes ──
    fig.add_trace(go.Scatter(x=[-1.35, 1.35], y=[0, 0], mode="lines",
                             line=dict(color="rgba(234,241,255,0.45)", width=2),
                             hoverinfo="skip", showlegend=False))
    fig.add_trace(go.Scatter(x=[0, 0], y=[-1.35, 1.35], mode="lines",
                             line=dict(color="rgba(234,241,255,0.45)", width=2),
                             hoverinfo="skip", showlegend=False))

    # ── Grid spokes every 30° ──
    if show_grid:
        for a in range(0, 360, 30):
            r = math.radians(a)
            fig.add_trace(go.Scatter(
                x=[0, math.cos(r)], y=[0, math.sin(r)],
                mode="lines",
                line=dict(color="rgba(148,163,255,0.12)", width=1),
                hoverinfo="skip", showlegend=False,
            ))

    # ── Cosine segment (horizontal, blue) ──
    if show_cos:
        fig.add_trace(go.Scatter(
            x=[0, cos_t], y=[0, 0],
            mode="lines",
            line=dict(color="#3aa0ff", width=6),
            name="cos θ",
            hovertemplate="cos θ = %{x:.4f}<extra></extra>",
        ))

    # ── Sine segment (vertical, green) ──
    if show_sin:
        fig.add_trace(go.Scatter(
            x=[cos_t, cos_t], y=[0, sin_t],
            mode="lines",
            line=dict(color="#3ddc84", width=6),
            name="sin θ",
            hovertemplate="sin θ = %{y:.4f}<extra></extra>",
        ))

    # ── Tangent segment on x = 1 ──
    if show_tan and not tan_undef:
        fig.add_trace(go.Scatter(
            x=[1, 1], y=[0, tan_t],
            mode="lines",
            line=dict(color="#ff9f43", width=5),
            name="tan θ",
            hovertemplate="tan θ = %{y:.4f}<extra></extra>",
        ))
        fig.add_trace(go.Scatter(
            x=[0, 1], y=[0, tan_t],
            mode="lines",
            line=dict(color="rgba(255,159,67,0.5)", width=2, dash="dash"),
            hoverinfo="skip", showlegend=False,
        ))

    # ── Terminal radius ──
    fig.add_trace(go.Scatter(
        x=[0, cos_t], y=[0, sin_t],
        mode="lines",
        line=dict(color="#eaf1ff", width=3),
        name="radius",
        hoverinfo="skip",
    ))

    # ── Moving point ──
    fig.add_trace(go.Scatter(
        x=[cos_t], y=[sin_t],
        mode="markers+text",
        marker=dict(size=16, color="#ffd93b",
                    line=dict(color="#fff", width=3)),
        text=[f"({cos_t:.3f}, {sin_t:.3f})"],
        textposition="top right",
        textfont=dict(color="#fff5c4", size=12,
                      family="Courier New, monospace"),
        name="P",
        hovertemplate="Point P<extra></extra>",
    ))

    # ── Angle arc ──
    if 0.4 < deg < 359.6:
        arc_theta = np.linspace(0, rad, max(2, int(deg)))
        fig.add_trace(go.Scatter(
            x=0.33 * np.cos(arc_theta),
            y=0.33 * np.sin(arc_theta),
            mode="lines",
            line=dict(color="#ffd93b", width=3),
            fill="toself",
            fillcolor="rgba(255,217,59,0.14)",
            hoverinfo="skip", showlegend=False,
        ))

    # ── Layout ──
    fig.update_layout(
        xaxis=dict(range=[-1.45, 1.45], showgrid=False, zeroline=False,
                   showticklabels=False, fixedrange=True),
        yaxis=dict(range=[-1.45, 1.45], showgrid=False, zeroline=False,
                   showticklabels=False, fixedrange=True,
                   scaleanchor="x", scaleratio=1),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=560,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="center", x=0.5,
            font=dict(color="#eaf1ff", size=12),
            bgcolor="rgba(0,0,0,0)",
        ),
        hovermode="closest",
    )
    return fig

# ─────────────────────────────────────────────────────────────
# LAYOUT
# ─────────────────────────────────────────────────────────────
col_circle, col_control = st.columns([1.05, 1], gap="large")

# ─── LEFT : CIRCLE ───
with col_circle:
    st.markdown("### 🧭 Interactive Unit Circle")

    show_sin = st.toggle("Show sin θ (green)", value=True)
    show_cos = st.toggle("Show cos θ (blue)", value=True)
    show_tan = st.toggle("Show tan θ (orange)", value=True)
    show_grid = st.toggle("Show 30° grid", value=True)

    fig = build_figure(
        st.session_state.get("angle", 30),
        show_sin, show_cos, show_tan, show_grid,
    )
    st.plotly_chart(fig, use_container_width=True)

# ─── RIGHT : CONTROLS + VALUES ───
with col_control:
    st.markdown("### 🔎 Angle Explorer")

    # ── Degree slider (main control) ──
    deg = st.slider(
        "Angle in degrees",
        min_value=0, max_value=360, value=30, step=1,
        key="angle_slider",
    )
    st.session_state["angle"] = deg

    # ── Radian display ──
    rad_exact = SPECIAL.get(deg, {}).get("rad", None)
    rad_dec = math.radians(deg)
    rad_text = f"{rad_exact}  ({rad_dec:.4f} rad)" if rad_exact else f"{rad_dec:.4f} rad"
    st.caption(f"Radians: **{rad_text}**")

    # ── Number input for precise angles ──
    precise = st.number_input(
        "Or type an exact angle (degrees)",
        min_value=0.0, max_value=360.0, value=float(deg), step=0.1,
        key="precise_input",
    )
    if abs(precise - deg) > 0.05:
        st.session_state["angle"] = precise
        st.rerun()

    # ── Quick angle buttons ──
    st.markdown("**Quick jump**")
    quick_cols = st.columns(9)
    quick_angles = [0, 30, 45, 60, 90, 120, 135, 150, 180]
    for i, qa in enumerate(quick_angles):
        if quick_cols[i].button(f"{qa}°", key=f"q{qa}", use_container_width=True):
            st.session_state["angle"] = qa
            st.rerun()

    # ── Values ──
    rad = math.radians(deg)
    cos_t = math.cos(rad)
    sin_t = math.sin(rad)
    tan_undef = abs(cos_t) < 1e-10
    cot_undef = abs(sin_t) < 1e-10
    tan_t = None if tan_undef else sin_t / cos_t
    cot_t = None if cot_undef else cos_t / sin_t
    sp = exact_for(deg)

    st.markdown("#### 📊 Values at θ = **{:.1f}°**".format(deg))

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f'<div class="val-card">'
            f'<div class="val-name">Sine · sin θ</div>'
            f'<div class="val-num">{fmt(sin_t)}</div>'
            f'<div class="val-exact">{sp["sin"] if sp else "≈ " + fmt(sin_t)}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="val-card">'
            f'<div class="val-name">Tangent · tan θ</div>'
            f'<div class="val-num">{"undefined" if tan_undef else fmt(tan_t)}</div>'
            f'<div class="val-exact">{sp["tan"] if sp else ("undefined" if tan_undef else "≈ " + fmt(tan_t))}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="val-card">'
            f'<div class="val-name">Cosine · cos θ</div>'
            f'<div class="val-num">{fmt(cos_t)}</div>'
            f'<div class="val-exact">{sp["cos"] if sp else "≈ " + fmt(cos_t)}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="val-card">'
            f'<div class="val-name">Cotangent · cot θ</div>'
            f'<div class="val-num">{"undefined" if cot_undef else fmt(cot_t)}</div>'
            f'<div class="val-exact">{sp["cot"] if sp else ("undefined" if cot_undef else "≈ " + fmt(cot_t))}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    # ── Info strip ──
    st.markdown("#### 📍 Position Info")
    i1, i2 = st.columns(2)
    with i1:
        st.markdown(
            f'<div class="info-box"><div class="info-k">Degrees</div>'
            f'<div class="info-v">{deg:.1f}°</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="info-box"><div class="info-k">Reference angle</div>'
            f'<div class="info-v">{reference_angle(deg):.1f}°</div></div>',
            unsafe_allow_html=True,
        )
    with i2:
        st.markdown(
            f'<div class="info-box"><div class="info-k">Radians</div>'
            f'<div class="info-v">{rad_text}</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="info-box"><div class="info-k">Quadrant</div>'
            f'<div class="info-v">{quadrant_of(deg)}</div></div>',
            unsafe_allow_html=True,
        )

# ─────────────────────────────────────────────────────────────
# SPECIAL VALUE TABLE
# ─────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 📊 Exact Values · Special Angles")
st.caption("Click any row in the table below to see it on the circle. (Table is read-only — use the slider above.)")

table_rows = []
for k in sorted(SPECIAL.keys()):
    s = SPECIAL[k]
    table_rows.append({
        "Angle": f"{k}°",
        "Radians": s["rad"],
        "sin θ": s["sin"],
        "cos θ": s["cos"],
        "tan θ": "undefined" if s["tan"] == "∞" else s["tan"],
        "cot θ": "undefined" if s["cot"] == "∞" else s["cot"],
    })

st.dataframe(table_rows, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────────────────────
# THE FOUR FUNCTIONS
# ─────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 🧠 The Four Functions Explained")

f1, f2 = st.columns(2)
with f1:
    st.markdown(
        '<div class="card"><h3>🔵 1. Sine — sin θ</h3>'
        '<p>The <b>y-coordinate</b> of the point on the unit circle. '
        'It measures how <i>high</i> the point is. As the angle grows, '
        'sine rises and falls like a wave.</p>'
        '<div class="formula">sin θ = y</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card"><h3>🟠 3. Tangent — tan θ</h3>'
        '<p>The ratio of sine to cosine. Geometrically it is the '
        '<b>slope</b> of the terminal side, and it equals the length of '
        'the segment on the tangent line at x = 1.</p>'
        '<div class="formula">tan θ = sin θ / cos θ</div></div>',
        unsafe_allow_html=True,
    )
with f2:
    st.markdown(
        '<div class="card"><h3>🟢 2. Cosine — cos θ</h3>'
        '<p>The <b>x-coordinate</b> of the point. It measures how '
        '<i>far right</i> or <i>left</i> the point sits. Together with '
        'sine it gives the exact position.</p>'
        '<div class="formula">cos θ = x</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card"><h3>🟣 4. Cotangent — cot θ</h3>'
        '<p>The reciprocal of tangent. It is the slope of the line '
        'measured the other way around, and equals the segment on the '
        'tangent line at y = 1.</p>'
        '<div class="formula">cot θ = cos θ / sin θ</div></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="big-lesson">💡 <b>The bigger lesson:</b> When you understand '
    'the geometry behind a formula, you don\'t just memorize mathematics — '
    '<b>you can apply it.</b></div>',
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# WHY IT MATTERS
# ─────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 🌍 Why the Unit Circle Matters")

apps = [
    ("🎮", "Game Development", "Rotating characters, aiming weapons, camera movement, and 3D graphics all rely on sine and cosine."),
    ("🤖", "Robotics", "Robot arms move by rotating joints. Every joint angle is computed with trigonometry."),
    ("⚡", "Electrical Engineering", "Alternating current is a sine wave. Voltage, current, and phase all use the unit circle."),
    ("📡", "Signal Processing", "Audio, radio, Wi-Fi, and images are broken into sine waves — the Fourier transform."),
    ("🚀", "Physics & Simulations", "Projectile motion, pendulums, orbits, and waves are all described with trig functions."),
    ("📊", "Data Science", "Seasonal patterns, cyclical trends, and mathematical modelling use periodic functions."),
]

app_cols = st.columns(3)
for i, (ico, ttl, dsc) in enumerate(apps):
    with app_cols[i % 3]:
        st.markdown(
            f'<div class="card" style="text-align:center;">'
            f'<div style="font-size:1.9rem;">{ico}</div>'
            f'<h3 style="font-size:0.72rem;letter-spacing:1.6px;text-transform:uppercase;">{ttl}</h3>'
            f'<p style="font-size:0.78rem;">{dsc}</p></div>',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="question-strip">💬 <b>Your turn:</b> Where do you use '
    'trigonometry most — engineering, programming, physics, graphics, or '
    'something else?</div>',
    unsafe_allow_html=True,
)
