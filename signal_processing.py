## @file signal_processing.py
# @brief Fonctions de traitement du signal pour l'égaliseur audio
# @details Ce fichier contient les fonctions nécessaires pour le traitement du signal
# audio, incluant le calcul des coefficients de filtre, le filtrage par bande,
# l'égalisation et la génération de réponse impulsionnelle.

import numpy as np

## @brief Calcule les coefficients du filtre pour une bande donnée
# @param band_index Index de la bande de fréquence (0-4)
# @return Tuple contenant les coefficients (a0, a1, b1, b2)
def calculate_coefficients(band_index):
    # À implémenter : calcul des coefficients pour chaque bande
    # Ceci est un exemple simplifié, vous devrez ajuster ces valeurs
    coefficients = [
        (0.2, -0.2, 1.7, -0.7),
        (0.3, -0.3, 1.6, -0.6),
        (0.4, -0.4, 1.5, -0.5),
        (0.5, -0.5, 1.4, -0.4),
        (0.6, -0.6, 1.3, -0.3)
    ]
    return coefficients[band_index]

## @brief Applique un filtre à une bande de fréquence spécifique
# @param data Données audio à filtrer
# @param a0 Coefficient a0 du filtre
# @param a1 Coefficient a1 du filtre
# @param b1 Coefficient b1 du filtre
# @param b2 Coefficient b2 du filtre
# @return Données audio filtrées
def filter_band(data, a0, a1, b1, b2):
    filtered_data = np.zeros_like(data)
    filtered_data[0] = a0 * data[0]
    filtered_data[1] = a0 * data[1] + a1 * data[0] + b1 * filtered_data[0]
    filtered_data[2] = a0 * data[2] + a1 * data[1] + b1 * filtered_data[1] + b2 * filtered_data[0]
    
    for i in range(3, len(data)):
        filtered_data[i] = a0 * data[i] + a1 * data[i-1] + b1 * filtered_data[i-1] + b2 * filtered_data[i-2]
    
    return filtered_data

## @brief Applique l'égalisation aux données audio
# @param data Données audio à égaliser
# @param gains Liste des gains pour chaque bande de fréquence
# @return Données audio égalisées
def equalizer(data, gains):
    result = np.zeros_like(data, dtype=np.float64)
    for i, gain in enumerate(gains):
        a0, a1, b1, b2 = calculate_coefficients(i)
        filtered = filter_band(data.astype(np.float64), a0, a1, b1, b2)
        result += filtered * gain
    return result.astype(np.int16)

## @brief Génère la réponse impulsionnelle pour un filtre donné
# @param a0 Coefficient a0 du filtre
# @param a1 Coefficient a1 du filtre
# @param b1 Coefficient b1 du filtre
# @param b2 Coefficient b2 du filtre
# @param length Longueur de la réponse impulsionnelle (défaut: 1000)
# @return Réponse impulsionnelle du filtre
def generate_impulse_response(a0, a1, b1, b2, length=1000):
    impulse = np.zeros(length)
    impulse[0] = 1
    return filter_band(impulse, a0, a1, b1, b2)