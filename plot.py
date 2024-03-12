import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open(r"C:\Users\hanan\OneDrive\Desktop\Speech_Processing_Basics\OAF_bite_angry.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples/sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype = np.int16)

"""np.frombuffer(): This NumPy function creates an array from a buffer of bytes.
It takes two main arguments:
signal_wave: The buffer containing the audio data.
dtype=np.int16: Specifies the data type of the elements in the array, in this case, 16-bit signed integers, commonly used for audio signals."""

times = np.linspace(0, t_audio, num=n_samples)

"""np.linspace(): This NumPy function generates a sequence of evenly spaced numbers within a specified interval.
It takes three main arguments:
0: The starting value of the sequence (time zero in this case).
t_audio: The end value of the sequence (total duration of the audio).
num=n_samples: The number of samples in the audio signal. The function generates n_samples equally spaced values between 0 and t_audio."""

plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio) #limit the x axis
plt.show()

