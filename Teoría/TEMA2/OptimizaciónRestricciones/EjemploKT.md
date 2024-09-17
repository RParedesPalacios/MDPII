## Problema de Optimización usando KT

Queremos minimizar la función:
```math
q(\theta) = 1 + (\theta - 2)^2,
```
sujeto a la restricción:

```math
    \theta\leq 3
```

o lo que es lo mismo:

```math
3 - \theta \geq 0
```

### Solución si Teorema KT

La solución sin el teoremas KKT desarrollada en clase nos lleva a un $\alpha=-1$ que viola la condición de que $\alpha\geq 0$.

El hecho de que el multiplicador $\alpha$ sea negativo implica que la restricción $3 - \theta \geq 0$ no está limitando el óptimo en este caso. 

**En términos prácticos**, significa que la solución óptima cae dentro de la región factible de la restricción sin tocar el límite. O sea, podriamos haber derivado $q(\theta)$ igualado a cero y resuelto analíticamente sin tener en cuenta la restricción. Esta solución sería:

```math
    \theta=2
```

Aún así nos podríamos haber evitado mucho desarrollo matemático empleando el Teorema KT:

### Paso 1: Formulación del Lagrangiano

La Lagrangiana para este problema, usando el multiplicador de Lagrange $\alpha$ asociado a la restricción, es:
```math
\mathcal{L}(\theta, \alpha) = 1 + (\theta - 2)^2 - \alpha (3 - \theta),
```
donde $\alpha \geq 0$.

### Paso 2: Derivar el Lagrangiano con respecto a $\theta$ e igualar a cero

Derivamos la Lagrangiana con respecto a $\theta$:
```math
\frac{\partial \mathcal{L}}{\partial \theta} = 2(\theta - 2) + \alpha.
```

Igualamos a cero para encontrar los puntos críticos:
```math
2(\theta - 2) + \alpha = 0.
```

Despejamos $\theta$ en términos de $\alpha$:
```math
2\theta - 4 + \alpha = 0,
```
```math
2\theta = 4 - \alpha,
```
```math
\theta = 2 - \frac{\alpha}{2}.
```

Denotemos esta solución como $\theta^*(\alpha) = 2 - \frac{\alpha}{2}$.

### Paso 3: Condición KT de complementariedad

Las condiciones KKT establecen que:
```math
\alpha^* (3 - \theta^*(\alpha^*)) = 0.
```

Sustituyendo $\theta^*(\alpha^*) = 2 - \frac{\alpha^*}{2}$ en la restricción:
```math
\alpha^* \left[ 3 - \left( 2 - \frac{\alpha^*}{2} \right) \right] = 0.
```

Simplificamos la expresión dentro del paréntesis:
```math
\alpha^* \left[ 1 + \frac{\alpha^*}{2} \right] = 0.
```

### Paso 4: Resolver las condiciones KT

Para que el producto $\alpha^* \left[ 1 + \frac{\alpha^*}{2} \right] = 0$, tenemos dos casos posibles:

1. $\alpha^* = 0$:
   - Si $\alpha^* = 0$, entonces:
     ```math
     \theta^* = 2 - \frac{0}{2} = 2.
     ```

2. $1 + \frac{\alpha^*}{2} = 0$:
   - Esto implica que:
     ```math
     \frac{\alpha^*}{2} = -1,
     ```
     ```math
     \alpha^* = -2.
     ```
   - **Sin embargo, esto viola la condición $\alpha \geq 0$**, lo que significa que este caso no es válido.

### Paso 5: Conclusión

La única solución válida es:
```math
\alpha^* = 0 \quad \text{y} \quad \theta^* = 2.
```

Verificamos la restricción:
```math
3 - \theta^* = 3 - 2 = 1 \geq 0,
```
lo que confirma que la solución cumple con la restricción.

