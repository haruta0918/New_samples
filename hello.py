import streamlit as st
import pandas as pd
import numpy as np

d = [
    {"LAT": 34.715265, "LON": 137.6885, "SIZE": 1, "COLOR": [0, 0, 255, 100]},
    {"LAT": 34.716265, "LON": 137.6885, "SIZE": 1, "COLOR": [0, 255, 0, 100]},
    {"LAT": 34.717265, "LON": 137.6885, "SIZE": 1, "COLOR": [255, 0, 0, 100]},
]

st.map(d, latitude="LAT", longitude="LON", size="SIZE", color="COLOR", zoom=15)