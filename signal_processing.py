import numpy as np

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

def filter_band(data, a0, a1, b1, b2):
    filtered_data = np.zeros_like(data)
    filtered_data[0] = a0 * data[0]
    filtered_data[1] = a0 * data[1] + a1 * data[0] + b1 * filtered_data[0]
    filtered_data[2] = a0 * data[2] + a1 * data[1] + b1 * filtered_data[1] + b2 * filtered_data[0]
    
    for i in range(3, len(data)):
        filtered_data[i] = a0 * data[i] + a1 * data[i-1] + b1 * filtered_data[i-1] + b2 * filtered_data[i-2]
    
    return filtered_data

def equalizer(data, gains):
    result = np.zeros_like(data)
    for i, gain in enumerate(gains):
        a0, a1, b1, b2 = calculate_coefficients(i)
        filtered = filter_band(data, a0, a1, b1, b2)
        result += filtered * gain
    return result

def generate_impulse_response(a0, a1, b1, b2, length=1000):
    impulse = np.zeros(length)
    impulse[0] = 1
    return filter_band(impulse, a0, a1, b1, b2)