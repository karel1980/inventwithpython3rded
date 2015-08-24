# Boter, Kaas en Eieren

import random

def tekenBord(bord):
    # Deze functie toont het gegeven bord.

    # "bord" is een lijst van 10 strings die het bord voorstellen (negeer positie 0)
    print('   |   |')
    print(' ' + bord[7] + ' | ' + bord[8] + ' | ' + bord[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bord[4] + ' | ' + bord[5] + ' | ' + bord[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bord[1] + ' | ' + bord[2] + ' | ' + bord[3])
    print('   |   |')

def invoerSpelerLetter():
    # Laat de speler typen welke letter hij wil zijn.
    # Retourneert een lijst met de speler zijn keuze als eerste item, en de letter van de computer als tweede item.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Wil je X of O zijn?')
        letter = input().upper()

    # Het eerste element in de lijst is de letter van de speler, het tweede element is de letter van de computer.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def wieMagEerst():
    # Kies willekeurig wie eerst mag
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'speler'

def speelOpnieuw():
    # Deze functie retourneert True als de speler nogmaals wil spelen, anders False.
    print('Wil je nogmaals spelen? (yes or no)')
    return input().lower().startswith('y')

def doeZet(bord, letter, zet):
    bord[zet] = letter

def isWinnaar(bo, le):
    # Gegeven een bord en een letter, retourneert True als de speler met de gegeven letter
    # 3 op een rij heeft. We korten af met bo en le zodat we minder hoeven te typen.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # eerste rij
    (bo[4] == le and bo[5] == le and bo[6] == le) or # middenste rij
    (bo[1] == le and bo[2] == le and bo[3] == le) or # onderste rij
    (bo[7] == le and bo[4] == le and bo[1] == le) or # linker kolom
    (bo[8] == le and bo[5] == le and bo[2] == le) or # middenste kolom
    (bo[9] == le and bo[6] == le and bo[3] == le) or # rechter kolom
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonaal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonaal

def maakBordKopie(bord):
    # Maak een kopie van de bord-lijst en retourneer de kopie
    kopieBord = []

    for i in bord:
        kopieBord.append(i)

    return kopieBord

def isVrijVak(bord, zet):
    # Retourneert True als de gegeven zet vrij is op het bord.
    return bord[zet] == ' '

def geefSpelerZet(bord):
    # Laat de speler zijn zet intypen.
    zet = ' '
    while zet not in '1 2 3 4 5 6 7 8 9'.split() or not isVrijVak(bord, int(zet)):
        print('Wat is je volgende zet? (1-9)')
        zet = input()
    return int(zet)

def geefWillekeurigeZetUitLijst(bord, zettenLijst):
    # Retourneert een geldige zet uit de gegeven lijst op het gegeven bord.
    # Retourneert None als er geen geldige zet is.
    mogelijkeZetten = []
    for i in zettenLijst:
        if isVrijVak(bord, i):
            mogelijkeZetten.append(i)

    if len(mogelijkeZetten) != 0:
        return random.choice(mogelijkeZetten)
    else:
        return None

def geefComputerZet(bord, computerLetter):
    # Gegeven een bord en de letter van de computer, bepaal welke zet te doen en geef die zet terug.
    if computerLetter == 'X':
        spelerLetter = 'O'
    else:
        spelerLetter = 'X'

    # Hier is ons algoritme voor de Boter Kaas en Eieren AI.
    # Eerst controleren we of we de volgende zet kunnen winnen.
    for i in range(1, 10):
        kopie = geefBordKopie(bord)
        if isVrijVak(kopie, i):
            doeZet(kopie, computerLetter, i)
            if isWinnaar(kopie, computerLetter):
                return i

    # Controleer of de speler zou kunnen winnen in de voolgende zet,
    # en blokkeer hem.
    for i in range(1, 10):
        kopie = geefBordKopie(bord)
        if isVrijVak(kopie, i):
            doeZet(kopie, spelerLetter, i)
            if isWinnaar(kopie, spelerLetter):
                return i

    # Probeer om een van de hoeken te kiezen, als ze vrij zijn.
    zet = kiesWillekeurigeZetUitLijst(bord, [1, 3, 7, 9])
    if zet != None:
        return zet

    # Probeer op het midden te zetten, als het vrij is.
    if isVrijVak(bord, 5):
        return 5

    # Doe een zet op de zijkanten
    return geefWillekeurigeZetUitLijst(bord, [2, 4, 6, 8])

def isBordVol(bord):
    # Retourneert True als ieder vak van het bord bezet is. Anders False.
    for i in range(1, 10):
        if isVrijVak(bord, i):
            return False
    return True


print('Welkom bij Boter, Kaas en Eieren!')

while True:
    # Voorbereiding bord
    hetBord = [' '] * 10
    spelerLetter, computerLetter = invoerSpelerLetter()
    beurt = wieMagEerst()
    print('De speler met ' + beurt + ' gaat eerst.')
    spelIsBezig = True

    while spelIsBezig:
        if beurt == 'speler':
            # Speler is aan de beurt
            tekenBord(hetBord)
            zet = geefSpelerZet(hetBord)
            doeZet(hetBord, spelerLetter, zet)

            if isWinnaar(hetBord, spelerLetter):
                tekenBord(hetBord)
                print('Hoera! Je bent gewonnen!')
                spelIsBezig = False
            else:
                if isBordVol(hetBord):
                    tekenBord(hetBord)
                    print('Gelijkspel!')
                    break
                else:
                    beurt = 'computer'

        else:
            # Computer is aan de beurt
            zet = geefComputerZet(hetBord, computerLetter)
            doeZet(hetBord, computerLetter, zet)

            if isWinnaar(hetBord, computerLetter):
                tekenBord(hetBord)
                print('De computer is gewonnen! Jij verliest.')
                spelIsBezig = False
            else:
                if isBordVol(hetBord):
                    tekenBord(hetBord)
                    print('Gelijkspel!')
                    break
                else:
                    beurt = 'speler'

    if not speelOpnieuw():
        break
