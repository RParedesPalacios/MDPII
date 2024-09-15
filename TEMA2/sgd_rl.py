

import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento inventados
np.random.seed(100)  # Para reproducibilidad
x_train = np.linspace(0, 10, 50)  # 50 puntos de entrada entre 0 y 10
y_train = 3 * x_train + 5 + np.random.randn(50) * 2  # y = 3x + 5 + ruido

# Inicialización de parámetros
w = np.random.randn()
b = np.random.randn()

# Hiperparámetros
learning_rate = 0.001
epochs = 100  # Número de pasos de optimización

# Para almacenar la evolución de los parámetros
w_history = [w]
b_history = [b]

# Función de coste: error cuadrático medio
def compute_cost(x, y, w, b):
    m = len(x)
    y_pred = w * x + b
    cost = (1 / (2 * m)) * np.sum((y_pred - y) ** 2)
    return cost

# Gradiente de la función de coste con respecto a w y b
def compute_gradient(x, y, w, b):
    m = len(x)
    y_pred = w * x + b
    dw = (1 / m) * np.sum((y_pred - y) * x)  # Derivada parcial respecto a w
    db = (1 / m) * np.sum(y_pred - y)  # Derivada parcial respecto a b
    return dw, db

# Visualización del proceso de optimización
plt.ion()  # Modo interactivo para actualizar la gráfica en tiempo real

# Crear figura y subgráficas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Establecer límites fijos para los ejes
ax1.set_xlim(0, 10)
ax1.set_ylim(min(y_train) - 5, max(y_train) + 5)


ax2.set_xlim(-10, 10)
ax2.set_ylim(-10,10)

ax2.set_xlabel('w')
ax2.set_ylabel('b')


# Punto óptimo
optimal_w, optimal_b = 3, 5

for epoch in range(epochs):
    # Calcular gradiente
    dw, db = compute_gradient(x_train, y_train, w, b)
    
  

    # Guardar los parámetros actuales en la historia
    w_history.append(w)
    b_history.append(b)
    
    # Graficar datos y la recta de regresión actual
    ax1.cla()  # Limpiar la subgráfica izquierda
    ax1.scatter(x_train, y_train, color='blue', label='Datos de entrenamiento')
    y_pred = w * x_train + b
    ax1.plot(x_train, y_pred, color='red', label=f'Recta: y = {w:.2f}x + {b:.2f}')
    ax1.set_title(f'Iteración: {epoch}, Coste: {compute_cost(x_train, y_train, w, b):.4f}')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    ax1.set_xlim(0, 10)
    ax1.set_ylim(min(y_train) - 5, max(y_train) + 5)
    
    # Graficar la evolución de los parámetros en la subgráfica derecha
    ax2.cla()  # Limpiar la subgráfica derecha

    ax2.set_xlim(-10, 10)
    ax2.set_ylim(-10,10)
    ax2.plot(w_history, b_history, marker='o', color='green', linestyle='-')
    ax2.scatter(optimal_w, optimal_b, color='red', marker='*', s=100, label='Punto óptimo (w=3, b=5)')

    ax2.set_xlim(-10, 10)
    ax2.set_ylim(-10,10)
    ax2.set_title('Evolución de los parámetros')
    ax2.set_xlabel('w')
    ax2.set_ylabel('b')
    
    plt.pause(0.1)  # Breve pausa para actualizar la visualización
    print(f'Presiona una tecla para continuar con la iteración {epoch + 1}/{epochs}...')
    plt.waitforbuttonpress()  # Espera a que el usuario presione una tecla

    # Actualizar parámetros
    w -= learning_rate * dw
    b -= 10*learning_rate * db
    

plt.ioff()  # Desactivar el modo interactivo
plt.show()

print(f'Parámetros finales: w = {w:.2f}, b = {b:.2f}')
