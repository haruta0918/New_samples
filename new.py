import streamlit as st
import pandas as pd
import numpy as np
import json
    
json_open = open('samples/20250415_165815.jpg.supplemental-metadata.json', 'r')
json_load = json.load(json_open)

d = [
        {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]},
    ]
d.append = [
        {"LAT": 34.0522, "LON": -118.2437, "SIZE": 0.6, "COLOR": [0, 255, 0, 100]},
        {"LAT": 34.0522, "LON": -118.2437, "SIZE": 0.6, "COLOR": [0, 255, 0, 100]},
    ]
