
sticks = 21
print('Naam invullen:')
x = input()
print('Gegroet ' + x + ', Welkom bij ons luciferspel!')
print('')
print('Het spel gaat als volgt: De computer kiest een willekeurig aantal lucifers tussen de 20 en 25. Dat aantal wordt door de computer als getal aan je getoond. Als speler heb je als eerste de keuze om 1, 2 of 3 lucifers weg te nemen. Daarna is het de beurt aan de computer. Ook de computer moet 1, 2 of 3 lucifers wegnemen, waarna de speler weer aan de beurt is, tot er geen lucifers meer over zijn. Degene die als laatste een lucifer MOET wegnemen, heeft verloren.')

while True:
    print ('Aantal lucifers', sticks)
    sticks_taken = int(input('Pak je stokjes(1-3):'))
    if sticks == 1:
        print('Je hebt het laatste lucifertje gepakt, losertje')
        break
    if sticks_taken >= 4 or sticks_taken <= 0:
        print ('Errorgeval, kies 1, 2 of 3 luficers')
        continue

        #dit laat de computer altijd winnen
    print ("Computer took: " , (4 - sticks_taken))
    sticks -= 4
if sticks == 0:
  print('Je hebt gewonnen van de computer, whiehoo')

