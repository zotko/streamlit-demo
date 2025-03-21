import streamlit as st
import plotly.express as px
from xyz2graph import MolGraph
import pandas as pd

# Titel und Einführung
st.title("Streamlit ist einfach und leistungsstark! 🚀")
st.markdown(
    "Sehr geehrter **Herr Schmidt**,<br>"
    "mein Name ist **Mykola Zotko**. Diese App zeigt, wie ***schnell und einfach*** interaktive Anwendungen mit Streamlit erstellt werden können. "
    "Schauen Sie sich meine Anwendung an!",
    unsafe_allow_html=True
)

# XYZ-String für das Molekül
xyz_str = """19

C 0.1718396797 1.4440789224 0.2473852864
C -0.0134772223 -0.0326757574 0.0938838006
C 0.1911918378 -0.7602489274 -1.0094614486
C -0.0813817148 -2.2280845682 -0.8268852762
C 1.1888060415 -3.1274931355 -0.6555344372
C 1.0072262499 -2.9809298727 0.8649620514
O 1.7002498947 -3.2153415856 1.8121104941
C -0.3781727538 -2.3187190045 0.7118575614
C -0.5011349614 -0.8838757759 1.2539682327
H 0.9138428957 1.6706272458 1.0233883876
H 0.5008268994 1.9104479694 -0.6849988179
H -0.7617855184 1.9284667049 0.5611273403
H 0.5329169007 -0.3495980615 -1.9547455555
H -0.8300449081 -2.6244457733 -1.5177412211
H 1.0406339629 -4.1643541340 -0.9779621725
H 2.1342332626 -2.7639536285 -1.0666321354
H -1.1876969857 -2.9870255658 1.0159842036
H 0.1026579561 -0.7413714326 2.1588693984
H -1.5333315866 -0.6261358196 1.5267273780
"""

# Molekülgraph erstellen und visualisieren
st.header("3D Molekülvisualisierung mit xyz2graph 🧪")
mg = MolGraph()
mg.from_string(xyz_str)
fig = mg.to_plotly()

# Anzeige der Plotly-Figur
st.plotly_chart(fig, use_container_width=True)

# Erklärung des Pakets
st.header("Über mein xyz2graph-Paket")
st.markdown("""
Mein selbst entwickeltes Paket ermöglicht:
- 🧪 Einfache Umwandlung von XYZ-Koordinaten in 3D-Modelle
- 🔍 Analyse molekularer Strukturen mit wenigen Codezeilen
- 📊 Integration mit Streamlit, Jupyter und mehr

GitHub: [xyz2graph](https://github.com/zotko/xyz2graph)

### Vielleicht überlegen Sie es sich noch einmal? 😊

Besuchen Sie meine Webseite: [zotko.dev](https://zotko.dev).
""")