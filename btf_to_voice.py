import sys
from pydub import AudioSegment
from gtts import gTTS
import os
f = open(sys.argv[1])
text = ""
for item in f:
  text += item
print(text)
tts = gTTS(text)
tts.save('test.mp3')

sound2 = AudioSegment.from_mp3("test.mp3")
sound1 = AudioSegment.from_mp3("bit.mp3")
output = sound1.overlay(sound2, position=19000)
output.export("finalSong.mp3", format="mp3")

os.system('ffplay finalSong.mp3')

print("results in test.mp3 file ")


