import pandas as pd
import streamlit as st
from connectors import get_data

st.set_page_config(page_title="7 Wonders!", page_icon="🎬")
st.title("7 Wonders!")

load_success = get_data()

if load_success:
    st.write('Start building dashboard')