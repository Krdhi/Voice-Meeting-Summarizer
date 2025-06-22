# 🎤 Voice Meeting Summarizer

#Recommended to run this on colab as there are less dependencies
# For Colab :
# Required packages: Run as separate block if using Colab
# !pip install gradio openai-whisper openai scipy

#For PyCharm/VSCode :
# Required packages: Run this command on the terminal if using Pycharm/VScode
# pip install gradio openai scipy numpy python-dotenv
# pip install git+https://github.com/openai/whisper.git
#If you're on macOS and using a Python version installed from python.org, run:
# /Applications/Python\ 3.13/Install\ Certificates.command
#for other versions:
#open /Applications/Python\ */Install\ Certificates.command

import gradio as gr
import openai
import whisper
import os
import tempfile
import scipy.io.wavfile
import numpy as np
from dotenv import load_dotenv

# ✅ Load API Key from .env (optional)
load_dotenv()
ENV_API_KEY = os.getenv("OPENAI_API_KEY")

# 🧠 Initialize the Whisper model
whisper_model = whisper.load_model("base")

# 🎯 Function to transcribe audio and summarize key points
def summarize_meeting(audio_input, api_key):
    try:
        # Prefer user-supplied API key, fallback to .env key
        api_key = api_key or ENV_API_KEY
        if not api_key:
            return "⚠️ Error: OpenAI API key is required.", ""

        client = openai.OpenAI(api_key=api_key)

        # ✅ Handle audio input from Gradio's numpy format
        if isinstance(audio_input, tuple):
            sr, data = audio_input
            if data is None or not np.any(data):
                return "⚠️ Error: No valid audio recorded. Please try again.", ""
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                scipy.io.wavfile.write(tmp_file.name, sr, data)
                audio_filepath = tmp_file.name
        else:
            return "⚠️ Error: Invalid audio input.", ""

        # 1️⃣ Transcribe audio using Whisper
        transcription = whisper_model.transcribe(audio_filepath)
        transcript_text = transcription["text"]

        # 2️⃣ Summarize transcript using GPT-4
        prompt = f"""
You are a meeting summarization assistant.

Here is the transcript of a meeting:
{transcript_text}

Summarize the meeting into:
1. A brief summary
2. Action items
3. Key takeaways
4. Reminders (if any)

Use markdown format with clear section headers.
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI meeting assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        output = response.choices[0].message.content.strip()
        return transcript_text, output

    except Exception as e:
        return f"⚠️ Error: {str(e)}", ""

# 🎛️ Gradio Interface
def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🎤 Voice Meeting Summarizer")

        #You can avoid below code for API Key and reference the .env file if you are using PyCharm/VSCode.
        api_key_input = gr.Textbox(label="🔑 Enter your OpenAI API Key", type="password", value=ENV_API_KEY or "")
        audio_input = gr.Audio(label="🎧 Record Meeting Audio", type="numpy", sources=["microphone"], format="wav")

        transcript_text = gr.Textbox(label="🔤 Live Transcript", lines=10)
        output_text = gr.Textbox(label="📜 Summary, Action Items & Takeaways", lines=20)

        summarize_button = gr.Button("🧠 Summarize Meeting")
        summarize_button.click(fn=summarize_meeting, inputs=[audio_input, api_key_input], outputs=[transcript_text, output_text])

    demo.launch(share=True)

# 🚀 Run the app
if __name__ == "__main__":
    create_ui()
