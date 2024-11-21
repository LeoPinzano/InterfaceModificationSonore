from scipy.io import wavfile
import numpy as np

def read_wav(filename):
    sample_rate, data = wavfile.read(filename)
    if len(data.shape) > 1:
        data = data[:, 0]  # Prendre seulement le canal gauche si stéréo
    return sample_rate, data

def write_wav(filename, sample_rate, data):
    wavfile.write(filename, sample_rate, np.int16(np.clip(data, -32768, 32767)))