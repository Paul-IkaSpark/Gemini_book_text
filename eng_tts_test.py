from google import genai
from google.genai import types
import wave
import base64
from datetime import datetime
import os
from pydub import AudioSegment
import re
import json

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    print(f"Saving file {filename}...")
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)
    print("File saved!")

def clean_dialogue_text(text):
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\*[^*]*\*', '', text)
    text = re.sub(r'^Speaker[12]:\s*', '', text)
    return text.strip()

def generate_audio_part(dialogue_text, voice1, voice2, part_number, char1, char2):
    dialogue_lines = dialogue_text.split('\n')
    cleaned_lines = []
    for line in dialogue_lines:
        if ':' in line:
            cleaned_line = f"{line.split(':')[0]}: {clean_dialogue_text(line.split(':', 1)[1])}"
            cleaned_lines.append(cleaned_line)
    
    cleaned_dialogue = '\n'.join(cleaned_lines)

    prompt = f"""Make Speaker1 ({char1}) and Speaker2 ({char2}) sound emotional based on their descriptions in parentheses. TTS the following conversation:

{cleaned_dialogue}"""

    print(f"\nGenerating part {part_number}...")
    print(f"Characters: {char1} ({voice1}) and {char2} ({voice2})")
    
    client = genai.Client(api_key="__")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=[
                        types.SpeakerVoiceConfig(
                            speaker='Speaker1',
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=voice1
                                )
                            )
                        ),
                        types.SpeakerVoiceConfig(
                            speaker='Speaker2',
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=voice2
                                )
                            )
                        )
                    ]
                )
            )
        )
    )

    data = response.candidates[0].content.parts[0].inline_data.data
    decoded_data = base64.b64decode(data)
    
    temp_filename = f'temp_part_{part_number}.wav'
    wave_file(temp_filename, decoded_data)
    return temp_filename

def get_character_name(line):
    match = re.search(r'\((.*?)[,)]', line)
    if match:
        return match.group(1).strip()
    return None

def process_dialogue():
    try:
        with open('dialogue.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("\nError: File dialogue.txt not found!")
        return
    except Exception as e:
        print(f"\nError while reading file: {str(e)}")
        return

    with open('voice_config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    lines = [line.strip() for line in lines if line.strip()]
    
    dialogues = []
    current_dialogue = []
    
    for line in lines:
        current_dialogue.append(line)
        if len(current_dialogue) == 2:
            dialogues.append(current_dialogue)
            current_dialogue = []
    
    if current_dialogue:
        dialogues.append(current_dialogue)
    
    temp_files = []
    for i, dialogue_pair in enumerate(dialogues):
        # THE ONLY CHANGE - check for temp file
        temp_file = f'temp_part_{i+1}.wav'
        if os.path.exists(temp_file):
            temp_files.append(temp_file)
            continue
            
        char1 = get_character_name(dialogue_pair[0])
        char2 = get_character_name(dialogue_pair[1]) if len(dialogue_pair) > 1 else None
        
        if char1 and char2:
            voice1 = config["characters"][char1]["voice"]
            voice2 = config["characters"][char2]["voice"]
            dialogue_text = '\n'.join(dialogue_pair)
            
            print(f"\nProcessing dialogue between {char1} and {char2}")
            temp_file = generate_audio_part(dialogue_text, voice1, voice2, i+1, char1, char2)
            temp_files.append(temp_file)
    
    if temp_files:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_filename = f'final_dialogue_{timestamp}.wav'
        
        combined = AudioSegment.empty()
        for temp_file in temp_files:
            audio_segment = AudioSegment.from_wav(temp_file)
            combined += audio_segment
            os.remove(temp_file)
        
        combined.export(final_filename, format="wav")
        print(f"\nDone! Final audio saved to file: {final_filename}")
        return final_filename
    else:
        print("\nFailed to create audio files")

if __name__ == "__main__":
    process_dialogue()