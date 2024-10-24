from gtts import gTTS
import os

text = "Selam dostum nasılsın"
tts = gTTS(text=text, lang='tr')
file_name = "output.mp3"
tts.save(file_name)
