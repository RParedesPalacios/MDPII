
# Obtener el estimador por máxima verosimilitud de la varianza en una gaussiana univariada

Necesitamos estimar los parámetros de la distribución gaussiana: la media $\mu$ y la varianza $\sigma^2$. 

## Paso 1: Definir la Función de Verosimilitud

Supongamos que tenemos un conjunto de datos $\left\{x_1, x_2, \dots, x_n\right\}$ que proviene de una distribución normal con media $\mu$ y varianza $\sigma^2$. La función de densidad de probabilidad de una distribución normal univariada es:

$f(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$

La función de verosimilitud $L(\mu, \sigma^2)$ para el conjunto de datos $ \{x_1, x_2, \dots, x_n\} $ es el producto de las densidades para todas las observaciones:

$
L(\mu, \sigma^2) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right).
$

## Paso 2: Logaritmo de la Función de Verosimilitud

Para simplificar la maximización, tomamos el logaritmo de la función de verosimilitud, obteniendo la log-verosimilitud:

$
\log L(\mu, \sigma^2) = -\frac{n}{2} \log(2\pi \sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2.
$

## Paso 3: Derivar las Ecuaciones de Máxima Verosimilitud

### 1. Derivada respecto a $\mu$:

$
\frac{\partial \log L(\mu, \sigma^2)}{\partial \mu} = \frac{1}{\sigma^2} \sum_{i=1}^{n} (x_i - \mu).
$

Igualando a cero para encontrar el estimador de $\mu$:

$
\sum_{i=1}^{n} (x_i - \mu) = 0 \implies \hat{\mu} = \frac{1}{n} \sum_{i=1}^{n} x_i.
$

### 2. Derivada respecto a $\sigma^2$:


Aquí vamos a desarrollar paso a paso la derivada con respecto a $\sigma^2$ para explicar por qué desaparece el término $\pi$ al realizar la derivada.

La expresión de la log-verosimilitud es:

$
\log L(\mu, \sigma^2) = -\frac{n}{2} \log(2\pi \sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2.
$

Esta expresión tiene dos términos: uno involucra $\log(2\pi \sigma^2)$ y el otro involucra la suma de los cuadrados de las diferencias $(x_i - \mu)^2$. Nuestro objetivo es derivar esta expresión respecto a $\sigma^2$.

#### Derivada del Primer Término

El primer término de la log-verosimilitud es:

$
-\frac{n}{2} \log(2\pi \sigma^2).
$

Para derivar este término respecto a $\sigma^2$, utilizamos la regla de la derivada de una función logarítmica, $\frac{d}{dx}[\log(x)] = \frac{1}{x}$, y la regla de la cadena:

$
\frac{d}{d\sigma^2} \left[ -\frac{n}{2} \log(2\pi \sigma^2) \right] = -\frac{n}{2} \cdot \frac{1}{2\pi \sigma^2} \cdot 2\pi.
$

Simplificando este resultado, tenemos:

$
\frac{d}{d\sigma^2} \left[ -\frac{n}{2} \log(2\pi \sigma^2) \right] = -\frac{n}{2} \cdot \frac{1}{\sigma^2}.
$

Como puedes ver, el término $2\pi$ se cancela, y el resultado final es:

$
-\frac{n}{2\sigma^2}.
$

#### Derivada del Segundo Término

El segundo término es:

$
-\frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2.
$

Para derivar este término respecto a $\sigma^2$, utilizamos la regla de la derivada $\frac{d}{dx} \left( \frac{1}{x} \right) = -\frac{1}{x^2}$:

$
\frac{d}{d\sigma^2} \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2 \right] = \frac{1}{2\sigma^4} \sum_{i=1}^{n} (x_i - \mu)^2.
$

#### Combinar Ambas Derivadas

Juntando los resultados de las dos derivadas, obtenemos:

$
\frac{\partial \log L(\mu, \sigma^2)}{\partial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4} \sum_{i=1}^{n} (x_i - \mu)^2.
$


## Resolver

Igualando a cero para encontrar el estimador de $\sigma^2$:

$
-\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4} \sum_{i=1}^{n} (x_i - \hat{\mu})^2 = 0.
$

Multiplicando por $2\sigma^4$:

$
-n\sigma^2 + \sum_{i=1}^{n} (x_i - \hat{\mu})^2 = 0.
$

Despejando $\sigma^2$:

$
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \hat{\mu})^2.
$
