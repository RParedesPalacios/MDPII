
## Factor de aprendizaje máximo en un punto

### Ejemplo para la función de Rosenbrock:

```math
f(\theta_1, \theta_2) = 10(\theta_2 - \theta_1^2)^2 + (1 - \theta_1)^2,
```

vamos a calcular la matriz Hessiana $H$ y evaluar sus valores propios.

La matriz Hessiana $H$ se compone de las segundas derivadas parciales de la función $f$. Vamos a hacerlo paso por paso.

### 1. Derivadas parciales de $f$:

Sea:

```math
f(\theta_1, \theta_2) = 10(\theta_2 - \theta_1^2)^2 + (1 - \theta_1)^2.
```

1. **Derivada parcial con respecto a $\theta_1$:**

```math
\frac{\partial f}{\partial \theta_1} = 20(\theta_2 - \theta_1^2)(-2\theta_1) - 2(1 - \theta_1).
```

Simplificando:

```math
\frac{\partial f}{\partial \theta_1} = -40\theta_1(\theta_2 - \theta_1^2) + 2(\theta_1 - 1).
```

2. **Derivada parcial con respecto a $\theta_2$:**

```math
\frac{\partial f}{\partial \theta_2} = 20(\theta_2 - \theta_1^2).
```

### 2. Segundas derivadas parciales (componentes de la Hessiana):

1. **Segunda derivada con respecto a $\theta_1$:**

```math
\frac{\partial^2 f}{\partial \theta_1^2} = -40(\theta_2 - \theta_1^2) - 40\theta_1(-2\theta_1) + 2.
```

Simplificando:

```math
\frac{\partial^2 f}{\partial \theta_1^2} = 120\theta_1^2 - 40\theta_2 + 2.
```

2. **Derivada cruzada:**

```math
\frac{\partial^2 f}{\partial \theta_1 \partial \theta_2} = \frac{\partial}{\partial \theta_2} \left[ -40\theta_1(\theta_2 - \theta_1^2) + 2(\theta_1 - 1) \right] = -40\theta_1.
```

3. **Segunda derivada con respecto a $\theta_2$:**

```math
\frac{\partial^2 f}{\partial \theta_2^2} = 20.
```

### 3. Construir la matriz Hessiana:

La Hessiana $H$ es una matriz simétrica:

```math
H = \begin{bmatrix} \frac{\partial^2 f}{\partial \theta_1^2} & \frac{\partial^2 f}{\partial \theta_1 \partial \theta_2} \\ \frac{\partial^2 f}{\partial \theta_2 \partial \theta_1} & \frac{\partial^2 f}{\partial \theta_2^2} \end{bmatrix} = \begin{bmatrix} 120\theta_1^2 - 40\theta_2 + 2 & -40\theta_1 \\ -40\theta_1 & 20 \end{bmatrix}.
```

### 4. Valores propios de la Hessiana

Ahora vamos a calcular los valores propios de la matriz Hessiana para una evaluación numérica específica.

#### Aplicación en el punto $(0, 0)$

En el punto $(0, 0)$, los componentes de la Hessiana se calculan como:

- $H_{11} = 120 \times 0^2 - 40 \times 0 + 2 = 2$,
- $H_{12} = -40 \times 0 = 0$,
- $H_{22} = 20$.

Por lo tanto, la matriz Hessiana en $(0, 0)$ es:

```math
H = \begin{bmatrix} 2 & 0 \\ 0 & 20 \end{bmatrix}.
```

Los valores propios de esta matriz son $2$ y $20$. 

### Condición para la convergencia

La condición $\rho < \frac{2}{\lambda_{\max}}$ es una regla que garantiza la convergencia de desecenso por gradiente, donde $\lambda_{\max}$ es el valor propio máximo de la matriz Hessiana. 

En este caso, $\lambda_{\max} = 20$. Por lo tanto, para garantizar la convergencia del método de gradiente descendente, el paso $\rho$ debe satisfacer:

```math
\rho < \frac{2}{\lambda_{\max}} = \frac{2}{20} = 0.1.
```

