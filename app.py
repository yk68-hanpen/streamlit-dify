import streamlit as st

# ページの設定
st.set_page_config(page_title="Streamlit Sample", layout="wide")

# タイトル
st.title("🎈 Streamlit サンプルアプリ")

# テキスト入力
name = st.text_input("お名前を入力してください:")
if name:
    st.write(f"こんにちは、{name}さん！")

# スライダー
age = st.slider("年齢を選択してください", 0, 100, 25)
st.write(f"あなたの年齢: {age}才")

# セレクトボックス
option = st.selectbox(
    "好きな色を選んでください:",
    ["赤", "青", "緑", "黄色"]
)
st.write(f"選択した色: {option}")

# チェックボックス
st.subheader("チェックボックスの例")
if st.checkbox("詳細情報を表示"):
    st.write("これは詳細情報です")

# ボタン
st.subheader("ボタンの例")
if st.button("クリックしてください"):
    st.balloons()
    st.write("ボタンがクリックされました！")

# データフレーム表示
st.subheader("データフレームの例")
import pandas as pd

data = {
    "名前": ["太郎", "花子", "次郎"],
    "年齢": [25, 30, 28],
    "職業": ["エンジニア", "デザイナー", "営業"]
}
df = pd.DataFrame(data)
st.dataframe(df)

# グラフの表示
st.subheader("グラフの例")
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)
