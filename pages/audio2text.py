import streamlit as st
from helper.styles import custom_css
import helper.strings as strings
import helper.a2t as a2t

st.set_page_config(layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)

st.markdown(f"<h1 class='title''>{strings.title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 class='subtitle-bold''>Audio to Text</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 class='subtitle''>Service coming soon..</h1>", unsafe_allow_html=True)

st.write(""); st.write("") ; st.write(""); st.write("")

