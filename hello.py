import streamlit as st
import pandas as pd
import numpy as np
import json
json_open = open('samples/20250415_165815.jpg.supplemental-metadata', 'r')
json_load = json.load(json_open)

d = [
    {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},
]
json_open = open('20250426_134824.jpg.supplemental-metadata', 'r')
json_load = json.load(json_open)

st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)
print(d)
