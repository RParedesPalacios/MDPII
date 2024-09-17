
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento
n=50
np.random.seed(10)
x_train = np.linspace(0, 10, n).astype(np.float32)
y_train = (3 * x_train + 5 + np.random.randn(n) * 2).astype(np.float32)

# Cálculo del valor óptimo analítico
x_mean = np.mean(x_train).astype(np.float32)
y_mean = np.mean(y_train).astype(np.float32)

# Derivar con respecto a w e igualar a cero para encontrar el valor óptimo de w
w_optimal = np.sum((x_train - x_mean) * (y_train - y_mean)) / np.sum((x_train - x_mean) ** 2)

# Derivar con respecto a b e igualar a cero para encontrar el valor óptimo de b
b_optimal = y_mean - w_optimal * x_mean

# Mostrar las soluciones
print("Solución analítica encontrada:")
print(f"w = ",w_optimal)
print(f"b = ",b_optimal)