import streamlit as st
import pandas as pd
import numpy as np
import json
import os

json_open=open('samples/20250427_152756.jpg.supplemental-metadata.json', 'r') 
json_load = json.load(json_open)
aaa=10000
d = [
        {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]}, 
    ]
print('aaa')
print(json_open)

folder_path = 'samples'
a=0
b='samples/20251.jpg.supplemental-metadata.json'
# フォルダ内の .json ファイルを探してループ
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        a+=1
        json_open=open(b, 'r') 
        json_load = json.load(json_open)
        d.append({"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]})       
st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)
print(a)