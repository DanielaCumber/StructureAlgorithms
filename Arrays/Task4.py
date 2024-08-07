#  How do you find all pairs of an integer array whose sum is equal to a given number?

import numpy as np

np.random.seed(0)
original_array = np.arange(1, 101)
np.random.shuffle(original_array)

# function with two descriptive arguments
def encontrar_pares_con_suma(arr, suma_objetivo):
    # Crear un diccionario para almacenar los elementos y sus índices
    diccionario = {}  # an empty dictionary (allows fast lookups) to store the array elements as we go through them
    # Set para almacenar los pares encontrados
    pair = set()  # un set evita duplicados (y las operaciones de inserción y búsqueda son rápidas)

    # Recorrer cada elemento en el array
    for num in arr:
        # Calcular el complemento necesario para alcanzar la suma objetivo
        complemento = suma_objetivo - num  # Calcular el complemento para alcanzar la suma_objetivo restando el número actual num de la suma_objetivo.

        # Verificar si el complemento ya está en el diccionario.
        if complemento in diccionario:
            # Si está, añadir el par al set. significa que hay un par cuya suma es igual a la suma_objetivo.
            pair.add((complemento, num))

        # Se añade el número actual num al diccionario para futuras verificaciones.
        diccionario[num] = True

    return pair  # La función devuelve el set pair que contiene todos los pares encontrados.

# Ejemplo
suma_objetivo = 55
pairs = encontrar_pares_con_suma(original_array, suma_objetivo)
print(f'Pares con suma {suma_objetivo}: {pairs}')

