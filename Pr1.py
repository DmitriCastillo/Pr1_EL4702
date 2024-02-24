# Importamos los módulos necesarios
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Importamos los datos del excel
ArchivoXl =pd.read_excel(r'C:\Users\dmitr\Documents\TEC\1 Semestre 2024\Probabilidad y Estadistica\Proyecto 1\AirQualityUCI.xlsx')
columna = ArchivoXl['C6H6(GT)']
arreglo = np.array(columna)
print(arreglo)

# Generamos los datos para el gráfico
x = np.array(range(10))
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

# Creamos el gráfico
plt.ion()
plt.plot(x,y)
plt.xlabel("Calidad del aire")
