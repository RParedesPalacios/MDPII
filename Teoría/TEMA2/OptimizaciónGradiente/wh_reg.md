
## Widrow-Hoff regularizado

Añadimos factor de regularización:

```math
q_S(\theta) = \frac{1}{2} \sum_{n=1}^{N} \left( \theta^t x_n - y_n \right)^2 + \frac{\lambda}{2} \theta^t \theta,
```

donde $\lambda > 0$ es el parámetro de regularización que controla la influencia del término regularizador.

### Paso 1: Derivar la función de costo con respecto a $\theta$

El objetivo es obtener la actualización de los pesos aplicando descenso por gradiente. Para ello, derivamos la función $q_S(\theta)$ con respecto a $\theta$:

**Primer término:** Derivada de la suma de errores cuadrados:

```math
\frac{\partial}{\partial \theta} \left[ \frac{1}{2} \sum_{n=1}^{N} \left( \theta^t x_n - y_n \right)^2 \right].
```

Para cada término individual, la derivada es:

```math
\frac{\partial}{\partial \theta} \left[ \frac{1}{2} \left( \theta^t x_n - y_n \right)^2 \right] = \left( \theta^t x_n - y_n \right) x_n.
```

Entonces, la derivada total del primer término es:

```math
\sum_{n=1}^{N} \left( \theta^t x_n - y_n \right) x_n.
```

**Segundo término (regularización):** La derivada del término de regularización es ahora:

```math
\frac{\partial}{\partial \theta} \left[ \frac{\lambda}{2} \theta^t \theta \right] = \lambda \theta.
```

**Gradiente total:**

Sumando ambos términos, el gradiente de la función de costo $q_S(\theta)$ es:

```math
\nabla q_S(\theta) = \sum_{n=1}^{N} \left( \theta^t x_n - y_n \right) x_n + \lambda \theta.
```

### Paso 3: Actualización del algoritmo de Widrow-Hoff (descenso por gradiente)

Para obtener la regla de actualización de los pesos, usamos el descenso por gradiente:

```math
\theta \leftarrow \theta - \rho \nabla q_S(\theta),
```

donde $\rho$ es la tasa de aprendizaje. Sustituyendo el gradiente, obtenemos:

```math
\theta \leftarrow \theta - \rho \left( \sum_{n=1}^{N} \left( \theta^t x_n - y_n \right) x_n + \lambda \theta \right).
```

### Extra, Versión muestra a muestra (estocástica) con regularización

En la versión muestra a muestra (o estocástica), la actualización se realiza para cada muestra individualmente en lugar de sumar sobre todas las muestras. Para una muestra $n$:

```math
\theta \leftarrow \theta - \rho \left[ \left( \theta^t x_n - y_n \right) x_n + \lambda \theta \right].
```
