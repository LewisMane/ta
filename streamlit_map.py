import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Folium Map", layout="wide")
st.title("📍 Zone 83$84 Map")

# -----------------------------
# Load your pre-generated HTML map
# -----------------------------
html_file_path = "zone 83--84 map.html"  # place your Folium HTML in the same folder

with open(html_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# -----------------------------
# Modify HTML to make map responsive and Locate button prominent
# -----------------------------
# 1. Make map container 100% width
html_content = html_content.replace(
    '<div class="folium-map"', '<div class="folium-map" style="width:100%;height:100vh;"'
)

# 2. Optional: enlarge LocateControl button via inline CSS
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
html_content = enhance_css + html_content

# -----------------------------
# Render the HTML map
# -----------------------------
components.html(html_content, height=700, scrolling=True)
