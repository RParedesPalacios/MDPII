## Ejercicio

MLP con una capa oculta, la función de activación de la capa oculta es ReLU, la de la capa de salida es lineal. 

![MLP](assets/mlp.png)

La función de coste es la divergencia al cuadrado:

```math
J(\mathbf{W}) = \frac{1}{2} \| \hat{\mathbf{y}} - \mathbf{y} \|^{2}
```



 Se utilizan los siguientes valores:

### Valores:
- **Entrada**: $\mathbf{x} = [-1, 0, 2]$
- **Salida esperada**: $\mathbf{y} = [3]$
- **Pesos de la capa 1**:

```math
W^{~(1)}= \begin{pmatrix} 2 & 0 & 1 \\ 0 & -1 & 1 \end{pmatrix}
```

- **Pesos de la capa 2**:

```math
W^{~(2)} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}
```

### Funciones de activación:
- **ReLU para la capa oculta**:

```math
f(z) = \max(0, z)
```

- **Función lineal para la capa de salida** (sin función de activación, simplemente $f(z) = z$).

---

### Forward Propagation

#### Cálculo de las activaciones en la capa oculta:

```math
\mathbf{z}^{(1)} = W^{~(1)} \cdot \mathbf{x} = \begin{pmatrix} 2 & 0 & 1 \\ 0 & -1 & 1 \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 0 \\ 2 \end{pmatrix} = \begin{pmatrix} 0 \\ 2 \end{pmatrix}
```
Luego, aplicamos la función de activación ReLU:

```math
\mathbf{a}^{(1)} = \text{ReLU}(\mathbf{z}^{(1)}) = \begin{pmatrix} 0 \\ 2 \end{pmatrix}
```

#### Cálculo de la salida de la red (capa de salida):

```math
\mathbf{z}^{(2)} = W^{~(2)} \cdot \mathbf{a}^{(1)} = \begin{pmatrix} -1 & 1 \end{pmatrix} \cdot \begin{pmatrix} 0 \\ 2 \end{pmatrix} = (2)
```

Dado que la función de activación en la capa de salida es lineal, tenemos:

```math
\mathbf{a}^{(2)} = \mathbf{z}^{(2)} = (2)
```

#### Error:

```math
\text{Error} = \frac{1}{2} || \mathbf{a}^{(2)} - y ||^2 = \frac{1}{2} || 2 - 3 ||^2 = \frac{1}{2}
```

---

### Backward Propagation


Denominamos $\delta^{(L)}=\frac{\partial J}{\partial \mathbf{z}^{(L)}}$


#### Cálculo del gradiente en la capa de salida:

Recordemos la regla de la cadena:

```math
\delta^{(2)}=\frac{\partial J}{\partial \mathbf{z}^{2}}=\frac{\partial J}{\partial \mathbf{a}^{2}}\frac{\partial \mathbf{a}^{2}}{\partial \mathbf{z}^{2}}=\frac{\partial J}{\partial \hat{y}}\frac{\partial \hat{y}}{\partial \mathbf{z}^{2}}
```
Dada que la función de salida es lineal

```math
\frac{\partial \hat{y}}{\partial \mathbf{z}^{2}}=1
```

y

```math
\frac{\partial J}{\partial \hat{y}}=(\hat{y} - y)
```

nos queda:

```math
\delta^{(2)} = (\hat{y} - y)=(-1)
```

El gradiente de los pesos de la capa de salida $W^{~(2)}$ es:

```math
\frac{\partial J}{\partial W^{~(2)}}=\frac{\partial J}{\partial \mathbf{z}^{(2)}}\frac{\partial \mathbf{z}^{(2)}}{\partial W^{~(2)}}=\delta^{(2)}\cdot \mathbf{a}^{(1)}
```


```math
\text{gradiente de } W^{~(2)} = \delta^{(2)}\cdot \mathbf{a}^{(1)}= (-1)\cdot\begin{pmatrix} 0 \\ 2 \end{pmatrix} = \begin{pmatrix} 0 \\ -2 \end{pmatrix}
```

#### Cálculo del gradiente en la capa oculta:


```math
\delta^{(1)}=\frac{\partial J}{\partial \mathbf{z}^{1}}=\frac{\partial J}{\partial \mathbf{a}^{1}}\frac{\partial \mathbf{a}^{1}}{\partial \mathbf{z}^{1}}
```

por partes:

```math
\frac{\partial J}{\partial \mathbf{a}^{1}}=\frac{\partial J}{\partial \mathbf{z}^{2}}\frac{\partial \mathbf{z}^{2}}{\partial \mathbf{a}^{1}}=\delta^2\cdot W^{~(2)}
```

y
```math
\frac{\partial \mathbf{a}^{1}}{\partial \mathbf{z}^{1}}=f'(\mathbf{z}^{(1)})
```

por lo tanto:

```math
\delta^{(1)} = (\delta^{(2)}\cdot W^{~(2)}) \odot f'(\mathbf{z}^{(1)})
```

Así pues:

```math
 \delta^{(2)}\cdot W^{~(2)} = (-1) \cdot \begin{pmatrix} -1 \\ 1 \end{pmatrix}  = \begin{pmatrix} 1 \\ -1 \end{pmatrix}
```

Luego, multiplicamos por la derivada de ReLU (suponemos que la derivada en 0 es 0):

```math
f'(\mathbf{z}^{(1)}) = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
```

```math
\delta^{(1)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \odot \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix}
```

El gradiente de los pesos de la primera capa $W^{~(1)}$ es:

```math
\frac{\partial J}{\partial W^{~(1)}}=\frac{\partial J}{\partial \mathbf{z}^{(1)}}\frac{\partial \mathbf{z}^{(1)}}{\partial W^{~(1)}}=\delta^{(1)}\cdot \mathbf{x}
```

```math
\text{gradiente de } W^{~(1)} = \delta^{(1)} \cdot \mathbf{x} = \begin{pmatrix} 0 \\ -1 \end{pmatrix} \cdot \begin{pmatrix} -1 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & -2 \end{pmatrix}
```


