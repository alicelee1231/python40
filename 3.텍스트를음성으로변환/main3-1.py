from gtts import gTTS

text = "안녕하세요. 내가 이 세계의 왕이다아아악"

tts = gTTS(text = text, lang='ko')
tts.save(r"3.텍스트를음성으로변환/hi.mp3")