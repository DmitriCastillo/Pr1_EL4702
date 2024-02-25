# Importamos los módulos necesarios
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Importamos los datos del excel
ArchivoXl =pd.read_excel(r'C:\Users\dmitr\Documents\TEC\1 Semestre 2024\Probabilidad y Estadistica\Proyecto 1\AirQualityUCI.xlsx')
columna = ArchivoXl['C6H6(GT)']
arreglo = np.array(columna)
n = len(arreglo)
minimo = min(arreglo)
maximo = max(arreglo)
sumatotal= sum(arreglo)

# Pruba de que los datos son correctos 
print("total de datos 9357")
print("length del arreglo", n)
print(arreglo)
print("minimo", minimo, "| maximo", maximo)
print("Total de datos sumados(incluyendo los -200), 17456,2")
print("Suma de guardada", sumatotal)
print("fin de la pruba")

# Datos para un histograma sin utilizar los intervalos de tiempo
clases = math.ceil(math.sqrt(n))
rango = maximo-minimo
intervalos = ((rango)+(rango * 0.5))/clases

# Pruba de las operaciones para el histograma
print('clases ',clases)
print('rango', rango)
print('intervalos', intervalos)

# Generamos los datos para el gráfico
plt.hist(arreglo, bins=clases, edgecolor='blue')

plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Mostrar el histograma
plt.show()
