

import streamlit as st
import pandas as pd

st.title('JPG画像と関連位置情報の表示')

# ---
# 1. JPG画像を表示
# ---
# ご自身のJPGファイルのパスを指定してください。
# 例: 'data/my_travel_photo.jpg'
try:
    st.image("C:\Users\harut\Desktop\写真\Takeout\Google フォト\4月15日/20250415_165815jpg", caption="旅行で撮った写真", use_column_width=True)
    st.caption("C:\Users\harut\Desktop\写真\Takeout\Google フォト\4月15日/20250415_165815jpg")
except FileNotFoundError:
    st.error("指定されたJPGファイルが見つかりません。パスを確認してください。")

# ---
# 2. そのJPG画像に関連する位置情報をDataFrameとして準備
# ---
# この例では、画像が撮影された場所の緯度と経度を仮定しています。
# 実際には、手入力したり、データベースから取得したりすることが考えられます。
location_df = pd.DataFrame({
    'lat': [34.7025],  # 例: 大阪の緯度
    'lon': [135.4950], # 例: 大阪の経度
    'place_name': ['大阪市内のどこか'],
    'description': ['この写真が撮影されたと思われる場所です。']
})

st.subheader('写真の撮影場所')
st.write("写真が撮影されたと思われる場所を地図に表示しています。")

# ---
# 3. `st.map()`で位置情報を地図にプロット
# ---
st.map(location_df)

st.dataframe(location_df) # 位置情報の詳細を表示

st.info("このアプローチでは、JPG画像自体は地図にプロットされず、"
        "別途準備した位置情報が`st.map()`によってオンライン地図上に表示されます。")