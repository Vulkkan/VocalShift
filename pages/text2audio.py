import os
import streamlit as st
from helper.styles import custom_css
import helper.strings as strings
import helper.t2a as t2a
import helper.mappings as mappings
import tempfile


st.set_page_config(layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)

st.markdown(f"<h1 class='title''>{strings.title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 class='subtitle-bold''>Text to Audio</h1>", unsafe_allow_html=True)

st.write(""); st.write("")


col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    st.markdown(f"<h1 class='subtitle-bold''>Set Parameters</h1>", unsafe_allow_html=True)

    # Speed Selection
    speed = st.selectbox('Speed', options=['Fast', 'Slow'])
    speed_factor = 1.0  # Default speed factor
    if speed == 'Fast':
        speed_factor = 1.5
    elif speed == 'Slow':
        speed_factor = 0.5
    
    # Language
    language_code = st.selectbox(
        'Language',
        options=list(mappings.language_mapping.keys()),
        format_func=lambda code: mappings.language_mapping.get(code, code) 
        )
    
    # Accent
    accent_code = st.selectbox(
        'Accent',
        options=list(mappings.accent_mapping.keys()),
        format_func=lambda code: mappings.accent_mapping.get(code, code) 
        )


# (Column) Upload Section
with col3:
    st.markdown(f"<h1 class='subtitle-bold''>Upload</h1>", unsafe_allow_html=True)

    text_input = st.file_uploader('Upload a text file containing the data to convert', type=['txt'])

    if text_input is not None:
        progress = st.text("Processing...")
        progress_bar = st.progress(0)

        # Extract text from the uploaded file
        extracted_text = t2a.extract_text_from_file(text_input)

        # Update progress bar while processing
        progress_bar.progress(40)

        # Generate audio using the backend (t2a.py)
        output_audio_path = tempfile.mktemp(suffix=".mp3")
        t2a.generate_audio_gtts(extracted_text, output_audio_path, speed=speed == 'Slow', language=language_code, accent=accent_code)

        # Adjust the audio speed
        adjusted_audio = t2a.adjust_audio_speed(output_audio_path, speed_factor)
        adjusted_audio_path = tempfile.mktemp(suffix="_adjusted.mp3")
        adjusted_audio.export(adjusted_audio_path, format="mp3")

        # Update progress bar for audio generation completion
        progress_bar.progress(80)

        # Display audio file download button and playback interface
        with open(output_audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')

        # Allow user to download the audio file
        st.download_button(
            label="Download Audio",
            data=audio_bytes,
            file_name="output_audio.mp3",
            mime="audio/mp3"
        )

        # Remove progress bar
        progress_bar.progress(100)
        progress.empty()
        progress_bar.empty()

        # Clean up the temp files
        os.remove(output_audio_path)
        os.remove(adjusted_audio_path)