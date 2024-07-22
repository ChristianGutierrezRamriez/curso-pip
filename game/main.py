# Proyecto piedra papel o tijera
import random
import os

#Seleccion de jugadores
player1 = input("Ingrese su nombre: ")
player_wins=0
computer_wins=0
options=('piedra','papel','tijera')
games=input('Ingrese el numero de juegos: ')
while not games.isdigit():
  print('Ingrese un numero valido')
  games=input('Ingrese el numero de juegos: ')
games_2=int(games)
counter_games=0

#funciones
def winner(player_option,computer_option):
  global player_wins,computer_wins

  if player_option == computer_option:
    print('Empate')
    print(f'Marcador {player1} {player_wins} vs {computer_wins} computadora')
  elif player_option == 'piedra' and computer_option == 'papel':
    print(f'{player1} pierde, papel le gana a piedra')
    computer_wins += 1
    print(f'Marcador {player1} {player_wins} vs {computer_wins} computadora')
  elif player_option == 'piedra' and computer_option == 'tijera':
    print(f'{player1} gana, piedra le gana a tijera')
    player_wins += 1
    print(f'Marcador {player1} {player_wins} vs {computer_wins} computadora')
  elif player_option =='papel' and computer_option == 'piedra':
    print(f'{player1} gana, papel le gana a piedra')
    player_wins += 1
    print(f'Marcador {player1} {player_wins} vs {computer_wins} computadora')
  elif player_option == 'papel' and computer_option == 'tijera':
    print(f'{player1} pierde, papel pierde con tijera')
    computer_wins += 1
    print(f'Marcador {player1} {player_wins} vs {computer_wins} computadora')
  elif player_option == 'tijera' and computer_option == 'piedra':
    print(f'{player1} pierde, tijera pierde con piedra')
    computer_wins += 1
    print(f'Marcador {player1} {player_wins} vs {computer_wins} computadora')
  elif player_option == 'tijera' and computer_option == 'papel':
    print(f'{player1} gana, tijera le gana a papel')
    player_wins += 1
    print(f'Marcador {player1} {player_wins} vs {computer_wins} computadora')

#funcion clear
def clear():
  _ = os.system('cls')

#inicio del juego
print('Bienvenido al juego de piedra, papel o tijera')

while player_wins < games_2 and computer_wins < games_2:
  print(f'\nJuego {counter_games+1}')
  
  player_option=input('Digite una opcion: \npiedra \npapel \ntijera\n').lower()
  
  while player_option not in options:
    player_option=input('Digite una opcion correcta: \npiedra \npapel \ntijera\n').lower()
    
  computer_option=random.choice(options)
  
  print(f'{player1} escogio {player_option} y la computadora escogio {computer_option}')
  
  winner(player_option,computer_option)
  
  play=input('Quieres continuar? (si/no)')
  if play == 'no':
    print(f'{player1} gana {player_wins} veces y la computadora gana {computer_wins} veces')
    break

  counter_games+=1
  #clear()

#fin del juego
if player_wins > computer_wins:
  print(f'{player1} gana el juego')
else:
  print(f'El computador gana el juego')
print(f'fin del juego, Gracias por jugar!')