## @file main.py
# @brief Interface graphique pour l'égaliseur audio
# @details Ce fichier contient la classe EqualizerGUI qui gère l'interface utilisateur
# pour l'égaliseur audio, permettant la sélection de fichiers, l'ajustement des gains
# et le traitement audio.

import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
from signal_processing import equalizer, generate_impulse_response
from audio_utils import read_wav, write_wav

## @class EqualizerGUI
# @brief Classe principale pour l'interface graphique de l'égaliseur
class EqualizerGUI:
    ## @brief Constructeur de la classe EqualizerGUI
    # @param master Fenêtre principale Tkinter
    def __init__(self, master):
        self.master = master
        master.title("Égaliseur Audio")
        master.geometry("600x400")

        self.filename = tk.StringVar()
        self.gains = [tk.DoubleVar(value=1.0) for _ in range(5)]

        self.create_widgets()

    ## @brief Crée et place les widgets de l'interface graphique
    def create_widgets(self):
        # Bouton de sélection de fichier
        ttk.Button(self.master, text="Sélectionner un fichier WAV", command=self.select_file).pack(pady=10)
        ttk.Label(self.master, textvariable=self.filename).pack()

        # Sliders pour les bandes de fréquences
        freq_bands = ["20-200 Hz", "200-800 Hz", "800-2500 Hz", "2500-8000 Hz", "8000-20000 Hz"]
        for i, band in enumerate(freq_bands):
            ttk.Label(self.master, text=band).pack()
            ttk.Scale(self.master, from_=0, to=2, orient='horizontal', variable=self.gains[i], length=300).pack()

        # Bouton de traitement
        ttk.Button(self.master, text="Appliquer l'égalisation", command=self.process_audio).pack(pady=20)

    ## @brief Ouvre une boîte de dialogue pour sélectionner un fichier WAV
    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if file_path:
            self.filename.set(file_path)

    ## @brief Traite le fichier audio sélectionné avec les gains spécifiés
    def process_audio(self):
        if not self.filename.get():
            print("Veuillez sélectionner un fichier WAV")
            return

        sample_rate, audio_data = read_wav(self.filename.get())
        gains = [gain.get() for gain in self.gains]
        
        equalized_data = equalizer(audio_data, gains)
        
        output_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if output_file:
            write_wav(output_file, sample_rate, equalized_data)
            print(f"Fichier égalisé sauvegardé : {output_file}")

## @brief Point d'entrée principal du programme
if __name__ == "__main__":
    root = tk.Tk()
    app = EqualizerGUI(root)
    root.mainloop()