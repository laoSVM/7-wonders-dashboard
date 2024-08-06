import pandas as pd
import streamlit as st
from data import GameManager

st.set_page_config(page_title="7 Wonders!", page_icon="🎬")
st.title("7 Wonders!")

file_id = st.secrets["FILE_ID"]
gm = GameManager(file_id)
load_success = gm.download_data()

if load_success:
    st.write('7 Wonders 启动!')