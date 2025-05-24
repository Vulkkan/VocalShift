import io
import PyPDF2
from gtts import gTTS
# from pydub import AudioSegment


# Function to extract text from a file (txt or pdf)
def extract_text_from_file(file_object) -> str:
    if file_object.name.endswith(".txt"):
        # Read text file from the uploaded file
        return file_object.getvalue().decode("utf-8")  # Convert bytes to string
    elif file_object.name.endswith(".pdf"):
        # Read PDF file
        pdf_reader = PyPDF2.PdfReader(file_object)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        raise ValueError("Unsupported file format. Use .txt or .pdf")

# Function to generate audio using gTTS
def generate_audio_gtts(
        input: str, 
        output: str, 
        speed: bool = False,
        language: str = 'en',
        accent: str = "co.uk"
        ):
    tts = gTTS(
        text=input,
        lang=language, 
        slow=speed, 
        tld=accent  # Using accent (Top Level Domain)
    )
    tts.save(output)


# # Function to adjust audio speed
# def adjust_audio_speed(audio_path: str, speed_factor: float) -> AudioSegment:
#     audio = AudioSegment.from_mp3(audio_path)
#     new_frame_rate = int(audio.frame_rate * speed_factor)
#     return audio._spawn(audio.raw_data, overrides={'frame_rate': new_frame_rate})


# def adjust_audio_speed_with_pitch_compensation(audio_path: str, speed_factor: float) -> AudioSegment:
#     """Adjusts the speed of the audio while compensating for pitch using time-stretching."""
#     # Load the audio
#     audio = AudioSegment.from_mp3(audio_path)
    
#     # Adjust speed while compensating for pitch by time-stretching
#     if speed_factor != 1.0:
#         # Apply time stretching - this method allows speed adjustment without affecting pitch
#         new_sample_rate = int(audio.frame_rate * speed_factor)
#         audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
        
#         # Ensure the audio still has the correct format (to avoid distorting the file)
#         audio = audio.set_frame_rate(audio.frame_rate)
    
#     return audio

