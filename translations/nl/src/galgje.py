import random
GALGJETEKENINGEN = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
woorden = 'mier baviaan das vleermuis beer bever kameel kat mossel cobra poema coyote kraai hert hond ezel eend arend fret vos kikker geit gans havik leeuw hagedis lama mol aap eland muis salamander otter uil panda papegaai duif python konijn ram rat raaf neushoorn zeehond haai schaap stinkdier luiaard slang spin ooievaar zwaan tijger pad forel kalkoen schildpad wezel walvis wolf wombat zebra'.split()

def kiesWillekeurigWoord(woordenLijst):
     # Deze functie retourneert een willekeurig woord uit een lijst van woorden
    woordPositie = random.randint(0, len(woordenLijst) - 1)
    return woordenLijst[woordPositie]

def toonBord(GALGJETEKENINGEN, fouteLetters, juisteLetters, geheimWoord):
    print(GALGJETEKENINGEN[len(fouteLetters)])
    print()

    print('Foute letters:', end=' ')
    for letter in fouteLetters:
        print(letter, end=' ')
    print()

    blancos = '_' * len(geheimWoord)

    for i in range(len(geheimWoord)): # vervang blanco's door correct geraden letters
        if geheimWoord[i] in juisteLetters:
            blancos = blancos[:i] + geheimWoord[i] + blancos[i+1:]

    for letter in blancos: # toon het geheime woord met een spatie tussen elke letter
        print(letter, end=' ')
    print()

def geefPoging(reedsGeraden):
    # Retourneert de letter die de speler ingaf. Deze functie verzekert dat de speler een enkele letter koos, en niets anders.
    while True:
        print('Raad een letter.')
        poging = input()
        poging = poging.lower()
        if len(poging) != 1:
            print('Geef een enkele letter in.')
        elif poging in reedsGeraden:
            print('Je heb die letter al geprobeerd. Kies opnieuw.')
        elif poging not in 'abcdefghijklmnopqrstuvwxyz':
            print('Geef alstublief een LETTER in.')
        else:
            return poging

def speelOpnieuw():
    # Deze functie retourneert True als de speler opnieuw wil spelen, anders False
    print('Wil je nogmaals spelen? (ja of nee)')
    return input().lower().startswith('j')


print('G A L G J E'))
fouteLetters = ''
juisteLetters = ''
geheimWoord = kiesWillekeurigeWoord(woorden)
spelIsGedaan = False

while True:
    toonBord(GALGJETEKENINGEN, fouteLetters, juisteLetters, geheimWoord)

    # Laat de speler een letter intypen
    poging = geefPoging(fouteLetters + juisteLetters)

    if poging in geheimWoord:
        juisteLetters = juisteLetters + poging

        # Controleer of de speler gewonnen is
        alleLettersGevonden = True
        for i in range(len(geheimWoord)):
            if geheimWoord[i] not in juisteLetters:
                alleLettersGevonden = False
                break
        if alleLettersGevonden:
            print('Juist! Het geheime woord is "' + geheimWoord + '"! Je bent gewonnen!')
            spelIsGedaan = True
    else:
        fouteLetters = fouteLetters + poging

        # Controleer of de speler te veel pogingen heeft gedaan en verliest
        if len(fouteLetters) == len(GALGJETEKENINGEN) - 1:
            toonBord(GALGJETEKENINGEN, fouteLetters, juisteLetters, geheimWoord)
            print('Je hebt alle pogingen opgebruikt!\nJe deed ' + str(len(fouteLetters)) + ' foute pogingen en ' + str(len(juisteLetters)) + ' juiste pogingen. Het woord was "' + geheimWoord + '"')
            spelIsGedaan = True

    # Vraag de speler of ze nog eens willen spelen (maar alleen als het spel gedaan is).
    if spelIsGedaan:
        if speelOpnieuw():
            fouteLetters = ''
            juisteLetters = ''
            spelIsGedaan = False
            geheimWoord, geheimCategorie = kiesWillekeurigWoord(words)
        else:
            break
