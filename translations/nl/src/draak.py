import random
import time

def toonIntroductie():
    print('Je bent in een land vol draken. Voor je zie je')
    print('twee grotten. In één grot zit een vriendelijke draak')
    print('die zijn schat met jou wil delen. De andere draak is')
    print('gierig en hongerig, en wil je in één hap opeten als hij je ziet')
    print()

def kiesGrot():
    grot = ''
    while grot != '1' and grot != '2':
        print('In welke grot ga je? (1 of 2)')
        grot = input()

    return grot

def controleerGrot(gekozenGrot):
    print('Je stapt richting de grot...')
    time.sleep(2)
    print('Het is er donker en spookachtig...')
    time.sleep(2)
    print('Een grote draak spring recht voor je tevoorschijn! Hij opent zijn kaken en...')
    print()
    time.sleep(2)

    vriendelijkeGrot = random.randint(1, 2)

    if gekozenGrot == str(vriendelijkeGrot):
         print('Geeft je zijn schat!')
    else:
         print('Eet je op met haar en huid!')

speelOpnieuw = 'ja'
while speelOpnieuw == 'ja' or speelOpnieuw == 'j':

    toonIntroductie()

    grotGetal = kiesGrot()

    controleerGrot(grotGetal)

    print('Wil je opnieuw spelen? (ja of nee)')
    speelOpnieuw = input()
