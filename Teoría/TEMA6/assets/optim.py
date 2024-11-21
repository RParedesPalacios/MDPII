
################## Resolver optimización
 
from scipy.optimize import minimize
import numpy as np

# Datos y etiquetas

x = np.array([[1, 1], [0, 0], [0, 1], [1, 0]])
labels = np.array([1, 1, -1, -1])
C=3 # Parámetro de regularización

# Definición del kernel polinómico

def polynomial_kernel(x, y):
    return (np.dot(x, y) + 1) ** 2



# Construcción de la matriz kernel
kernel_matrix = np.zeros((4, 4))

for i in range(4):
    for j in range(4):
        kernel_matrix[i, j] = polynomial_kernel(x[i], x[j])



# Definir de nuevo las variables necesarias
n_samples = len(labels)  # Número de muestras

# Definir la función objetivo para la optimización dual de SVM
def objective(alphas):
    return 0.5 * np.sum([alphas[i] * alphas[j] * labels[i] * labels[j] * kernel_matrix[i, j] for i in range(n_samples) for j in range(n_samples)]) - np.sum(alphas)

# Restricción: \sum \alpha_i y_i = 0
def constraint_eq(alphas):
    return np.dot(alphas, labels)

# Restricción: \alpha_i >= 0
bounds = [(0, None) for _ in range(n_samples)]

# Punto inicial para la optimización
initial_alphas = np.zeros(n_samples)

# Resolver el problema de optimización
result = minimize(
    fun=objective,
    x0=initial_alphas,
    bounds=bounds,
    constraints={'type': 'eq', 'fun': constraint_eq},
    method='SLSQP'
)

# Extraer los valores de \alpha
optimal_alphas = result.x

print(optimal_alphas)




############## OBTENER LAS FRONTERAS y PLOTEAR

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# Identificar las muestras de soporte: \alpha_i > 1e-5
support_vectors_indices = np.where(optimal_alphas > 1e-5)[0]
support_vectors = x[support_vectors_indices]
support_vector_labels = labels[support_vectors_indices]
support_vector_alphas = optimal_alphas[support_vectors_indices]

# Calcular el sesgo (bias): b = y_i - sum(alpha_j * y_j * K(x_j, x_i))
idx=1 # por ejemplo con x_1 
bias = labels[idx] - sum(optimal_alphas[j] * labels[j] * polynomial_kernel(x[j], x[idx]) for j in range(n_samples))
print(bias)

# Recalcular f(x) incluyendo el sesgo
def decision_function(sample):
    decision_value = 0
    for i in range(n_samples):
        decision_value += optimal_alphas[i] * labels[i] * polynomial_kernel(x[i], sample)
    return decision_value + bias



# Generar una cuadrícula para visualizar las fronteras de decisión
x_min, x_max = -1, 3
y_min, y_max = -1, 3
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))



# Calcular la función de decisión para cada punto en la cuadrícula
grid_points = np.c_[xx.ravel(), yy.ravel()]
decision_values = [decision_function(point) for point in grid_points]
decision_values = np.array(decision_values).reshape(xx.shape)

# Revisar nuevamente las fronteras de decisión
decision_values_corrected = [decision_function(point) for point in grid_points]
decision_values_corrected = np.array(decision_values_corrected).reshape(xx.shape)

# Dibujar nuevamente las fronteras de decisión
plt.figure(figsize=(8, 8))
plt.contourf(xx, yy, decision_values_corrected, levels=0, cmap=ListedColormap(['#AAAAFF','#FFAAAA']), alpha=0.8)
plt.contour(xx, yy, decision_values_corrected, levels=[-1, 0, 1], colors=['blue', 'black', 'red'], linewidths=2, linestyles=['--', '-', '--'])

# Dibujar los puntos de entrenamiento
for i, sample in enumerate(x):
    plt.scatter(sample[0], sample[1], c='red' if labels[i] == 1 else 'blue', s=100, edgecolors='k')


# Configurar la gráfica
plt.title("Fronteras de Decisión y Márgenes con Kernel Polinómico")
plt.xlabel("x1")
plt.ylabel("x2")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.grid(True)
plt.show()


