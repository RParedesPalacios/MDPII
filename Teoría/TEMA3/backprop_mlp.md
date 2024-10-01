# BACKPROPAGATION MLP

Empleamos notación vectorial para compactar las expresiones.


### Algoritmo Backpropagation para Redes Neuronales Multicapa

El algoritmo de **backpropagation** es esencial para entrenar redes neuronales multicapa, como el perceptrón multicapa (MLP), con el fin de ajustar los pesos de la red para minimizar una función de coste. En este desarrollo empleamos notación matricial/vectorial, lo que permite expresar las fórmulas de manera más compacta y eficiente.

### 1. Estructura de un Perceptrón Multicapa (MLP)

Un MLP consta de varias capas:
1. **Capa de entrada:** donde los valores de entrada $\mathbf{x} \in \mathbb{R}^n$ se propagan hacia adelante.
2. **Capas ocultas:** donde cada neurona está conectada a las neuronas de la capa anterior.
3. **Capa de salida:** que genera las predicciones.

La propagación hacia adelante implica calcular las salidas de cada capa aplicando una función de activación $f(x)$ a la combinación lineal de las salidas de la capa anterior.

### 2. Propagación hacia adelante (Forward Propagation)

Para la capa $l$, la salida de las neuronas está dada por:

```math
\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)}
```
```math
\mathbf{a}^{(l)} = f(\mathbf{z}^{(l)})
```

Donde:
- $\mathbf{a}^{(l-1)}$ es el vector de activaciones de la capa anterior.
- $\mathbf{W}^{(l)}$ es la matriz de pesos de la capa $l$.
- $f(x)$ es la función de activación aplicada elemento a elemento.

La salida final de la red es:

```math
\hat{\mathbf{y}} = \mathbf{a}^{(L)}
```

### 3. Función de coste

Se minimiza una función de coste $J$, que mide el error entre las predicciones $\hat{\mathbf{y}}$ y las verdaderas etiquetas $\mathbf{y}$. Una función de coste común es el error cuadrático medio:

```math
J(\mathbf{W}) = \frac{1}{2} \| \hat{\mathbf{y}} - \mathbf{y} \|^2
```

Para problemas de clasificación, también es común usar la **entropía cruzada**:

```math
J(\mathbf{W}) = - \sum_{i} y_i \log(\hat{y}_i)
```

### 4. Propagación hacia atrás (Backpropagation)

El objetivo de backpropagation es calcular los gradientes de $J$ con respecto a los pesos $\mathbf{W}^{(l)}$ de cada capa para ajustar estos parámetros.

#### 4.1. Derivadas parciales en la capa de salida

Para la capa de salida $L$, la derivada del coste con respecto a las activaciones y las entradas es:

```math
\delta^{(L)} = \frac{\partial J}{\partial \mathbf{z}^{(L)}} = (\hat{\mathbf{y}} - \mathbf{y}) \odot f'(\mathbf{z}^{(L)})
```

Donde:
- $f'(\mathbf{z}^{(L)})$ es la derivada de la función de activación.
- La operación $\odot$ es el producto elemento a elemento, recordemos que los operandos son vectores

Los gradientes de los pesos $\mathbf{W}^{(L)}$ son:

```math
\frac{\partial J}{\partial \mathbf{W}^{(L)}} = \delta^{(L)} (\mathbf{a}^{(L-1)})^T
```

#### 4.2. Derivadas parciales en capas ocultas

El error en una capa $l$ se propaga hacia atrás usando el error de la capa siguiente $\delta^{(l+1)}$:

```math
\delta^{(l)} = (\mathbf{W}^{(l+1)})^T \delta^{(l+1)} \odot f'(\mathbf{z}^{(l)})
```

Los gradientes de los pesos $\mathbf{W}^{(l)}$ son:

```math
\frac{\partial J}{\partial \mathbf{W}^{(l)}} = \delta^{(l)} (\mathbf{a}^{(l-1)})^T
```

### 5. Actualización de los pesos

Los pesos se actualizan usando gradiente descendente con un tamaño de paso $\eta$:

```math
\mathbf{W}^{(l)} := \mathbf{W}^{(l)} - \eta \frac{\partial J}{\partial \mathbf{W}^{(l)}}
```

### 6. Resumen del algoritmo de backpropagation

1. **Inicialización:** Se inicializan los pesos $\mathbf{W}^{(l)}$ de forma aleatoria.
2. **Propagación hacia adelante:** Se calculan $\mathbf{z}^{(l)}$ y $\mathbf{a}^{(l)}$ hasta obtener $\hat{\mathbf{y}}$.
3. **Cálculo del coste:** Se evalúa la función de coste $J(\hat{\mathbf{y}}, \mathbf{y})$.
4. **Propagación hacia atrás:** Se calculan $\delta^{(L)}$ y los errores en cada capa.
5. **Actualización de los pesos:** Se ajustan los pesos con gradiente descendente.
6. **Repetición:** Se itera hasta minimizar el error o alcanzar un criterio de parada.

### 7. Funciones de activación comunes

- **ReLU (Rectified Linear Unit):**
  ```math
  f(x) = \max(0, x), \quad f'(x) =
  \begin{cases} 
  1 & \text{si } x > 0 \\ 
  0 & \text{si } x \leq 0 
  \end{cases}
  ```

- **Sigmoide:**
  ```math
  f(x) = \frac{1}{1 + e^{-x}}, \quad f'(x) = f(x)(1 - f(x))
  ```
