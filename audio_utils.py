## @file audio_utils.py
# @brief Utilitaires pour la lecture et l'écriture de fichiers audio WAV
# @details Ce fichier contient des fonctions pour lire et écrire des fichiers audio
# au format WAV, en utilisant la bibliothèque scipy.io.wavfile.

from scipy.io import wavfile
import numpy as np

## @brief Lit un fichier audio WAV
# @param filename Chemin du fichier WAV à lire
# @return Tuple contenant la fréquence d'échantillonnage et les données audio
# @details Si le fichier est stéréo, seul le canal gauche est retourné
def read_wav(filename):
    ## Lecture du fichier WAV
    sample_rate, data = wavfile.read(filename)
    
    ## Conversion en mono si le fichier est stéréo
    if len(data.shape) > 1:
        data = data[:, 0]  # Prendre seulement le canal gauche si stéréo
    
    return sample_rate, data

## @brief Écrit les données audio dans un fichier WAV
# @param filename Chemin du fichier WAV à écrire
# @param sample_rate Fréquence d'échantillonnage des données audio
# @param data Données audio à écrire
# @details Les données sont converties en int16 et limitées entre -32768 et 32767
def write_wav(filename, sample_rate, data):
    ## Conversion et limitation des données
    limited_data = np.int16(np.clip(data, -32768, 32767))
    
    ## Écriture du fichier WAV
    wavfile.write(filename, sample_rate, limited_data)