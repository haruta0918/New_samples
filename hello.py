import streamlit as st
import pandas as pd
import numpy as np
import json

json_open=open('samples/20250427_152756.jpg.supplemental-metadata.json', 'r') 
json_load = json.load(json_open)

d = [
        {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},
        {"LAT":34.7047046, "LON":137.6896061, "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},   
    ]
st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)