from vosk import Model, KaldiRecognizer
import wave
import json
import os


'''
Audio file format: must be mono, WAV, PCM encoded.

Conversion can be done using ffmpeg:
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
'''


def transcribe_vosk(audio_path: str):
    # ✅ Load model from local path
    model_path = "models/vosk-model-en-us-0.22-lgraph"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Vosk model not found at {model_path}")

    model = Model(model_path)

    # ✅ Open audio file
    wf = wave.open(audio_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000, 44100]:
        raise ValueError("Audio must be mono WAV (PCM) with sample rate 8000/16000/44100")

    rec = KaldiRecognizer(model, wf.getframerate())
    results = []

    while True:
        data = wf.readframes(4000)
        if not data:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result())["text"])

    results.append(json.loads(rec.FinalResult())["text"])
    transcript = " ".join(results)


    # ✅ Save transcript
    output_dir = "output/audio"
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_file = os.path.join(output_dir, f"{base_name}_transcript.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"Transcript saved to {output_file}")



transcribe_vosk("input/audio_notes/recording.wav")
