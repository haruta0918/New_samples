import streamlit as st
import pandas as pd
import numpy as np
import json
    
json_open = open('samples/20250415_165815.jpg.supplemental-metadata.json', 'r')
json_load = json.load(json_open)

d = [
        {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},
    ]


d.extend = ([
    {"LAT": 34.704852848835955, "LON": 137.68991679239386, "SIZE": 0.6, "COLOR": [0, 255, 0, 100]},
    {"LAT": 34.70681773800157, "LON": 137.6818660117991, "SIZE": 0.6, "COLOR": [0, 255, 0, 100]},
])
st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)
print(d)