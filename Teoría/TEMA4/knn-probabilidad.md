
# Relación entre k-Vecinos más Cercanos y la Estimación de Probabilidad a Posteriori 

El método de los k-vecinos más cercanos (k-NN) tiene una relación muy intuitiva con la estimación de la probabilidad a posteriori $p(c | x)$, y esto puede explicarse a través de conceptos geométricos como el volumen de una hiperesfera, la densidad de probabilidad y la forma en que se distribuyen los puntos de datos.

## 1. k-NN como estimador de $p(c | x)$
El algoritmo k-NN se basa en la idea de que la probabilidad condicional $p(c | x)$ puede aproximarse observando la cantidad de vecinos más cercanos de una clase específica que rodean a un punto de interés $x$. En concreto:

- $K$ es el número total de vecinos más cercanos que estás considerando (por ejemplo, los 10 vecinos más cercanos).
- $K_c$ es el número de esos $K$ vecinos que pertenecen a la clase $c$.

Entonces, la estimación de la probabilidad a posteriori de la clase $c$ dada $x$ es simplemente:

```math
p(c | x) \approx \frac{K_c}{K}
```

Esta aproximación asume que los puntos cercanos a $x$ pueden darnos información sobre las probabilidades de las clases.

## 2. Volumen de la hiperesfera
Para comprender la relación con la densidad de probabilidad, imagina que alrededor de $x$ construyes una *hiperesfera* que contiene exactamente $K$ vecinos más cercanos. El *volumen* de esta hiperesfera está relacionado con la distancia a la que necesitas extenderte desde $x$ para encontrar esos $K$ vecinos.

Denotemos por $V_K(x)$ al volumen de la hiperesfera que contiene exactamente a los $K$ vecinos más cercanos a $x$. Este volumen depende de la densidad local de los datos: si la densidad es alta, los $K$ vecinos estarán muy cerca de $x$, lo que significa que el volumen será pequeño; si la densidad es baja, el volumen será mayor.

## 3. Densidad de probabilidad condicional $p(x | c)$
La relación entre el volumen de la hiperesfera y la densidad de probabilidad $p(x | c)$ viene dada por la idea de que, en un entorno local alrededor de $x$, la densidad de puntos de la clase $c$ puede aproximarse como:

```math
p(x | c) \approx \frac{K_c}{N_c V_K(x)}
```

Donde:
- $K_c$ es el número de vecinos que pertenecen a la clase $c$.
- $N_c$ es el número total de puntos de la clase $c$ en el conjunto de datos.
- $V_K(x)$ es el volumen de la hiperesfera que contiene los $K$ vecinos más cercanos.

Esta expresión dice que la densidad condicional $p(x | c)$ es proporcional al número de vecinos de la clase $c$ dentro de un volumen dado (la hiperesfera), ajustado por el total de puntos de esa clase.

## 4. Relación entre la densidad de probabilidad y $p(c | x)$
Finalmente, para estimar la probabilidad a posteriori $p(c | x)$, podemos usar el teorema de Bayes:

```math
p(c | x) = \frac{p(x | c) p(c)}{p(x)}
```

Donde:
- $p(x | c)$ es la densidad de los puntos de la clase $c$ cerca de $x$.
- $p(c)$ es la probabilidad a priori de la clase $c$ (proporcional a $rac{N_c}{N}$, donde $N$ es el número total de puntos).
- $p(x)$ es la densidad total de puntos en $x$, sumando todas las clases.

Cuando usas k-NN, la estimación de $p(c | x)$ se aproxima dividiendo el número de vecinos de la clase $c$ por el total de vecinos $K$, lo cual está alineado con esta idea de Bayes, ya que:

```math
p(c | x) \approx \frac{K_c}{K}
```

