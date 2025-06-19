import streamlit as st
import pandas as pd
import numpy as np
import json
    
json_open = open('samples/20250415_165815.jpg.supplemental-metadata.json', 'r')
json_load = json.load(json_open)

d = {
    "points": [
        {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},
    ]
}

new_point = ([
    {"LAT": 34.704852848835955, "LON": 137.68991679239386, "SIZE": 0.5, "COLOR": [0, 255, 0, 100]},
])
d["points"].append(new_point)
points_df = pd.DataFrame(d["points"])
points_df = points_df.rename(columns={"LAT": "lat", "LON": "lon"})
st.map(points_df)
print(d)