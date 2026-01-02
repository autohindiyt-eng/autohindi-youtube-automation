from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip

# Testo in Hindi
text_hindi = "नमस्ते! यह आपका पहला ऑटो शॉर्ट है।"

# Genera audio
audio_path = "assets/audio/audio.mp3"
tts = gTTS(text=text_hindi, lang='hi')
tts.save(audio_path)

# Genera video da immagine
image_path = "assets/images/sample.jpg"
clip = ImageClip(image_path, duration=5)
clip = clip.set_audio(AudioFileClip(audio_path))

# Salva video
output_path = "outputs/short_test.mp4"
clip.write_videofile(output_path, fps=24)

print(f"Video generato: {output_path}")
