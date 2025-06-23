# 🎤 Voice Meeting Summarizer — Audio-to-Insight Agent (Python 3.13 Compatible)

*Record your meeting, transcribe it, and receive instant summaries with action items using Whisper + GPT-4.*

---

## 🌍 Project Description

The Voice Meeting Summarizer captures spoken content from your microphone, transcribes it using OpenAI's **Whisper model**, and summarizes it with **GPT-4**. It’s designed for professionals who want to capture and understand meetings quickly.

---

## 📁 Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)

---

## ✨ Features

| Feature                    | Details                                               |
| -------------------------- | ----------------------------------------------------- |
| 🎙️ Audio Recording        | Record meetings directly in the browser               |
| 📝 Whisper Transcription   | Transcribes recorded audio to text                    |
| 🧠 GPT-4 Summary Generator | Extracts summary, action items, key takeaways         |
| 🔐 API Key Support         | OpenAI API handled securely via .env or textbox input |
| 🖼️ Gradio Interface       | Intuitive browser-based interface                     |
| ✅ Cross-platform           | Runs in Colab or locally in PyCharm (Python 3.13)     |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourname/voice-meeting-summarizer.git
cd voice-meeting-summarizer
```

### 2. Create and activate virtual environment

```bash
python3.13 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install gradio openai scipy numpy python-dotenv
pip install git+https://github.com/openai/whisper.git
```

> ⚠️ macOS Python installs might require this step for SSL:

```bash
open /Applications/Python\ */Install\ Certificates.command
```

> ✅ Colab Users:

```python
!pip install gradio openai-whisper openai scipy
```

---

## 💻 Usage

Run the following command to launch the app:

```bash
python app.py
```

Then:

* Record audio from your microphone
* Provide OpenAI API key if not stored in `.env`
* Get a full transcript + bullet summary, action items & reminders

---

## 📂 Project Structure

```
voice-meeting-summarizer/
├── app.py               # Main script with UI and logic
├── .env                 # Store your OpenAI API key securely (optional)
├── README.md            # This file
```

---

## 📝 Notes

* The Whisper model used is `base`. You can change it to `medium` or `large` in the code.
* The transcript length is truncated if it’s too large for summarization.
* Ideal for meeting recaps, interview notes, content research, and personal journaling.

---

## 📜 License

MIT License — Free to use and modify. Attribution appreciated.

---

## 🙌 Acknowledgements

* [OpenAI Whisper](https://github.com/openai/whisper)
* [OpenAI GPT](https://platform.openai.com/)
* [Gradio](https://gradio.app/)
