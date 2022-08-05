import streamlit as st
import geopandas as gp
import folium, osmnx, OSMPythonTools
from streamlit_folium import st_folium

st.write(folium.__version__)
st.write(osmnx.__version__)
st.write(OSMPythonTools.pkgVersion)

#url = 's3://quantcldata/varios/openstreetmap.pk'
url = 's3://quantcldata/OSM/cities.pk'

#odf = gp.read_file(url)
#st.write(odf.head())


#for ciudad, cdf in odf.groupby('ciudad'):
#    cdf['centro']=cdf.geometry.apply(lambda g: g.centroid)
#    centro = cdf.iloc[0]['centro']
#    st.subheader(ciudad)
#    cfm = folium.Map(location=(centro.y, centro.x)  # centroid
#    st_folium(cfm)
