# 🎙️ Jervis Voice Assistant using Python

Jervis is a beginner-friendly voice assistant using vanilla Python. It listens to spoken commands through your microphone, converts speech into text, checks the command, and responds using text-to-speech.

## ✨ Features

- Greets the user according to the current time.
- Listens to commands through a microphone.
- Tells the current time.
- Opens Google, YouTube, and ChatGPT in the default web browser.
- Tells a random programming joke.
- Searches Wikipedia and reads a short summary.

## 🛠️ Technologies and libraries

| Library | Purpose |
| --- | --- |
| `SpeechRecognition` | Captures audio and converts speech into text. |
| `PyAudio` | Provides microphone access for SpeechRecognition. |
| `pyttsx3` | Converts text into spoken audio (text-to-speech). |
| `wikipedia` | Searches Wikipedia and retrieves summaries. |
| `pyjokes` | Generates programming jokes. |
| `datetime` | Gets the current time and determines the greeting. |
| `webbrowser` | Opens websites in the default browser. |

## 📋 Requirements

- Python 3.13 or later.
- An available and enabled microphone.
- An internet connection for Google speech recognition and Wikipedia searches.

> **Microphone usage note:** Installing PyAudio does not automatically provide a microphone. Windows must detect an input device under **Settings → System → Sound → Input**. If Windows displays **No input devices found**, fix the Windows microphone or audio-driver issue before running Jervis.

## 📁 Project structure

Your project folder should look like this:

```text
Jervis Voice Assistant/
│
├── .venv/                # Virtual environment (created during setup)
├── main.py               # Main Python program
├── requirements.txt      # Required third-party Python packages
└── README.md             # Project documentation
```

Do not manually create the `.venv` folder. The setup instructions below create it for you.

## 🚀 Setup and installation 

There are two ways to download Jervis Voice Assistant on your computer:

### 1. Using Git
```bash
git clone https://github.com/proshanta-pal19/Jervis-Voice-Assistant-in-Python.git
```

### 2. Install Dependencies & Run Jervis
Make sure Python is installed. Then run:
```bash
pip install -r requirements.txt
```

Make sure the virtual environment is activated and that your terminal is in the project folder. Then run:

```bash
python main.py
```

## 🗣️ Example voice commands

| Say this | Jervis's action |
| --- | --- |
| "What is the time?" | Tells you the current time. |
| "Open Google" | Opens Google in your browser. |
| "Open YouTube" | Opens YouTube in your browser. |
| "Open ChatGPT" | Opens ChatGPT in your browser. |
| "Tell me a joke" | Tells a programming joke. |
| "Search Wikipedia for Python" | Searches Wikipedia for Python and reads a summary. |
| "Goodbye" or "exit" | Closes the assistant. |

## 📝 Notes

- The program uses Google's online speech-recognition service through `recognize_google()`, so an internet connection is required for speech-to-text.
- `pyttsx3` performs text-to-speech locally on your computer.
- The microphone must be connected, enabled, and available to Windows desktop applications.
- This is an educational beginner project. It is not a continuously streaming or wake-word-based assistant.