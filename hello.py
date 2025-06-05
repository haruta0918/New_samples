import streamlit as st
import pandas as pd
import numpy as np

d = [
    {"LAT": 34.71946333, "LON": 137.69348144, "SIZE": 1, "COLOR": [0, 0, 255, 100]},
    {"LAT": 34.71928830, "LON": 137.69297330, "SIZE": 1, "COLOR": [0, 255, 0, 100]},
    {"LAT": 34.71929167, "LON": 137.69297789, "SIZE": 1, "COLOR": [255, 0, 0, 100]},
]

st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)
