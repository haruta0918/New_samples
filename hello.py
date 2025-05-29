import streamlit as st
import pandas as pd
import numpy as np

df = (
    {
        "col1":34.715265,
        "col2":137.6885,
        "col3":11,

    }
)

st.map(df, latitude="col1", longitude="col2", size="col3", color="#0044ff")
