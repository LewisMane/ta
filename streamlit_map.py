import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(page_title="Folium Maps", layout="wide")
st.title("📍 Zone Maps")

# --------------------------------------------------
# Auto-detect screen width (mobile vs desktop)
# --------------------------------------------------
st.markdown(
    """
    <script>
    const width = window.innerWidth;
    window.parent.postMessage(
        { type: "STREAMLIT_SCREEN_WIDTH", width: width },
        "*"
    );
    </script>
    """,
    unsafe_allow_html=True
)

# Default screen width
if "screen_width" not in st.session_state:
    st.session_state.screen_width = 1200

st.session_state.screen_width = st.session_state.get("screen_width", 1200)

is_mobile = st.session_state.screen_width < 768
MAP_HEIGHT = 500 if is_mobile else 700

# --------------------------------------------------
# BASE DIRECTORY FOR MAP FILES  ✅
# --------------------------------------------------
MAP_DIR = Path("Maps")

# --------------------------------------------------
# REGISTER YOUR MAPS HERE
# --------------------------------------------------
MAPS = {
    "Zone 83 & 84": MAP_DIR / "zone 83--84 map.html",
    "Zone 85 & 89": MAP_DIR / "zone 85 - 89 map.html",
    "Zone 86, 87 & TT87": MAP_DIR / "zone 86, 87, tt87 map.html",
    "Zone 88, 92 & 93": MAP_DIR / "zone 88, 92, 93 map.html",
    "Zone 90 & 91": MAP_DIR / "zone 90 91 map.html",
}

# --------------------------------------------------
# Map selector (radio buttons)
# --------------------------------------------------
selected_map_name = st.radio(
    "Select zone to view",
    list(MAPS.keys()),
    horizontal=True
)

st.subheader(f"📍 {selected_map_name}")

# --------------------------------------------------
# CACHED MAP LOADER  🚀
# --------------------------------------------------
@st.cache_data(show_spinner="Loading map…")
def load_html_map(html_path: Path) -> str:
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Make map responsive
    html = html.replace(
        '<div class="folium-map"',
        '<div class="folium-map" style="width:100%; height:100vh;"'
    )

    # Enhance Locate button
    enhance_css = """
    <style>
    .leaflet-control-locate {
        background-color: #2A8FE2 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 6px 10px !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
    }
    .leaflet-control-locate:hover {
        background-color: #1f6bbf !important;
    }
    </style>
    """
    return enhance_css + html

# --------------------------------------------------
# Load selected map (cached)
# --------------------------------------------------
html_file_path = MAPS[selected_map_name]

if not html_file_path.exists():
    st.error(f"Map file not found: {html_file_path}")
    st.stop()

html_content = load_html_map(html_file_path)

# --------------------------------------------------
# Render the HTML map (auto-sized)
# --------------------------------------------------
components.html(
    html_content,
    height=MAP_HEIGHT,
    scrolling=False
)


