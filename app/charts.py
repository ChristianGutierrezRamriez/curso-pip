import matplotlib.pyplot as plt
import numpy as np
"""
Generado automaticamente
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.aix.axis('equal')
  plt.show()
"""
labels = ['a','b','c']
values = [100,200,80]

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

if __name__=='__main__':
  generate_bar_chart(labels, values)
