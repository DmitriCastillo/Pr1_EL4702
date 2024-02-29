"""
Proyecto 1 Probabilidad y Esatdística
Análisis de Concentración de Benzeno
Creado por:
           Axel Dmitri Castillo Collao 2023154988
	   Felipe Sánchez Segura 2023083272
           Yair González Núñez 202304804
"""

# Importamos los módulos necesarios
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Importamos los datos del excel
ArchivoXl =pd.read_excel(r'AirQualityUCI.xlsx') #<- Hay que tener el documento excel y  .py en la misma carpeta
DatosTiempo = ArchivoXl[ArchivoXl['C6H6(GT)']>-200]['Time']
Datos = ArchivoXl[ArchivoXl['C6H6(GT)']>-200]['C6H6(GT)']

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
print("-------- Medidas de Tendencia y variabilidad --------")
print("   Total de datos: \n   -> n =", n)
print("   Minimo: \n   ->",minimo,"\n""   Maximo:\n   ->",maximo)
print("   Media:\n   ->", np.mean(arreglo))
print("   Mediana:\n   ->", np.median(arreglo))
print("   Desviación estándar:\n   ->", np.std(arreglo))
print("   Varianza:\n   ->", np.var(arreglo),'\n')


# Datos para un histograma sin utilizar los intervalos de tiempo
clases = math.ceil(math.sqrt(n))
rango = maximo-minimo
intervalos = ((rango)+(rango * 0.5))/clases

# Prueba de las operaciones para el histograma
print("----------- Operaciones para el histograma ----------")
print('   Clases:\n   ->', clases)
print('   Rango:\n   ->', rango)
print('   Intervalos:\n   ->', intervalos,'\n')
# Generamos los datos para el gráfico

plt.figure()
plt.hist(arreglo, bins=clases, edgecolor='blue')

plt.xlabel('Concentración real de benceno promediada por hora en microg/m^3')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Generamos el diagrama de puntos
plt.figure()    
plt.plot(Horas, arreglo, 'bo')
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d:%M'))
plt.xticks(rotation=90)
plt.xlabel('Horas')
plt.ylabel('Concentración real de benceno promediada por hora en microg/m^3')
plt.title('Diagrama de puntos')

plt.figure()    
plt.boxplot(Datos, patch_artist=True, labels=['C6H6'])
plt.ylabel('Concentración real de benceno promediada por hora en microg/m^3')
plt.title('Diagrama de cajas')
# Mostrar el histograma y el diagrama de puntos
plt.show()
