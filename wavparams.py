import wave

obj = wave.open(r"C:\Users\hanan\OneDrive\Desktop\Speech_Processing_Basics\OAF_bite_angry.wav")

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

obj.close()

obj_new = wave.open("OAF_angry_new_chan2.wav", "wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(1)
obj_new.setframerate(24414.0)

obj_new.writeframes(frames)
obj_new.close()

""" Reducing the sample width:  will lead to loss of audio quality. With fewer bits to represent each sample, the dynamic range (difference between quietest and loudest sounds) will be reduced, potentially causing audio clipping (distortion) or reduced signal-to-noise ratio (increased background noise). 
    higher sample rate might capture wider range of frequencies, but would increase the file size.
    
    Channels: Increasing the channel shouldnt apparently(?) affect the audio but we can see a change in pitch in the experiment.
    
    Frame rate: Frame rate modification affects playback software interpretation, not the audio itself.
    Correct Interpretation: Software adjusts playback speed (e.g., halves speed if frame rate doubles) to maintain original duration.
    Incorrect Interpretation: Software plays at original speed, resulting in faster playback (perceived pitch increase) but unchanged duration.
"""
