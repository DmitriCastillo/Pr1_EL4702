# Importamos los módulos necesarios
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Importamos los datos del excel
ArchivoXl =pd.read_excel(r'C:\Users\segur\OneDrive\Documentos\Electro\EL4702\Pr_1\AirQualityUCI.xlsx') # <-- Se agrega la ruta donde
columna = ArchivoXl['C6H6(GT)']																		                                     # esté guardado el archivo
arreglo = np.array(columna)
n = len(arreglo)
minimo = min(arreglo)
maximo = max(arreglo)
sumatotal= sum(arreglo)

# Medidas de Tendencia y variabilidad
print("----- Medidas de Tendencia y variabilidad -----")
print("Media: ", np.mean(arreglo))
print("Mediana: ", np.median(arreglo))
print("Desviación estándar: ", np.std(arreglo))
print("Varianza: ", np.var(arreglo))

# Prueba de que los datos son correctos 
print("total de datos 9357")
print("length del arreglo", n)
print(arreglo)
print("minimo", minimo, "| maximo", maximo)
print("Total de datos sumados(incluyendo los -200), 17456,2")
print("Suma de guardada", sumatotal)
print("fin de la prueba")

# Datos para un histograma sin utilizar los intervalos de tiempo
clases = math.ceil(math.sqrt(n))
rango = maximo-minimo
intervalos = ((rango)+(rango * 0.5))/clases

# Prueba de las operaciones para el histograma
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
