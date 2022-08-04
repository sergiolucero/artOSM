import streamlit as st
import geopandas as gp
import folium, osmnx, OSMPythonTools


st.write(folium.__version__)
st.write(osmnx.__version__)
st.write(OSMPythonTools.pkgVersion)

url = 's3://quantcldata/varios/openstreetmap.pk')
odf = gp.read_file(url)

st.write(odf)
