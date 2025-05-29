import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(200, 2) / [350, 350] + [34.712531, 137.6887006],
    columns=["lat", "lon"],
)
st.map(latitude=34.712531,longitude=137.6887006, size=10, color="#0044ff",zoom=11)
st.map(df)