import streamlit as st
import pandas as pd
import numpy as np
import json
import os

import os

folder_path = 'samples'

t=0
# フォルダ内の .json ファイルを探してループ
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        if t==0:
            # .jsonファイルを取得して並び替え（オプション）
            json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
            json_files.sort()  # ソートすると見やすい順に並ぶ

            folder_path2=folder_path+'/'    
            a2=0
            a=json_files[a2]
            print(a)
            stra=str(a)
            c=folder_path2+stra
            json_open=open(c, 'r',encoding='utf-8') 
            json_load = json.load(json_open)
            d = [
                    {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]}, 
                ]
        else:
            a2+=1
            a=json_files[a2]
            stra=str(a)
            c=folder_path2+stra
            file_path = os.path.join(folder_path, filename)
            json_open=open(c, 'r',encoding='utf-8') 
            json_load = json.load(json_open)
            print(json_load['title'])
            d.append({"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 0.5, "COLOR": [0, 0, 255, 100]})
            t+=1       
st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)
print(d)

