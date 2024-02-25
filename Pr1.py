# Importamos los módulos necesarios
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Importamos los datos del excel
ArchivoXl =pd.read_excel(r'AirQualityUCI.xlsx') <- #Hay que tener el documento excel y  .py en la misma carpeta
DatosTiempo = ArchivoXl['Time']
Datos = ArchivoXl['C6H6(GT)']

# Arreglos para los graficos
    
arreglo = np.array(Datos)
HorasEnTime = np.array(DatosTiempo)
Horas_array = []

n = len(arreglo)
minimo = min(arreglo)
maximo = max(arreglo)
sumatotal= sum(arreglo)

for hora in HorasEnTime:
    c_hora= str(hora)
    Horas_array.append(c_hora)
    
Horas = np.array(Horas_array)

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

# Pruba de las operaciones para el histograma

print('clases ',clases)
print('rango', rango)
print('intervalos', intervalos)

# Generamos los datos para el gráfico

plt.figure()
plt.hist(arreglo, bins=clases, edgecolor='blue')

plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Generamos el diagrama de puntos
plt.figure()    
plt.plot(Horas, arreglo, 'bo')
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d:%M:%S'))
plt.xticks(rotation=90)
plt.xlabel('Horas')
plt.ylabel('Resultados')
plt.title('Diagrama de puntos')

# Mostrar el histograma y el diagrama de puntos
plt.show()
