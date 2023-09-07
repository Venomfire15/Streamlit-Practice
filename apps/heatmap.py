import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    #filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    filepath = "F:\\Project MON\\DataSet\\Glob.csv"
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude="longitude",
        value="wind_degree",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(height=700)
