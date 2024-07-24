"""
El reto consiste en graficar el porcentaje de poblacion mundial de cada pais

Proceso
1 Leer la data
2 Crear una lista con los paises
3 Crear una lista con los porcentajes
4 Crear un grafico de torta
"""

import matplotlib.pyplot as plt
import utils

def run():
  data = utils.load_data('./app/data.csv')
  labels = list(map(lambda x: x['Country/Territory'], data))
  values = list(map(lambda x: x['World Population Percentage'], data))
  utils.generate_pie_chart(labels, values)

if __name__ == '__main__':
  run()