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
woorden = {'Kleuren':'rood oranje geel groen blauw indigo paars wit zwart bruin'.split(),
'Vormen':'vierkant driehoek rechthoek cirkel ovaal ruit trapezium vijfhoek zeshoek zevenhoek achthoek'.split(),
'Fruit':'appel sinaasappel citroen limoen peer watermeloen druif pompelmoes kers banaan meloen mango aardbei tomaat'.split(),
'Dieren':'vleermuis beer bever kat poema krab hert hond ezel eend arend vis kikker geit bloedzuiger leeuw hagedis aap eland otter uil panda python konijn rat haai schaap stinkdier inktvis tijger kalkoen schildpad wezel walvis wolf wombat zebra'.split()}

def kiesWillekeurigWoord(woordDict):
    # Deze functie retourneert een willekeurig woord uit de gegeven dictionary met lijsten van woorden samen met de sleutel.
    # Eerst kiezen we een willekeurige sleutel uit de dictionary
    woordCategorie = random.choice(list(woordDict.keys()))

    # Vervolgens kiezen we een willekeurig woord uit te lijst horend bij de sleutel
    woordPositie = random.randint(0, len(woordDict[woordCategorie]) - 1)

    return [woordDict[woordCategorie][woordPositie], woordCategorie]

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
geheimWoord, geheimCategorie = kiesWillekeurigWoord(words)
spelIsGedaan = False

while True:
    print('Het geheime woord zit in deze categorie: ' + geheimCategorie)
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
