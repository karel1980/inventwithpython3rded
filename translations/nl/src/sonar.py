# Sonar

import random
import sys

def tekenBord(bord):
    # Teken de bord-datastructuur.

    hlijn = '    ' # initiele ruimte voor de getallen links van het bord
    for i in range(1, 6):
        hlijn += (' ' * 9) + str(i)

    # toon de getallen aan de bovenkant
    print(hlijn)
    print('   ' + ('0123456789' * 6))
    print()

    # toon elk van de 15 rijen
    for i in range(15):
        # getallen van één cijfer moeten een extra spatie krijgen
        if i < 10:
            extraSpatie = ' '
        else:
            extraSpatie = ''
        print('%s%s %s %s' % (extraSpatie, i, geefRij(bord, i), i))

    # toon de getallen aan de onderkant
    print()
    print('   ' + ('0123456789' * 6))
    print(hlijn)


def geefRij(bord, row):
    # Retourneert een string voor een specifieke rij van het bord.
    bordRij = ''
    for i in range(60):
        bordRij += bord[i][row]
    return bordRij

def geefNieuwBord():
    # Maak een nieuwe 60x15 bord-datastructuur.
    bord = []
    for x in range(60): # de hoofdlijst is een lijst van 60 lijsten.
        bord.append([])
        for y in range(15): # elke lijst in de hooflijst bevat 15 letters
            # gebruik verschillende symbolen voor de oceaan om het meer leesbaar te maken
            if random.randint(0, 1) == 0:
                bord[x].append('~')
            else:
                bord[x].append('`')
    return bord

def geefWillekeurigeKisten(aantalKisten):
    # Maak een lijst van kist-datastructuren (lisjten met 2 items, die de x en y coordinaten zijn)
    kisten = []
    for i in range(aantalKisten):
        kisten.append([random.randint(0, 59), random.randint(0, 14)])
    return kisten

def isGeldigeZet(x, y):
    # Retourneert True als de coordinaten op het bord liggen, anders False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def doeZet(bord, kisten, x, y):
    # Change the bord data structure with a sonar device character. Remove treasure chests
    # from the chests list as they are found. Return False if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    if not isGeldigeZet(x, y):
        return False

    kleinsteAfstand = 100 # any chest will be closer than 100.
    for cx, cy in kisten:
        if abs(cx - x) > abs(cy - y):
            afstand = abs(cx - x)
        else:
            afstand = abs(cy - y)

        if afstand < kleinsteAfstand: # we want the closest treasure chest.
            kleinsteAfstand = afstand

    if kleinsteAfstand == 0:
        # xy is directly on a treasure chest!
        kisten.remove([x, y])
        return 'Je hebt een gezonken kist gevonden!'
    else:
        if kleinsteAfstand < 10:
            bord[x][y] = str(kleinsteAfstand)
            return 'Schatkist gevonden op een afstand van %s van het sonartoestel' % (kleinsteAfstand)
        else:
            bord[x][y] = 'O'
            return 'Sonar heeft niets gedetecteert. Alle schatkisten liggen buiten bereik.'


def geefSpelerZet():
    # Laat de speler haar zet intypen. Retourneert een lijst met twee getallen, de x,y coordinaten
    print('Waar wil je je volgende sonartoestel laten vallen? (0-59 0-14) (of typ stop)')
    while True:
        zet = input()
        if zet.lower() == 'stop':
            print('Bedankt om te spelen!')
            sys.exit()

        zet = zet.split()
        if len(zet) == 2 and zet[0].isdigit() and zet[1].isdigit() and isGeldigeZet(int(zet[0]), int(zet[1])):
            return [int(zet[0]), int(zet[1])]
        print('Typ een getal van 0 tot 59, een spatie, en dan een getal van 0 tot 14.')


def speelOpnieuw():
    # Deze functie retourneert True als de speler nog eens wil spelen, anders False.
    print('Wil je nogmaals spelen? (ja of nee)')
    return input().lower().startswith('j')


def toonInstructies():
    print('''Instructies:
Je bent de kapitein van de Simon, een schattenjagersschip. Je huidige missie
is om de drie schatkisten die in de diepten van het deel van de oceaan waar je bent
te vinden zijn.

Om te spelen voeg je de coordinaten in van het punt van de oceaan waar je een sonartoestel
wil laten vallen. De sonar kan detecteren hoe ver de dichtbijzijnste schatkist zich
bevindt.

Bijvoorbeeld: de 't' hieronder toont waar het toestel gevallen is, en de cijfers 2 tonen
alles op afstand 2 van het toestel. De cijfers 4 tonen alles op afstand 4 van het toestel.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 t 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
Druk op enter om door te gaan...''')
    input()

    print('''Bijvoorbeeld: Hier is een schatkist (de k) op een afstand 2 van het sonartoestel (de t).

    22222
    k   2
    2 t 2
    2   2
    22222

Het punt waar het toestel viel zal gemarkeerd worden met een 2.

Schatkisten kunnen zich niet verplaatsen. Sonartoestellen kunnen schatkisten
detecteren tot een afstand 9. Als alle kisten buiten berijk zijn zal het
punt gemarkeerd worden met een O.

Als een toestel bovenop een schatkist valt heb je de locatie van de schat
ontdekt en wordt de schat opgehaald. Het sonartoestel blijft ter plaatse.

Wanneer je een schatkist ophaalt zullen alle sonartoestellen zich aanpassen
zodat ze de afstand volgende nabije schatkist weergeven.
Druk op enter om door te gaan...''')
    input()
    print()


print('S O N A R !')
print()
print('Wil je de instructies lezen? (ja/nee)')
if input().lower().startswith('j'):
    toonInstructies()

while True:
    # voorbereidin spel
    sonarToestellen = 16
    hetBord = geefNieuwBord()
    deKisten = geefWillekeurigeKisten(3)
    tekenBord(hetBord)
    vorigeZetten = []

    while sonarToestellen > 0:
        # Begin een spelronde:

        # Toon de status van sonartoestellen en kisten
        if sonarToestellen == 1: extraSsonar = ''
        else: extraSsonar = 'len'
        if len(deKisten) == 1: extraSchest = ' blijft'
        else: extraSchest = 'en blijven'
        print('Je hebt %s sonartoestel%s over. %s schatkist%s over.' % (sonarToestellen, extraSsonar, len(deKisten), extraSchest))

        x, y = geefSpelerZet()
        vorigeZetten.append([x, y]) # we moeten alle zetten bijhouden zodat sonartoestellen aangepast kunnen worden

        zetResultaat = doeZet(hetBord, deKisten, x, y)
        if zetResultaat == False:
            continue
        else:
            if zetResultaat == 'Je hebt een gezonken kist gevonden!';
                # Pas alle sonartoestellen die momenteel op de kaart staan aan
                for x, y in vorigeZetten:
                    doeZet(hetBord, deKisten, x, y)
            tekenBord(hetBord)
            print(zetResultaat)

        if len(deKisten) == 0:
            print('Je hebt alle gezonken schatkisten gevonden! Proficiat en goed gespeeld!')
            break

        sonarToestellen -= 1

    if sonarToestellen == 0:
        print('We hebben geen sonaratoestellen over! Nu moeten we terugkeren terwijl er nog'))
        print('schatkisten te vinden waren! Game over.')
        print('    Hier waren de overgebleven schatkisten:')
        for x, y in deKisten:
            print('    %s, %s' % (x, y))

    if not speelOpnieuw():
        sys.exit()
