import qrcode
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'lat': [35.689487, 35.658581, 35.703717],
    'lon': [139.691706, 139.745433, 139.771357]
})

st.write('st.map exsample')
st.map(df)

