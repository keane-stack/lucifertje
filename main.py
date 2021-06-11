import random

#def waardoor als je de game opnieuwstart niet weer de uitleg te zien krijgt
def introgame():
  global sticks 
  print('Naam invullen:')
  x = input()
  print('Gegroet ' + x + ', Welkom bij ons luciferspel!')
  print('')
  print('Het spel gaat als volgt: De computer kiest een willekeurig aantal lucifers tussen de 20 en 25. Dat aantal wordt door de computer als getal aan je getoond. Als speler heb je als eerste de keuze om 1, 2 of 3 lucifers weg te nemen. Daarna is het de beurt aan de computer. Ook de computer moet 1, 2 of 3 lucifers wegnemen, waarna de speler weer aan de beurt is, tot er geen lucifers meer over zijn. Degene die als laatste een lucifer MOET wegnemen, heeft verloren.')
#door deze def kan je het spel restarten
def game():
  sticks = random.randrange (20,25)
  while True:
    print ('\nAantal lucifers', sticks)

    choice = input('Pak je stokjes(1-3):')

    if not choice.isnumeric():
      print ("Error, kies 1, 2 of 3")
      continue

    sticks_taken = int(choice)
    if sticks == 1:
        print('Je hebt het laatste lucifertje gepakt, losertje')
        einde()
        break
    if sticks_taken >= 4 or sticks_taken <= 0:
        print ('Error, kies 1, 2 of 3')
        continue

        #dit laat de computer altijd winnen
    print ("Computer took: " , (4 - sticks_taken))
    sticks -= 4
    if sticks == 0: 
         print('Je hebt gewonnen van de computer, whiehoo')
         einde()
def einde():
#restart code
 opnieuw = input ('Wil je nog een ronde, type (ja/nee):')
 if opnieuw == 'ja':
  opnieuw = 0
  print()
  game()

 elif opnieuw == 'nee':
  print('AjuParaplu')
 #als er geen ja of nee invult
 else:
  opnieuw = 0
  print ('Geef eens een antwoord, ja of nee')
  einde()
introgame()
game()


 