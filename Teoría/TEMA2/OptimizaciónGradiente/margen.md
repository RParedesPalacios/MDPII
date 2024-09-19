## Margen, Regularización y Generalización

En el contexto de un clasificador lineal para la clasificación binaria, de la forma:

```math
\text{sign}(w^T x ),
```

el margen está relacionado directamente con el módulo de los parámetros $w$. A continuación, explicaremos esta relación y derivaremos la expresión matemática correspondiente.

### Definición del margen en un clasificador lineal

Dado un conjunto de datos de entrenamiento $\{(x_i, y_i)\}_{i=1}^{N}$, donde $x_i$ es una muestra y $y_i \in$```{-1, 1}``` es su etiqueta, el margen de clasificación es la distancia mínima entre las muestras y la frontera de decisión del clasificador, definida por $w^T x = 0$.

Para una muestra $(x_i, y_i)$ correctamente clasificada, el valor de la función de decisión debe cumplir:

```math
y_i (w^T x_i) > 0.
```
Teniendo en cuenta que la distancia de un punto a un hiperplano definido por la ecuación característica $w^T x = 0$ es:

```math
Distancia = \frac{|w^T x_i|}{\|w\|}.
```

El **margen geométrico** para una muestra bien clasificada es:

```math
\gamma_i = \frac{y_i (w^T x_i)}{\|w\|}.
```

El margen geométrico del clasificador, $\gamma$, es la distancia mínima entre cualquier muestra y la frontera de decisión:

```math
\gamma = \min_{i=1, \dots, N} \frac{y_i (w^T x_i)}{\|w\|}.
```

### 2. Maximización del margen y relación con el módulo de $w$

En general, el módulo de los parámetros está inversamente relacionado con el margen en problemas lineales. Un módulo grande indica que la frontera de decisión está muy influenciada por pequeñas variaciones en los datos de entrada, resultando en un margen más pequeño. Al contrario, un módulo pequeño indica que la frontera es más estable y menos sensible a perturbaciones en los datos, por lo tanto **generaliza** mejor, lo que corresponde a un margen más grande.

Se busca pues maximizar el margen $\gamma$ o, de forma equivalente, minimizar $\|w\|$ como se puede conseguir con técnicas de regularización.

