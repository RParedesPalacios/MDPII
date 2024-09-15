import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento inventados
np.random.seed(10)  # Para reproducibilidad
x_train = np.linspace(0, 10, 50)  # 50 puntos de entrada entre 0 y 10
y_train = 3 * x_train + 5 + np.random.randn(50) * 2  # y = 3x + 5 + ruido

# Inicialización de parámetros
w = np.random.randn()
b = np.random.randn()

w=-3
b=-5

# Hiperparámetros
learning_rate = 0.02
epochs = 1000  # Número de pasos de optimización

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

# Generar cuadrícula para la función de coste
w_range = np.linspace(-10, 10, 100)
b_range = np.linspace(-10, 10, 100)
W, B = np.meshgrid(w_range, b_range)
Z = np.zeros_like(W)

# Calcular el coste en cada punto de la cuadrícula
for i in range(len(w_range)):
    for j in range(len(b_range)):
        Z[j, i] = compute_cost(x_train, y_train, W[j, i], B[j, i])

# Visualización del proceso de optimización
plt.ion()  # Modo interactivo para actualizar la gráfica en tiempo real

# Crear figura y subgráficas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Establecer límites fijos para los ejes
ax1.set_xlim(0, 10)
ax1.set_ylim(min(y_train) - 5, max(y_train) + 5)
ax2.set_xlabel('w')
ax2.set_ylabel('b')

# Punto óptimo
optimal_w, optimal_b = 3, 5
plt.waitforbuttonpress()  

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
    ax1.set_xlabel('x', fontsize=24)
    ax1.set_ylabel('y', fontsize=24)
    ax1.legend(fontsize=24)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(min(y_train) - 5, max(y_train) + 5)
    
    # Graficar la función de coste en la subgráfica derecha
    ax2.cla()  # Limpiar la subgráfica derecha
    contour = ax2.contourf(W, B, Z, levels=150, cmap='viridis', alpha=0.7)
    ax2.plot(w_history, b_history, marker='o', color='green', linestyle='-', label='Trayectoria (w, b)')
    
    # Marcar el punto óptimo
    ax2.scatter(optimal_w, optimal_b, color='red', marker='*', s=100, label='Punto óptimo (w=3, b=5)')
    
    ax2.set_title('Evolución de los parámetros')
    ax2.set_xlabel('w', fontsize=24)
    ax2.set_ylabel('b', fontsize=24)
    ax2.legend(fontsize=24)
    
    plt.pause(0.1)  # Breve pausa para actualizar la visualización
    print(f'Presiona una tecla para continuar con la iteración {epoch + 1}/{epochs}...')
    #plt.waitforbuttonpress()  # Espera a que el usuario presione una tecla


    # Actualizar parámetros
    w -= learning_rate * dw
    b -= learning_rate * db



plt.ioff()  # Desactivar el modo interactivo
plt.show()

print(f'Parámetros finales: w = {w:.2f}, b = {b:.2f}')
