# Reversi

import random
import sys

def tekenBord(bord):
    # Deze functie geeft het gegeven bord weer. Retourneert None
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (bord[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)


def resetBord(bord):
    # Maakt het gegeven bord leeg, behalve de originele startpositie.
    for x in range(8):
        for y in range(8):
            bord[x][y] = ' '

    # Start-stukken
    bord[3][3] = 'X'
    bord[3][4] = 'O'
    bord[4][3] = 'O'
    bord[4][4] = 'X'


def geefNieuwBord():
    # Maakt een gloednieuwe, lege bord-datastructuur.
    bord = []
    for i in range(8):
        bord.append([' '] * 8)

    return bord


def isGeldigeZet(bord, tegel, xstart, ystart):
    # Retourneert False als de zet van de speler op vak (xstart, ystart) ongeldig is.
    # Als het een geldige zet is retourneert dit de lijst van vakjes die eigendom van de speler worden indien hier gespeeld wordt.
    if bord[xstart][ystart] != ' ' or not isOpBord(xstart, ystart):
        return False

    bord[xstart][ystart] = tegel # Zet tijdelijk de tegel op het bord

    if tegel == 'X':
        andereTegel = 'O'
    else:
        andereTegel = 'X'

    tegelsOmOmTeDraaien = []
    for xrichting, yrichting in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xrichting # eerste stap in de richting
        y += yrichting # eerste stap in de richting
        if isOpBord(x, y) and bord[x][y] == andereTegel:
            # Dit is een stuk van de andere speler naast ons stuk
            x += xrichting
            y += yrichting
            if not isOpBord(x, y):
                continue
            while bord[x][y] == andereTegel:
                x += xrichting
                y += yrichting
                if not isOpBord(x, y): # Verlaat de while-lus, en ga verder in de for-lus.
                    break
            if not isOpBord(x, y):
                continue
            if bord[x][y] == tegel:
                # Er zijn stukken om om te draaien. Ga in de omgekeerde richting tot we het originele stuk tegenkomen. Onderweg houden we de tegels bij.
                while True:
                    x -= xrichting
                    y -= yrichting
                    if x == xstart and y == ystart:
                        break
                    tegelsOmOmTeDraaien.append([x, y])

    bord[xstart][ystart] = ' ' # Zet de lege tegel terug.
    if len(tegelsOmOmTeDraaien) == 0: # Indien geen enkele tegel omgedraaid werd is het geen geldige zet
        return False
    return tegelsOmOmTeDraaien


def isOpBord(x, y):
    # Retourneert True als de coordinaten op het bord te vinden zijn.
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def geefBordMetGeldigeZetten(bord, tegel):
    # Retourneert een nieuw bord met een . waar de speler een geldige zet kan doen.
    bordKopie = geefBordKopie(bord)

    for x, y in geefGeldigeZetten(bordKopie, tegel):
        bordKopie[x][y] = '.'
    return bordKopie


def geefGeldigeZetten(bord, tegel):
    # Retourneert een lijst van [x, y] lijsten met geldige zetten voor de gegeven speler
    # op het gegeven bord
    geldigeZetten = []

    for x in range(8):
        for y in range(8):
            if isGeldigeZet(bord, tegel, x, y) != False:
                geldigeZetten.append([x, y])
    return geldigeZetten


def geefScoreVanBord(bord):
    # Bepaal de score door de tegels te tellen. Geeft een map terug met de sleutels 'X' en 'O'.
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if bord[x][y] == 'X':
                xscore += 1
            if bord[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}


def vraagSpelerTegel():
    # Laat de speler typen met welke tegel hij wil spelen.
    # Geeft een lijst met de speler zijn tegel als eerste item en de tegel van de computer als tweede item.
    tegel = ''
    while not (tegel == 'X' or tegel == 'O'):
        print('Wil je X of O zijn?')
        tegel = input().upper()

    # Het eerste element in de lijst is de tegel van de speler, het tweede is de tegel van de computer
    if tegel == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def wieGaatEerst():
    # Kies willekeurig welke speler eerst gaat.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'speler'


def speelOpnieuw():
    # Deze functie retourneert True als de speler opnieuw wil spelen, of False indien niet.
    print('Wil je opnieuw spelen? (ja of nee)')
    return input().lower().startswith('j')


def doeZet(bord, tegel, xstart, ystart):
    # Zet de tegel op het bord op (xstart, ystart) en draai de tegels van de tegenspeler om.
    # Retourneert False als het een ongelidige zet is, True als het wel een geldige zet is.
    tegelsOmOmTeDraaien = isGeldigeZet(bord, tegel, xstart, ystart)

    if tegelsOmOmTeDraaien == False:
        return False

    bord[xstart][ystart] = tegel
    for x, y in tegelsOmOmTeDraaien:
        bord[x][y] = tegel
    return True


def geefBordKopie(bord):
    # Maak een kopie van de bord-lijst en geef de kopie terug.
    kopieBord = geefNieuwBord()

    for x in range(8):
        for y in range(8):
            kopieBord[x][y] = bord[x][y]

    return kopieBord


def isOpHoek(x, y):
    # Retourneert True als de positie op een van de vier hoeken is.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def geefSpelerZet(bord, spelerTegel):
    # Laat de speler zijn zet ingeven.
    # Retourneert de zet als [x, y] (of de tekst 'hints' of 'stop')
    GETALLEN1TOT8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Geef een zet in, of typ stop om het spel te stoppen, of typ hints om hints aan/uit te zetten')
        zet = input().lower()
        if zet == 'stop':
            return 'stop'
        if zet == 'hints':
            return 'hints'

        if len(zet) == 2 and zet[0] in GETALLEN1TOT8 and zet[1] in GETALLEN1TOT8:
            x = int(zet[0]) - 1
            y = int(zet[1]) - 1
            if isGeldigeZet(bord, spelerTegel, x, y) == False:
                continue
            else:
                break
        else:
            print('Dat is geen geldige zet. Typ het x-getal (1-8), gevolgd door het y-getal (1-8).')
            print('Bijvoorbeeld: 81 is rechts bovenaan.')

    return [x, y]


def geefComputerZet(bord, computerTegel):
    # Bepaalt de zet van de computer op basis van het bord en de computerTegel.
    # Retourneert de zet als [x, y]
    mogelijkeZetten = geefGeldigeZetten(bord, computerTegel)

    # Zet de mogelijke zetten in willekeurige volgorde
    random.shuffle(mogelijkeZetten)

    # always go for a corner if available.
    for x, y in mogelijkeZetten:
        if isOpHoek(x, y):
            return [x, y]

    # Overloop alle mogelijke zetten en onthoud de zet met de beste score
    besteScore = -1
    for x, y in mogelijkeZetten:
        bordKopie = geefBordKopie(bord)
        doeZet(bordKopie, computerTegel, x, y)
        score = geefScoreVanBord(bordKopie)[computerTegel]
        if score > besteScore:
            bestMove = [x, y]
            besteScore = score
    return bestMove


def toonPunten(spelerTegel, computerTegel):
    # Toont de huidige score
    scores = geefScoreVanBord(hoofdBord)
    print('Je hebt %s punten. De computer heeft %s punten.' % (scores[spelerTegel], scores[computerTegel]))




while True:
    # Reset the bord and game.
    hoofdBord = geefNieuwBord()
    resetBord(hoofdBord)
    spelerTegel, computerTegel = vraagSpelerTegel()
    toonHints = False
    beurt = wieGaatEerst()
    print(beurt + ' gaat eerst.')

    while True:
        if beurt == 'speler':
            # Beurt van de speler
            if toonHints:
                geldigeZettenBord = geefBordMetGeldigeZetten(hoofdBord, spelerTegel)
                tekenBord(geldigeZettenBord)
            else:
                tekenBord(hoofdBord)
            toonPunten(spelerTegel, computerTegel)
            zet = geefSpelerZet(hoofdBord, spelerTegel)
            if zet == 'stop':
                print('Bedankt om te spelen!')
                sys.exit() # programma beeindigen
            elif zet == 'hints':
                toonHints = not toonHints
                continue
            else:
                doeZet(hoofdBord, spelerTegel, zet[0], zet[1])

            if geefGeldigeZetten(hoofdBord, computerTegel) == []:
                break
            else:
                beurt = 'computer'

        else:
            # Beurt van de computer
            tekenBord(hoofdBord)
            toonPunten(spelerTegel, computerTegel)
            input('Druk op enter om de zet van de computer te zien.')
            x, y = geefComputerZet(hoofdBord, computerTegel)
            doeZet(hoofdBord, computerTegel, x, y)

            if geefGeldigeZetten(hoofdBord, spelerTegel) == []:
                break
            else:
                beurt = 'speler'

    # Display the final score.
    tekenBord(hoofdBord)
    scores = geefScoreVanBord(hoofdBord)
    print('X behaalde %s punten. O behaalde %s punten.' % (scores['X'], scores['O']))
    if scores[spelerTegel] > scores[computerTegel]:
        print('Je won van de computer met %s punten! Proficiat!' % (scores[spelerTegel] - scores[computerTegel]))
    elif scores[spelerTegel] < scores[computerTegel]:
        print('Je bent verloren. De computer heeft %s punten meer.' % (scores[computerTegel] - scores[spelerTegel]))
    else:
        print('Gelijkspel!')

    if not speelOpnieuw():
        break
