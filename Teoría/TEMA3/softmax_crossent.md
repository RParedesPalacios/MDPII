# Derivación de Gradientes en un Perceptrón Multicapa

## Notación Compacta
- **Entrada**: $\mathbf{x} \in \mathbb{R}^d$.
- **Capa oculta**: $\mathbf{\mathbf{z_1}} = W_1 \mathbf{x}$, donde $W_1 \in \mathbb{R}^{h \times d}$.
- **Activación**: $\mathbf{\mathbf{a_1}} = \text{ReLU}(\mathbf{z_1}) = \max(0, \mathbf{\mathbf{z_1}})$.
- **Capa de salida**: $\mathbf{\mathbf{z_2}} = W_2 \mathbf{\mathbf{a_1}}$, donde $W_2 \in \mathbb{R}^{k \times h}$.
- **Softmax**: $y_{\text{pred}} = \text{softmax}(\mathbf{z_2})$, donde:

```math
y_{\text{pred}, i} = \frac{e^{z_{2,i}}}{\sum_{j=1}^k e^{z_{2,j}}}.
```

- **Cross-entropía**:

```math
L = -\sum_{i=1}^k y_i \log(y_{\text{pred}, i}),
```
con $y$ como vector one-hot del label.

---

## 1. Propagación hacia Adelante
1. **Capa oculta**:

```math
   \mathbf{z_1} = W_1 x, \quad \mathbf{a_1} = \text{ReLU}(\mathbf{z_1}).
```

2. **Capa de salida**:

```math
   \mathbf{z_2} = W_2 \mathbf{a_1}, \quad y_{\text{pred}} = \text{softmax}(\mathbf{z_2}).
```

3. **Función de pérdida**:

```math
   L = -\sum_{i=1}^k y_i \log(y_{\text{pred}, i}).
```

---

## 2. Propagación hacia Atrás

### Gradiente en la Capa de Salida
1. **Derivada de la función de pérdida con respecto a $\mathbf{z_2}$**:

- La salida de softmax es:

```math
     y_{\text{pred}, i} = \frac{e^{z_{2,i}}}{\sum_{j=1}^k e^{z_{2,j}}}.
```

- Gradiente:

```math
     \mathbf{\delta_2} = \frac{\partial L}{\partial \mathbf{\mathbf{z_2}}} = y_{\text{pred}} - y,
```
donde $\mathbf{\delta_2} \in \mathbb{R}^k$.

2. **Gradiente con respecto a $W_2$**:

- Gradiente de los pesos de la capa de salida:

```math
     \frac{\partial L}{\partial W_2} = \mathbf{\delta_2} \mathbf{a_1}^t.
```

---

### Gradiente en la Capa Oculta
3. **Propagación del gradiente hacia $\mathbf{z_1}$**:
- Propagación desde $\mathbf{\delta_2}$:

```math
     \frac{\partial L}{\partial \mathbf{a_1}} = W_2^t \mathbf{\delta_2}.
```

- Aplicamos la derivada de ReLU:

```math
     \frac{\partial \mathbf{a_1}}{\partial \mathbf{z_1}} = \text{diag}(\mathbb{1}_{\mathbf{z_1} > 0}),
```
donde $\mathbb{1}_{\mathbf{z_1} > 0}$ es un vector indicador que es 1 si $\mathbf{z_1} > 0$, y 0 en caso contrario.

- Gradiente de $\mathbf{z_1}$:
   
```math
     \mathbf{\delta_1} = \frac{\partial L}{\partial \mathbf{z_1}} = \frac{\partial L}{\partial \mathbf{a_1}} \odot \text{diag}(\mathbb{1}_{\mathbf{z_1} > 0}),
```
donde $\odot$ denota el producto elemento a elemento.

4. **Gradiente con respecto a $W_1$**:
- Gradiente de los pesos de la capa oculta:

```math
     \frac{\partial L}{\partial W_1} = \mathbf{\delta_1} \mathbf{x}^t.
```

---

## Resumen del Cálculo de Gradientes
1. **Capa de salida**:

```math
   \mathbf{\delta_2} = y_{\text{pred}} - y, \quad \frac{\partial L}{\partial W_2} = \mathbf{\delta_2} \mathbf{a_1}^t.
```

2. **Capa oculta**:

```math
   \mathbf{\delta_1} = (W_2^t \mathbf{\delta_2}) \odot \mathbb{1}_{\mathbf{z_1} > 0}, \quad \frac{\partial L}{\partial W_1} = \mathbf{\delta_1} \mathbf{x}^t.
```
