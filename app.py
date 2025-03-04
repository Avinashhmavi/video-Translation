# app.py
import os
import tempfile
import subprocess
import streamlit as st
from dotenv import load_dotenv
import whisper
from moviepy.editor import VideoFileClip
from deep_translator import GoogleTranslator
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from pydub import AudioSegment

# Load environment variables
load_dotenv()

# Initialize ElevenLabs client
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def extract_audio(video_path):
    """Extract audio from video using MoviePy"""
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_audio(audio_path):
    """Transcribe audio using Whisper"""
    model = whisper.load_model("medium")
    result = model.transcribe(audio_path, word_timestamps=True)
    return result['segments']

def translate_text(segments, target_lang):
    """Translate text using Google Translate"""
    translated_segments = []
    for segment in segments:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(segment['text'])
        translated_segments.append({
            'start': segment['start'],
            'end': segment['end'],
            'text': translated
        })
    return translated_segments

def generate_voice(segments, output_path, voice_id):
    """Generate translated voice using ElevenLabs"""
    full_audio = AudioSegment.empty()
    
    for seg in segments:
        audio = client.generate(
            text=seg['text'],
            voice=voice_id,
            model="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            temp_path = f.name
            save(audio, temp_path)
        
        audio_segment = AudioSegment.from_mp3(temp_path)
        os.remove(temp_path)
        
        target_duration = (seg['end'] - seg['start']) * 1000  # ms
        if len(audio_segment) > target_duration:
            audio_segment = audio_segment[:target_duration]
        else:
            silence = AudioSegment.silent(target_duration - len(audio_segment))
            audio_segment += silence
        
        full_audio += audio_segment
    
    full_audio.export(output_path, format="wav")
    return output_path

def merge_audio_video(video_path, audio_path, output_path):
    """Merge audio with video using FFmpeg CLI"""
    cmd = [
        'ffmpeg',
        '-y',  # Overwrite output
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',  # Copy video stream
        '-c:a', 'aac',  # Encode audio to AAC
        '-map', '0:v:0',  # Take video from first input
        '-map', '1:a:0',  # Take audio from second input
        '-shortest',  # Match shortest duration
        output_path
    ]
    
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        st.write("FFmpeg Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"FFmpeg Error: {e.stderr}")
        raise

def main():
    st.title("🎥 AI Video Translator")
    
    # Supported Indian languages
    indian_langs = {
        "Hindi": "hi",
        "Tamil": "ta",
        "Telugu": "te",
        "Bengali": "bn",
        "Marathi": "mr",
        "Gujarati": "gu",
        "Punjabi": "pa"
    }
    
    # File upload
    video_file = st.file_uploader("Upload video", type=["mp4", "mov"])
    
    # Get available voices
    voices = client.voices.get_all().voices
    voice_options = {v.name: v.voice_id for v in voices}
    
    # UI elements
    target_lang = st.selectbox("Target Language", list(indian_langs.keys()))
    voice_name = st.selectbox("Voice Style", list(voice_options.keys()))
    
    if video_file and st.button("Translate Video"):
        with st.spinner("Processing..."):
            # Initialize paths
            video_path = audio_path = translated_audio = output_path = None
            
            try:
                # Save uploaded video
                with tempfile.NamedTemporaryFile(delete=False) as f:
                    video_path = f.name
                    f.write(video_file.read())
                
                # Processing pipeline
                audio_path = extract_audio(video_path)
                segments = transcribe_audio(audio_path)
                translated_segments = translate_text(segments, indian_langs[target_lang])
                translated_audio = "translated.wav"
                generate_voice(translated_segments, translated_audio, voice_options[voice_name])
                output_path = "translated_video.mp4"
                merge_audio_video(video_path, translated_audio, output_path)
                
                # Display results
                st.success("Translation Complete!")
                st.video(output_path)
                
                # Download button
                with open(output_path, "rb") as f:
                    st.download_button(
                        "Download Translated Video",
                        f.read(),
                        file_name="translated_video.mp4",
                        mime="video/mp4"
                    )
            
            except Exception as e:
                st.error(f"Error: {str(e)}")
            finally:
                # Cleanup
                for path in [video_path, audio_path, translated_audio, output_path]:
                    if path and os.path.exists(path):
                        os.remove(path)

if __name__ == "__main__":
    main()