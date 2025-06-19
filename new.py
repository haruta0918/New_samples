import streamlit as st
import pandas as pd
import numpy as np
import json
    
json_open = open('samples/20250415_165815.jpg.supplemental-metadata.json', 'r')
json_load = json.load(json_open)


new_point = {"LAT": 34.9, "LON": 137.8, "SIZE": 0.5, "COLOR": [255, 0, 0, 100]}
d["points"].append(new_point)
print(d["points"])  # すべてのポイントリストを表示
