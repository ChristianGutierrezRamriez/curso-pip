import utils
"""
Trabajos en clase
data =[
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  country = input('Type Country => ')
  
  result = utils.population_by_country(data,country)
  print(result)

if __name__ == '__main__':
  run()
"""

def iniciar_programa():
  #bienvenida al programa
  utils.welcome()
  #cargar datos
  data = utils.load_data('./data.csv')
  #solicitar al usuario una opcion
  country = utils.user_option(data)
  nombre_fig = country
  #obtener datos
  country_data = utils.get_country_data(data,country)
  print(country_data)
  #generar grafico
  years, population_data = utils.get_population_data(country_data)
  print(years,population_data)
  utils.generate_bar_chart(nombre_fig,years,population_data)
  utils.generate_pie_chart(nombre_fig,years,population_data)

if __name__ == '__main__':
  iniciar_programa()