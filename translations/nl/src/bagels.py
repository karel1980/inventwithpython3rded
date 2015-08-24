import random
def geefGeheimGetal(aantalCijfers):
    # Retourneert een tekst die 'aantalCijfers' lang is, bestaande uit willekeurige cijfers
    cijfers = list(range(10))
    random.shuffle(cijfers)
    geheimGetal = ''
    for i in range(aantalCijfers):
        geheimGetal += str(cijfers[i])
    return geheimGetal

def geefHints(poging, geheimGetal):
    # Retourneert een tekst met de pico, fermi, bagels hints voor de gebruiker
    if poging == geheimGetal:
        return 'Je hebt het gevonden!'

    hints = []

    for i in range(len(poging)):
        if poging[i] == geheimGetal[i]:
            hints.append('Fermi')
        elif poging[i] in geheimGetal:
            hints.append('Pico')
    if len(hints) == 0:
        return 'Bagels'

    hints.sort()
    return ' '.join(hints)

def bevatEnkelCijfers(getal):
    # Retourneert True als getal een tekst is die enkel uit cijfers bestaat. Anders False.
    if getal == '':
        return False

    for i in getal:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def speelOpnieuw():
    # Deze functie retourneert True als de speler nogmaals wil spelen. Anders False.
    print('Wil je nog eens spelen? (ja of nee)')
    return input().lower().startswith('j')

AANTALCIJFERS = 3
MAXPOGINGEN = 10

print('Ik denk aan een getal met %s cijfers. Probeer te raden wat het is.' % (AANTALCIJFERS))
print('Hier zijn hints:')
print('Wat ik zeg:    Wat het betekent:')
print('  Pico         Een cijfer is juist maar in de verkeerde positie.')
print('  Fermi        Een cijfer is juist en op de juiste plaats.')
print('  Bagels       Geen enkel cijfer is juist.')

while True:
    geheimGetal = geefGeheimGetal(AANTALCIJFERS)
    print('Ik denk aan een getal. Je hebt %s pogingen om het te raden.' % (MAXPOGINGEN))

    aantalPogingen = 1
    while aantalPogingen <= MAXPOGINGEN:
        poging = ''
        while len(poging) != AANTALCIJFERS or not bevatEnkelCijfers(poging):
            print('Poging #%s: ' % (aantalPogingen))
            poging = input()

        hints = geefHints(poging, geheimGetal)
        print(hints)
        aantalPogingen += 1

        if poging == geheimGetal:
            break
        if aantalPogingen > MAXPOGINGEN:
            print('Er zijn geen pogingen over. Het antwoord was %s' % (geheimGetal))

    if not speelOpnieuw():
        break
