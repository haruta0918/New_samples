import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(30, 1) / [400, 400] + [34.7134129, 137.6963825],
    columns=["lat", "lon"],
)
st.map(df)