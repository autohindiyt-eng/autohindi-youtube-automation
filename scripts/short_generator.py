from gtts import gTTS
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import os

# Testo in Hindi per il Short
text_hindi = "नमस्ते! यह आपका पहला ऑटो शॉर्ट है।"  # "Ciao! Questo è il tuo primo Short automatico."

# Crea l'audio con gTTS
audio_path = "assets/audio/audio.mp3"
tts = gTTS(text=text_hindi, lang='hi')
tts.save(audio_path)

# Crea un video da immagine e aggiungi audio
image_path = "assets/images/sample.jpg"
clip = ImageClip(image_path, duration=5)  # durata 5 secondi
clip = clip.set_audio(AudioFileClip(audio_path))

# Salva il video finale
output_path = "outputs/short_test.mp4"
clip.write_videofile(output_path, fps=24)

print(f"Video generato: {output_path}")
