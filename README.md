# Gemini_book_text

Download:
https://github.com/btbn/ffmpeg-builds/releases

ffmpeg-master-latest-win64-gpl-shared.zip

Unpack all files from bin folder, into profect folder

Get "Api generative language" api ENABLED at console.cloud.google.com

And write your API into 
 client = genai.Client(api_key="_your API here_")

Need to install:
pip install google-generativeai pydub

The script working as a part:

Processing dialogue between Mikhail and Evgeniy

Generating part 1...
Characters: Mikhail (Fenrir) and Evgeniy (Charon)
Saving file temp_part_1.wav...
File saved!

Processing dialogue between Mikhail and Yuriy

Generating part 2...
Characters: Mikhail (Fenrir) and Yuriy (Orus)
Saving file temp_part_2.wav...
File saved!

Processing dialogue between Mikhail and Yuriy

Generating part 3...
Characters: Mikhail (Fenrir) and Yuriy (Orus)
Saving file temp_part_3.wav...
File saved!

Processing dialogue between Mikhail and Evgeniy

Generating part 4...
Characters: Mikhail (Fenrir) and Evgeniy (Charon)
Saving file temp_part_4.wav...
File saved!

The languages model names are in:
voice_config.json

There example for 3, it is working like https://notebooklm.google.com/ podcasts

You can try to use emotions like lought and etc, need to be tested more

How it is working, you have text. "TEXT"
Copy and paste "TEXT" into and AI system, tell the prompt to recognize names and write temple as at dialogue.txt
Copy paste text into dialogue.txt then with Ai editing and ready to use

Run eng_tts_test.py

Enjoy. The test provided as final_dialogue_20250702_170804.wav 02/07/25
