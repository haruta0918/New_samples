import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [1, 1] + [34.7134129, 137.6963825],
    columns=["lat", "lon"],
)
st.map(df)