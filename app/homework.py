import csv

def read_csv(path):
  total = 0
  data = []
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = ['Departamento', 'Cantidad']
    for item in reader:
      iterable = zip(header, item)
      new_data = {key: value for key, value in iterable}
      data.append(new_data)
      total += int(item[1])
  print(data)
  print(total)

  return total
  
if __name__ == '__main__':  
  response = read_csv('./app/data2.csv')
  print(response)