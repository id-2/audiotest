import streamlit as st
import whisper
from whisper.utils import get_partial_transcript

model = whisper.load_model("medium")

def transcribe_realtime(audio):
  generator = model.transcribe_generator(audio)

  for result in generator:
    yield result["text"]

st.title("Real-time Audio Transcription")

uploaded_file = st.file_uploader("Choose an audio file", type=["mp4", "mp3", "ogg"])

if uploaded_file is not None:
  audio_bytes = uploaded_file.read()

  for transcript in transcribe_realtime(audio_bytes):
    st.write(transcript)
