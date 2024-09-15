
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento inventados
np.random.seed(100)  # Para reproducibilidad
x_train = np.linspace(0, 10, 50)  # 50 puntos de entrada entre 0 y 10
y_train = 3 * x_train + 5 + np.random.randn(50) * 2  # y = 3x + 5 + ruido


# Cálculo del valor óptimo analítico
x_mean = np.mean(x_train)
y_mean = np.mean(y_train)

# Cálculo de la pendiente (w)
w_optimal = np.sum((x_train - x_mean) * (y_train - y_mean)) / np.sum((x_train - x_mean) ** 2)

# Cálculo del intercepto (b)
b_optimal = y_mean - w_optimal * x_mean

print(f'Solución analítica: w = {w_optimal:.2f}, b = {b_optimal:.2f}')
