from pydub import AudioSegment

audio = AudioSegment.from_wav(r"C:\Users\hanan\OneDrive\Desktop\Speech_Processing_Basics\output1.wav")

audio =audio +6
audio = audio*2

audio = audio.fade_in(2000)

audio.export("manipulate.wav", format="wav")

audio2 = AudioSegment.from_wav("manipulate.wav")
print("done")