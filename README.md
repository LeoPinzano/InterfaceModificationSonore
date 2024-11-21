# Interface pour modifications sonores - Égaliseur

Ce projet implémente une interface graphique en Python permettant de modifier des bandes sonores en utilisant l'égalisation.

## Fonctionnalités

- Sélection de fichier WAV
- Égaliseur à 5 bandes de fréquences
- Traitement et sauvegarde du fichier audio modifié

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-nom-utilisateur/interface-modifications-sonores.git
   ```

2. Installez les dépendances :
   ```
   pip install numpy scipy matplotlib tkinter
   ```
## Utilisation

Exécutez le fichier principal :

```
python main.py
```

Étapes à suivre :

Sélectionnez un fichier WAV à traiter.
Ajustez les sliders pour chaque bande de fréquence.
Cliquez sur le bouton "Appliquer l'égalisation" pour traiter le son.

## Structure du projet

- `main.py` : Interface graphique et logique principale
- `signal_processing.py` : Fonctions de traitement du signal
- `audio_utils.py` : Utilitaires pour la manipulation des fichiers audio

## Fonctions principales et algorithmes

### main.py

1. `EqualizerGUI.__init__(self, master)`:
   - Initialise l'interface graphique
   - Crée les variables pour stocker le nom du fichier et les gains

2. `create_widgets(self)`:
   - Crée les éléments de l'interface : boutons, sliders, labels
   - Configure les sliders pour les 5 bandes de fréquences

3. `select_file(self)`:
   - Ouvre une boîte de dialogue pour sélectionner un fichier WAV
   - Met à jour la variable `filename`

4. `process_audio(self)`:
   - Lit le fichier WAV sélectionné
   - Récupère les valeurs des gains depuis les sliders
   - Applique l'égalisation au signal audio
   - Sauvegarde le fichier audio traité

### signal_processing.py

1. `calculate_coefficients(band_index)`:
   - Calcule les coefficients a0, a1, b1, b2 pour chaque bande de fréquence
   - Utilise des valeurs prédéfinies pour chaque bande

2. `filter_band(data, a0, a1, b1, b2)`:
   - Applique un filtre du second ordre au signal audio
   - Utilise une boucle pour calculer chaque échantillon filtré

3. `equalizer(data, gains)`:
   - Applique l'égalisation au signal audio complet
   - Pour chaque bande :
     - Calcule les coefficients
     - Applique le filtre
     - Multiplie par le gain correspondant
   - Somme les signaux filtrés de toutes les bandes

4. `generate_impulse_response(a0, a1, b1, b2, length=1000)`:
   - Génère la réponse impulsionnelle d'un filtre
   - Crée une impulsion et applique le filtre

### audio_utils.py

1. `read_wav(filename)`:
   - Lit un fichier WAV
   - Convertit en mono si le fichier est stéréo

2. `write_wav(filename, sample_rate, data)`:
   - Écrit les données audio dans un fichier WAV
   - Convertit les données en int16 et les limite entre -32768 et 32767

## Description des filtres

Chaque bande de fréquence utilise un filtre passe-bande avec les caractéristiques suivantes :

- Basse (20-200 Hz) : a0 = 0.2, a1 = -0.2, b1 = 1.7, b2 = -0.7
- Bas-médium (200-800 Hz) : a0 = 0.3, a1 = -0.3, b1 = 1.6, b2 = -0.6
- Médium (800-2500 Hz) : a0 = 0.4, a1 = -0.4, b1 = 1.5, b2 = -0.5
- Haut-médium (2500-8000 Hz) : a0 = 0.5, a1 = -0.5, b1 = 1.4, b2 = -0.4
- Aigu (8000-20000 Hz) : a0 = 0.6, a1 = -0.6, b1 = 1.3, b2 = -0.3

## Auteur

PINZANO Léo
