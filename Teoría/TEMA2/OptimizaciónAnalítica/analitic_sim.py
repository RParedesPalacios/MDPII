import numpy as np
import sympy as sp

# Datos de entrenamiento
n=50
np.random.seed(10)
x_train = np.linspace(0, 10, n).astype(np.float32)
y_train = (3 * x_train + 5 + np.random.randn(n) * 2).astype(np.float32)


# Definir variables simbólicas
w, b = sp.symbols('w b', real=True)
x_values = x_train.tolist()  # Valores de x
y_values = y_train.tolist()  # Valores de y

# Definir la función de coste (MSE) como una suma
mse = sp.Rational(1, n) * sum((y - (w * x + b))**2 for x, y in zip(x_values, y_values))

# Derivar la función de coste con respecto a w y b
d_mse_w = sp.diff(mse, w)
d_mse_b = sp.diff(mse, b)

# Resolver las derivadas igualadas a cero para encontrar los valores óptimos de w y b
solutions = sp.solve([d_mse_w, d_mse_b], (w, b))

# Mostrar las soluciones
print("Solución analítica encontrada:")
print(f"w = {solutions[w]}")
print(f"b = {solutions[b]}")