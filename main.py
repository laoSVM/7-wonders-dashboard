import pandas as pd
import streamlit as st
from connectors import get_data

st.set_page_config(page_title="7 Wonders!", page_icon="🎬")
st.title("7 Wonders!")

file_id = st.secrets["FILE_ID"]
load_success = get_data(file_id)

if load_success:
    st.write('7 Wonders 启动!')