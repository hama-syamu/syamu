# Streamlitライブラリをインポート
import streamlit as st

import random
st.title('おみくじアプリ')

if st.button('おみくじを引く'):

    results = ['菅野美穂…','おい！ゴルァ！免許持ってんのか！！','よし、お前らクルルァについてこい！','あたまに来ますよー','there!','ココアライオン',"ん、５点！"
    ,"何を四天王…？"]
    result = random.choice(results)
    st.write(f'結果:{result}')