import csv

import matplotlib.pyplot as plt

"""
Trabajos de clase

def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
  """
#Proyecto poblacion mundial

#saludo de bienvenida
def welcome():
  """
  Esta funcion imprime un saludo de bienvenida
  """
  print('Bienvenido al programa de poblacion mundial Versión 1.0')

def load_data(path):
  """
  Esta funcion carga los datos de un archivo csv
  """
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = dict(iterable)
      data.append(country_dict)
    return data

def user_option(data):
  """
  Esta funcion le pide al usuario que ingrese una opcion y valida que la opcion se encuentre en el dataset
  Formato data: lista de diccionarios {['Country/Territory': xxxx]}
  """
  #obtener lista de paises
  countries = [x['Country/Territory'] for x in data]
  #validar y manejar excepcion
  while True:
    try:
      option = input('Ingrese una opcion: ')
      if option.title() not in countries:
        raise Exception('El pais no se encuentra, seleccione otra opcion')
    except Exception as error:
      print(error)
    else:
      return option.title()
      break

def get_country_data(data, country):
  """
  Esta funcion filtra los datos de un pais especifico
  2022 Population,2020 Population,2015 Population,2010 Population,2000 Population,1990 Population,1980 Population,1970 Population
  """
  #filtrar los datos de un pais especifico
  country_data = list(filter(lambda item: item['Country/Territory'] == country, data))
  return country_data

def get_population_data(country_data):
  """
  Esta genera una lista con los valores de poblacion de un pais especifico
  """
  #lista con los a;os 
  years = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
  #filtrar los datos de un pais especifico
  population_data = []
  population_data.append(int(country_data[0]['2022 Population']))
  population_data.append(int(country_data[0]['2020 Population']))
  population_data.append(int(country_data[0]['2015 Population']))
  population_data.append(int(country_data[0]['2010 Population']))
  population_data.append(int(country_data[0]['2000 Population']))
  population_data.append(int(country_data[0]['1990 Population']))
  population_data.append(int(country_data[0]['1980 Population']))
  population_data.append(int(country_data[0]['1970 Population']))
  #= list(map(lambda x: x['2022 Population'], country_data))
  #population_data2 = list(country_data.values())
  #print(f'datos de utils {population_data2}')
  #population = population_data2[5:13]
  #print(f'datos de utils population {population}')
  return years, population_data

def generate_bar_chart(nombre_fig,labels, values):
  """
  Esta funcion genera un grafico de barras
  """
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{nombre_fig}bar.png')
  plt.close()

def generate_pie_chart(nombre_fig,labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{nombre_fig}_pie.png')
  plt.close()
