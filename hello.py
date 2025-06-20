import streamlit as st
import pandas as pd
import numpy as np
import json

with open('samples/20250427_152756.jpg.supplemental-metadata.json', 'r', encoding='utf-8') as f1:
    data1 = json.load(f1)


    
d = [
        {"LAT":f1['geoData']['latitude'], "LON":f1['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},
    ]
# 1つの辞書として追加
with open('samples/20250427_150440.jpg.supplemental-metadata.json', 'r', encoding='utf-8') as f2:
    data2 = json.load(f2)
lat = f2['geoData']['latitude']
lon = f2['geoData']['longitude']
new_point = {
    "LAT": lat,
    "LON": lon,
    "SIZE": 0.5,
    "COLOR": [0, 255, 0, 100]
}
st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)(new_point,latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15),