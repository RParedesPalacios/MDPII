
# Softmax y cálculo para evitar overflow

## 1. Definición de Softmax:
La función **Softmax** toma un vector de entradas (logits) $\mathbf{z} = [z_1, z_2, \dots, z_n]$ y lo transforma en un vector de probabilidades $\mathbf{a} = [a_1, a_2, \dots, a_n]$. Esto se realiza mediante la siguiente fórmula:

```math
a_i = \frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}} \quad \text{para cada componente} \quad i = 1, 2, \dots, n
```

Este proceso asegura que la suma de todas las probabilidades en el vector $\mathbf{a}$ sea 1, lo que convierte a **Softmax** en una función muy útil para problemas de clasificación en redes neuronales, entre otros.

## 2. Problemas Numéricos:
Un problema común al calcular la función Softmax es que los valores $z_i$ pueden ser muy grandes. Si los valores $z_i$ son muy grandes, $e^{z_i}$ puede dar lugar a un desbordamiento (*overflow*).

Para evitar estos problemas numéricos, podemos restar un valor constante a todos los componentes del vector $\mathbf{z}$ sin cambiar el resultado de la función **Softmax**. Esto es posible porque la función **Softmax** es invariante ante traslaciones de los logits por una constante.

## 3. Restar el Máximo para Estabilidad Numérica:
El valor constante que normalmente se resta es el máximo de los componentes de $\mathbf{z}$. Vamos a ver por qué esto es útil.

Dado un vector de logits $\mathbf{z} = [z_1, z_2, \dots, z_n]$, supongamos que restamos el valor máximo de $z$, denotado como $z_{\text{max}}$:

```math
z_{\text{max}} = \max_{i}(z_i)
```

Definimos una nueva versión de $z$, donde cada componente es el valor original menos $z_{\text{max}}$:

```math
\tilde{z_i} = z_i - z_{\text{max}} \quad \text{para cada} \quad i = 1, 2, \dots, n
```

Ahora, si aplicamos **Softmax** al nuevo vector $\tilde{\mathbf{z}}$, obtenemos:

```math
a_i = \frac{e^{\tilde{z_i}}}{\sum_{j=1}^{n} e^{\tilde{z_j}}} = \frac{e^{z_i - z_{\text{max}}}}{\sum_{j=1}^{n} e^{z_j - z_{\text{max}}}}
```

## 4. Equivalencia al Original:
Veamos cómo esta transformación no cambia el resultado final de la función **Softmax**. Podemos factorizar la constante $e^{-z_{\text{max}}}$ del numerador y denominador:

```math
a_i = \frac{e^{z_i} e^{-z_{\text{max}}}}{\sum_{j=1}^{n} e^{z_j} e^{-z_{\text{max}}}} = \frac{e^{z_i}}{e^{z_{\text{max}}} \sum_{j=1}^{n} e^{z_j} e^{-z_{\text{max}}}} = \frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}}
```

Esto muestra que el resultado final es equivalente al original, ya que la constante $e^{-z_{\text{max}}}$ se cancela en el numerador y el denominador.

