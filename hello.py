import streamlit as st
import pandas as pd
import numpy as np
import json
    
json_open = open('samples/20250415_165815.jpg.supplemental-metadata.json', 'r')
json_load = json.load(json_open)
d = [
        {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},
    ]
# 1つの辞書として追加
json_open1 = open('sample/20250427_152127.jpg.supplemental-metadata.json', 'r')
json_load1 = json.load(json_open1)
lat = json_load1['geoData']['latitude']
lon = json_load1['geoData']['longitude']
new_point = {
    "LAT": lat,
    "LON": lon,
    "SIZE": 0.5,
    "COLOR": [0, 255, 0, 100]
}
st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)(new_point,latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15),