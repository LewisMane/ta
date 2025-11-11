import streamlit as st

st.set_page_config(page_title="Folium Map", layout="wide")
st.title("📍 My Folium Map")

st.sidebar.header("Info")
st.sidebar.markdown("""
- Tap the locate button to grant location permission.  
- Geolocation works best when deployed via **HTTPS** (Streamlit Cloud).  
- All markers, layers, and popups are included.
""")

# -----------------------------
# Load your pre-generated HTML map
# -----------------------------
html_file_path = "zone 83--84 map.html"  # place your Folium HTML in the same folder as this script

with open(html_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML map directly
st.components.v1.html(html_content, height=700, scrolling=True)

st.markdown("---")
st.markdown("**Tip:** Deploy to Streamlit Cloud for HTTPS to ensure mobile geolocation works seamlessly.")
