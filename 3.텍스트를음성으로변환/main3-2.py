from gtts import gTTS
from playsound import playsound
import os

a =os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(a)
text = "hi this is your king"

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")