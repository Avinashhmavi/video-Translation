```markdown
# 🎥 AI Video Translator

Welcome to the **AI Video Translator**! This powerful tool allows you to seamlessly translate videos into multiple Indian languages with just a few clicks. Whether you're looking to localize content, make videos accessible to a broader audience, or simply experiment with AI-powered translation, this app has got you covered.

---

## 🌟 Features

- **Multi-language Support**: Translate videos into popular Indian languages, including:
  - Hindi (हिंदी)
  - Tamil (தமிழ்)
  - Telugu (తెలుగు)
  - Bengali (বাংলা)
  - Marathi (मराठी)
  - Gujarati (ગુજરાતી)
  - Punjabi (ਪੰਜਾਬੀ)

- **AI-Powered Transcription**: Utilizes OpenAI's Whisper model for accurate transcription of video audio.

- **Real-time Translation**: Leverages Google Translate API to provide high-quality translations.

- **Voice Cloning**: Uses ElevenLabs' advanced voice synthesis technology to generate natural-sounding translated audio in various voice styles.

- **Seamless Integration**: Combines video and translated audio using FFmpeg for professional-quality output.

- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.

---

## 🚀 Live Demo

Experience the magic of AI Video Translator by visiting the live demo:

👉 [Try it now!](https://video-translation-app.streamlit.app/)

---

## ⚙️ Pre-requisites

Before running the app locally, ensure you have the following installed:

1. **Python 3.8+**: Download it from [python.org](https://www.python.org/downloads/).
2. **FFmpeg**: Install FFmpeg for audio-video processing.
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html).
   - **macOS**: Use Homebrew: `brew install ffmpeg`.
   - **Linux**: Use your package manager, e.g., `sudo apt install ffmpeg`.
3. **Dependencies**: Install the required Python libraries using:
   ```bash
   pip install -r requirements.txt
   ```
4. **API Keys**:
   - Obtain an API key from [ElevenLabs](https://elevenlabs.io/) and add it to your `.env` file:
     ```
     ELEVENLABS_API_KEY=your_api_key_here
     ```
   - Add the same key to Streamlit secrets (`secrets.toml`) if deploying on Streamlit Cloud.

---

## 📋 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/video-translation-app.git
   cd video-translation-app
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`.

---

## 🛠️ How It Works

1. **Upload a Video**: Drag and drop your video file (MP4 or MOV format) into the app.
2. **Select Target Language**: Choose the language you want to translate the video into.
3. **Pick a Voice Style**: Select from a variety of natural-sounding voices for the translated audio.
4. **Translate**: Click "Translate Video" and let the AI do its magic!
5. **Download**: Once the process is complete, download the translated video with a single click.

---

## 📦 Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Whisper**: For transcribing video audio into text.
- **Google Translate API**: For translating transcribed text into the target language.
- **ElevenLabs**: For generating high-quality synthetic voices in multiple languages.
- **FFmpeg**: For merging translated audio with the original video.
- **MoviePy**: For extracting audio from video files.
- **PyDub**: For audio processing and manipulation.

---

## 📞 Contact

For any questions, feedback, or collaboration opportunities, feel free to reach out:

- Email: avi.hm24@gmail.com
- LinkedIn: [Your LinkedIn Profile]((https://www.linkedin.com/in/avinashhm/))

---

## 🙏 Acknowledgments

Special thanks to the following projects and services that made this app possible:

- [OpenAI Whisper](https://github.com/openai/whisper)
- [ElevenLabs](https://elevenlabs.io/)
- [Google Translate API](https://cloud.google.com/translate)
- [Streamlit](https://streamlit.io/)
- [FFmpeg](https://ffmpeg.org/)

---

Happy translating! 🌍🎥
```
