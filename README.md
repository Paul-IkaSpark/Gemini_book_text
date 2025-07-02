# Gemini_book_text

## 📚 Turn Any Book into a Multi-Voice Audiobook with AI

**Gemini_book_text** is a Python script that transforms your dialogue-rich text (books, podcasts, scripts) into an audiobook with multiple AI voices. Powered by Google Generative Language API and ffmpeg, this tool enables you to automate the conversion of dialogue into realistic voice-acted audio files.

---

## 🚀 Quick Start

### 1. **Download & Set Up ffmpeg**

- Download the latest ffmpeg build from [btbn/ffmpeg-builds releases](https://github.com/btbn/ffmpeg-builds/releases):
  - Recommended file: **`ffmpeg-master-latest-win64-gpl-shared.zip`**
- Unpack **all files from the `bin` folder** into your project folder (where the script is).

### 2. **Enable Google Generative Language API**

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable the **"Generative Language API"** for your project.
- Generate an API key.

### 3. **Configure Your API Key**

Open the script and replace `"your API here"` with your actual key:

```python
client = genai.Client(api_key="your API here")
```

### 4. **Install Dependencies**

```bash
pip install google-generativeai pydub
```

---

## 🛠️ How It Works

1. **Prepare Your Dialogue**

   - Paste your book/script text into an AI (e.g., Gemini, ChatGPT) and use a prompt to extract all dialogue, assigning clear speaker names.
   - Copy the formatted dialogue (see `dialogue.txt` for an example) into `dialogue.txt` in your project.

2. **Configure Voices**

   - Edit `voice_config.json` to assign voices to each character.  
   - The file contains a list of available voice models for easy selection.

3. **Run the Script**

   ```bash
   python eng_tts_test.py
   ```

   The script processes each scene or dialogue, generates audio parts (e.g., `temp_part_1.wav`, `temp_part_2.wav`, etc.), and then combines them into a single final audiobook file.

4. **Enjoy Your Audiobook!**

   - The output file (e.g., `final_dialogue_YYYYMMDD_HHMMSS.wav`) is your ready-made multi-character audiobook.
   - A test sample is provided: `final_dialogue_20250702_170804.wav` (dated 2025-07-02).

---

## 🎭 Features

- **Multi-Character Support:** Easily add more characters by editing `voice_config.json`.
- **Flexible Voice Models:** Select from a variety of AI voices (see the list in `voice_config.json`).
- **Emotions:** You can experiment with emotions (like laughter) in the dialogue, though results may vary and need more testing.
- **Podcast-Style Output:** Works great for podcasts and dramatized books.

---

## 📋 Example Output

```
Processing dialogue between Mikhail and Evgeniy
Generating part 1... Characters: Mikhail (Fenrir) and Evgeniy (Charon)
Saving file temp_part_1.wav... File saved!

Processing dialogue between Mikhail and Yuriy
Generating part 2... Characters: Mikhail (Fenrir) and Yuriy (Orus)
Saving file temp_part_2.wav... File saved!
...
```

---

## 💡 Tips

- Use any text AI to process your book/script into clear dialogue with speaker names.
- Paste the processed text into `dialogue.txt` before running the script.
- You can add or change characters and their voices in `voice_config.json` — the more, the merrier!
- Experiment with different voice models and emotions for creative results.

---

## 📁 Files

- `eng_tts_test.py` — Main script to run
- `dialogue.txt` — Your prepared dialogue file
- `voice_config.json` — Voice and character configuration
- `final_dialogue_*.wav` — Your finished audiobook
- `temp_part_*.wav` — Intermediate audio parts

---

## ☑️ Requirements

- Python 3.8+
- [ffmpeg](https://github.com/btbn/ffmpeg-builds/releases) (unpacked into project folder)
- Google Generative Language API key

---

Enjoy your AI-powered, multi-character audiobooks!
