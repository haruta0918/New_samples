import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    (200, 2) / [350, 350] + [34.712531, 137.6887006],
    columns=["lat", "lon"],
)
st.map(df, size=5, color="#0044ff")
st.map(df)