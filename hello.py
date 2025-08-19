import streamlit as st
import pandas as pd
import numpy as np
import json
import os

import os

folder_path = 'いじる用'
o=0
t=0

# フォルダ内の .json ファイルを探してループ
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        o+=1
        print(o)
        if t==0:
            print("1回目")
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
                    {"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 2, "COLOR": json_load['color']}, 
                ]
        else:
            print("2回目以降")
            a2+=1
            a=json_files[a2]
            stra=str(a)
            c=folder_path2+stra
            file_path = os.path.join(folder_path, filename)
            json_open=open(c, 'r',encoding='utf-8') 
            json_load = json.load(json_open)
            d.append({"LAT":json_load['geoData']['latitude'], "LON":json_load['geoData']['longitude'], "SIZE": 2, "COLOR": json_load['color']})
        t+=1

st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)

print(d)

