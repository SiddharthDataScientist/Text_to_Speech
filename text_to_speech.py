import gtts
import playsound

text = input('Enter the text you want to convert: ')
speech = gtts.gTTS(text= text, lang='en')

speech.save("Audio.mp3")
playsound.playsound('Audio.mp3')