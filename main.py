import random
import time

def clamp(value, min_value, max_value):
  return max(min_value, min(value, max_value))

# Dit laat de computer altijd winnen.
def computer_pick(player_choice, sticks_left):
  k = (sticks_left - 1) / (3 + 1)
  intK = int(k)

  if k == intK:
    sticks_taken = 4 - player_choice
  else:
    sticks_taken = sticks_left - (int(k) * 3 + (int(k) + 1))
  
  return clamp(sticks_taken, 0, sticks_left)

# Functie waardoor als je de game opnieuw start niet weer de uitleg te zien krijgt.
def introgame():
  global sticks

  print('Naam invullen:')
  name = input()

  intro_texts = [
    'Gegroet ' + name + ', Welkom bij ons luciferspel!',
    '',
    'Het spel gaat als volgt: De computer kiest een willekeurig aantal lucifers tussen de 20 en 25. Dat aantal wordt door de computer als getal aan je getoond. Als speler heb je als eerste de keuze om 1, 2 of 3 lucifers weg te nemen. Daarna is het de beurt aan de computer. Ook de computer moet 1, 2 of 3 lucifers wegnemen, waarna de speler weer aan de beurt is, tot er geen lucifers meer over zijn. Degene die als laatste een lucifer MOET wegnemen, heeft verloren.'
  ]

  for text in intro_texts:
    print(text)
    time.sleep(0.1)

# Door deze def kan je het spel restarten.
def game():
  sticks = random.randrange(20, 25)

  while True:
    print ('\nAantal lucifers:', sticks)

    choice = input('Pak 1, 2 of 3 lucifers: ')

    if not choice.isnumeric():
      print ("Error, kies 1, 2 of 3")
      continue
    
    sticks_taken = int(choice)

    if sticks_taken > sticks:
      print ("ERROR, je pakt meer lucifers dan er zijn.  ")
      continue

    sticks -= sticks_taken

    if sticks_taken >= 4 or sticks_taken <= 0:
      print ('Error, kies 1, 2 of 3')
      continue

    if sticks <= 0:
      print('Je hebt het laatste lucifertje gepakt, helaas, je hebt verloren!')
      einde()
      break

    sticks_taken = computer_pick(sticks_taken, sticks)
    
    lucifer_text = " lucifer"

    if sticks_taken > 1:
      lucifer_text += "s"

    print ("De computer pakte " + str(sticks_taken) + lucifer_text)

    sticks -= sticks_taken

    if sticks <= 0: 
      print('ERROR Je hebt gewonnen van de computer, goed gedaan!')
      einde()
      break

# Restart code
def einde():
  opnieuw = input ('Wil je nog een ronde, type (ja/nee):')
  if opnieuw == 'ja':
    opnieuw = 0
    print()
    game()
  elif opnieuw == 'nee':
    print('Bedankt voor het spelen!')
  else: # Als er geen ja of nee invult.
    opnieuw = 0
    print ('Error, antwoord ja of nee')
    einde()

introgame()
game()

 