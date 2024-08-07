#  How do you find duplicate numbers in an array if it contains multiple duplicates?
import numpy as np

np.random.seed(0)
original_array = np.arange(1, 101)
np.random.shuffle(original_array)
mod_array = np.delete(original_array, [50, 10, 20, 30])

# Crear una lista con los números del 1 al 100
expected = list(range(1, 101))

# Inicializar una lista para los números faltantes
missing_numbers = []

# Encontrar los números faltantes usando bucles
for number in expected:
    if number not in mod_array:
        missing_numbers.append(number)

print(f'Números faltantes: {missing_numbers}')
print(f'Valores eliminados: {original_array[50]}, {original_array[10]}, {original_array[20]}, {original_array[30]}')