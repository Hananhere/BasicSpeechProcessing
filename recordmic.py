import pyaudio
import wave

fpb = 3200
form= pyaudio.paInt16
chan = 1
rate_ = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format = form,
    channels = chan,
    rate = rate_,
    input = True,
    frames_per_buffer = fpb
    )

print("Start recording")

seconds = 5
frames = []

for i in range(0, int(rate_/fpb*seconds)):
    data = stream.read(fpb)
    frames.append(data)
    
stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output1.wav", "wb")
obj.setnchannels(chan)
obj.setsampwidth(p.get_sample_size(form))
obj.setframerate(rate_)
obj.writeframes(b"".join(frames))
obj.close()
