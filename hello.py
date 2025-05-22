import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 2) / [500, 500] + [34.7134129, 137.6963825],
    columns=["lat", "lon"],
)
st.map(df)