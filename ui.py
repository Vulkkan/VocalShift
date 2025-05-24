import streamlit as st
from helper.styles import custom_css
import helper.strings as strings

st.set_page_config(layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)

st.markdown(f"<h1 class='title''>{strings.title}</h1>", unsafe_allow_html=True)
st.write("Speedy transcription and voice-overs")


st.write(""); st.write("") ; st.write("")
st.write(""); st.write("") ; st.write("")


with st.container():
    # st.markdown(f"<h1 class='subtitle-bold''>Select a service</h1>", unsafe_allow_html=True)
    st.header('Select a service')

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write('Generate voice-overs for text files')
        # st.markdown(f"<h1 class='subtitle''>Generate voice-overs for text files</h1>", unsafe_allow_html=True)
        text2audio = st.button('Text to Audio', type='primary')
        if text2audio:
            st.switch_page('pages/text2audio.py')
        st.write('')

    with col3:
        st.write('Generate transcriptions for audio (coming soon)')
        # st.markdown(f"<h1 class='subtitle''>Generate transcriptions for audio</h1>", unsafe_allow_html=True)
        audio2text = st.button('Audio to Text', type='primary')
        if audio2text:
            st.switch_page('pages/audio2text.py')



