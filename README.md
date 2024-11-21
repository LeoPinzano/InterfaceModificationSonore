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

## Structure du projet

- `main.py` : Interface graphique et logique principale
- `signal_processing.py` : Fonctions de traitement du signal
- `audio_utils.py` : Utilitaires pour la manipulation des fichiers audio

## Algorithmes

### Égalisation

L'égaliseur utilise 5 filtres passe-bande du second ordre. Pour chaque bande de fréquence :

1. Calcul des coefficients du filtre
2. Application du filtre sur le signal audio
3. Ajustement du gain selon la valeur du slider
4. Sommation des signaux filtrés

## Description des filtres

Chaque bande de fréquence utilise un filtre passe-bande avec les caractéristiques suivantes :

- Basse (20-200 Hz) : a0 = 0.2, a1 = -0.2, b1 = 1.7, b2 = -0.7
- Bas-médium (200-800 Hz) : a0 = 0.3, a1 = -0.3, b1 = 1.6, b2 = -0.6
- Médium (800-2500 Hz) : a0 = 0.4, a1 = -0.4, b1 = 1.5, b2 = -0.5
- Haut-médium (2500-8000 Hz) : a0 = 0.5, a1 = -0.5, b1 = 1.4, b2 = -0.4
- Aigu (8000-20000 Hz) : a0 = 0.6, a1 = -0.6, b1 = 1.3, b2 = -0.3

## Réponses impulsionnelles

Les réponses impulsionnelles des filtres sont générées dans le fichier `signal_processing.py`. Voici un exemple de code pour les visualiser :

```python
import matplotlib.pyplot as plt
from signal_processing import generate_impulse_response, calculate_coefficients

for i in range(5):
    a0, a1, b1, b2 = calculate_coefficients(i)
    response = generate_impulse_response(a0, a1, b1, b2)
    plt.figure(figsize=(10, 5))
    plt.plot(response)
    plt.title(f"Réponse impulsionnelle - Bande {i+1}")
    plt.xlabel("Échantillons")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
```

## Auteur

PINZANO Léo
