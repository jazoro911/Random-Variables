# Generación de números pseudoaleatorios utilizando el método del congruencial lineal. 
# Determinística pero aparentemente aleatoria.

import random

def generador_LCG_norm(semilla,a,c,m,N): # N : cantidad de números pseudoaleatorios a generar

    pseudo_lcg = []
    x = semilla

    for _ in range(N):
        x = ((a * x + c) % m) / m # Normalizamos dividiendo por m para obtener un número entre 0 y 1
        pseudo_lcg.append(x)

    return pseudo_lcg

## Ejemplo de uso
semilla = 123 # Douglas Adams
a = 6        # (a-1) es multiplo de m y a < m
c = 8        # c <= (m-1)
m = 15       # m y c son primos relativos ---> MCD(m,c) = 1
N = 10

numeros_pseudoaleatorios = generador_LCG_norm(semilla, a, c, m, N)
print(numeros_pseudoaleatorios)

random.seed(123)  
print([random.random() for _ in range(10)])  # Genera 10 números pseudoaleatorios utilizando la función random() de la biblioteca random de Python.

# El método LCG es diferente al método que utiliza Python (Mersenne Twister),
# por lo que los números generados serán diferentes.







