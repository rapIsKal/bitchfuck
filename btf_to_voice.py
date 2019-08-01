import sys
from gtts import gTTS
import os
f = open(sys.argv[1])
text = ""
for item in f:
  text += item
print(text)
tts = gTTS(text)
tts.save('test.mp3')

os.system('ffplay test.mp3')

print("results in test.mp3 file ")