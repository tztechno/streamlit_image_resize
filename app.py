import streamlit as st
from PIL import Image
import os

# 画像をリサイズする関数
def resize_image(input_image, max_width):
    original_width, original_height = input_image.size
    
    # 画像のリサイズ
    if original_width > max_width:
        ratio = max_width / original_width
        new_height = int(original_height * ratio)
        resized_image = input_image.resize((max_width, new_height), Image.ANTIALIAS)
        return resized_image
    else:
        return input_image

# Streamlit アプリの設定
st.title("画像リサイズアプリ")
max_width = st.number_input("最大幅を入力してください:", min_value=1, value=224)
uploaded_file = st.file_uploader("画像ファイルを選択してください", type=["jpg", "jpeg", "png"])

# 画像がアップロードされた場合
if uploaded_file is not None:
    # 画像を開く
    image = Image.open(uploaded_file)
    
    # 画像のリサイズ
    resized_image = resize_image(image, max_width)
    
    # 新しいファイル名の作成
    original_filename = uploaded_file.name
    new_filename = f"{max_width}_{original_filename}"
    
    # リサイズされた画像を保存
    resized_image.save(new_filename)
    
    # リサイズされた画像の表示
    st.image(resized_image, caption=f"リサイズされた画像（幅: {max_width}px）", use_column_width=True)
    
    # 保存場所の情報を表示
    st.success(f"リサイズされた画像が保存されました: {new_filename}")
