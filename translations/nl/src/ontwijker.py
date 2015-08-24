import pygame, random, sys
from pygame.locals import *

VENSTERBREEDTE = 600
VENSTERHOOGTE = 600
TEKSTKLEUR = (255, 255, 255)
ACHTERGRONDKLEUR = (0, 0, 0)
FPS = 40
SLECHTERIKMINGROOTTE = 10
SLECHTERIKMAXGROOTTE = 40
SLECHTERIKMINSNELHEID = 1
SLECHTERIKMAXSNELHEID = 8
NIEUWESLECHTERIKSNELHEID = 6
SPELERVERPLAATSSNELHEID = 5

def beeindigen():
    pygame.quit()
    sys.exit()

def wachtToSpelerToetsIndrukt():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                beeindigen()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    beeindigen()
                return

def spelerRaaktSlechterik(spelerRechthoek, slechteriken):
    for s in slechteriken:
        if spelerRechthoek.colliderect(s['rechthoek']):
            return True
    return False

def tekenTekst(tekst, lettertype, oppervlak, x, y):
    tekstvoorwerp = lettertype.render(tekst, 1, TEKSTKLEUR)
    tekstrechthoek = tekstvoorwerp.get_rect()
    tekstrechthoek.topleft = (x, y)
    oppervlak.blit(tekstvoorwerp, tekstrechthoek)

# Voorbereiding pygame, venster en muis
pygame.init()
hoofdKlok = pygame.time.Clock()
vensterOppervlak = pygame.display.set_mode((VENSTERBREEDTE, VENSTERHOOGTE))
pygame.display.set_caption('Ontwijker')
pygame.mouse.set_visible(False)

# Voorbereiding lettertype
lettertype = pygame.font.SysFont(None, 48)

# Voorbereiding geluiden
spelVoorbijGeluid = pygame.mixer.Sound('spelvoorbij.wav')
pygame.mixer.music.load('achtergrond.mid')

# Voorbereiding afbeeldingen
spelerAfbeelding = pygame.image.load('speler.png')
spelerRechthoek = spelerAfbeelding.get_rect()
slechterikAfbeelding = pygame.image.load('slechterik.png')

# Toon het 'Start' scherm
tekenTekst('Ontwijker', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3), (VENSTERHOOGTE / 3))
tekenTekst('Druk op een toets om te beginnen.', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3) - 30, (VENSTERHOOGTE / 3) + 50)
pygame.display.update()
wachtToSpelerToetsIndrukt()


besteScore = 0
while True:
    # Voorbereiding begin spel
    slechteriken = []
    score = 0
    spelerRechthoek.topleft = (VENSTERBREEDTE / 2, VENSTERHOOGTE - 50)
    beweegLinks = beweegRechts = beweegBoven = beweegOnder = False
    valsspelenOmgekeerd = valsspelenTraag = False
    slechterikTeller = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # De spel-lus gaat door zolang het spel bezig is
        score += 1 # verhoog de score

        for event in pygame.event.get():
            if event.type == QUIT:
                beeindigen()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    valsspelenOmgekeerd = True
                if event.key == ord('x'):
                    valsspelenTraag = True
                if event.key == K_LEFT or event.key == ord('a'):
                    beweegRechts = False
                    beweegLinks = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    beweegLinks = False
                    beweegRechts = True
                if event.key == K_UP or event.key == ord('w'):
                    beweegOnder = False
                    beweegBoven = True
                if event.key == K_DOWN or event.key == ord('s'):
                    beweegBoven = False
                    beweegOnder = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    valsspelenOmgekeerd = False
                    score = 0
                if event.key == ord('x'):
                    valsspelenTraag = False
                    score = 0
                if event.key == K_ESCAPE:
                        beeindigen()

                if event.key == K_LEFT or event.key == ord('a'):
                    beweegLinks = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    beweegRechts = False
                if event.key == K_UP or event.key == ord('w'):
                    beweegBoven = False
                if event.key == K_DOWN or event.key == ord('s'):
                    beweegOnder = False

            if event.type == MOUSEMOTION:
                # Als de muis beweegt, beweeg de speler dan naar waar de muis is
                spelerRechthoek.move_ip(event.pos[0] - spelerRechthoek.centerx, event.pos[1] - spelerRechthoek.centery)

        # Voeg nieuwe slechteriken toe bovenaan het scherm.
        if not valsspelenOmgekeerd and not valsspelenTraag:
            slechterikTeller += 1
        if slechterikTeller == NIEUWESLECHTERIKSNELHEID:
            slechterikTeller = 0
            slechterikGrootte = random.randint(SLECHTERIKMINGROOTTE, SLECHTERIKMAXGROOTTE)
            newBaddie = {'rechthoek': pygame.Rect(random.randint(0, VENSTERBREEDTE-slechterikGrootte), 0 - slechterikGrootte, slechterikGrootte, slechterikGrootte),
                        'snelheid': random.randint(SLECHTERIKMINSNELHEID, SLECHTERIKMAXSNELHEID),
                        'oppervlak':pygame.transform.scale(slechterikAfbeelding, (slechterikGrootte, slechterikGrootte)),
                        }

            slechteriken.append(newBaddie)

        # Beweeg de speler.
        if beweegLinks and spelerRechthoek.left > 0:
            spelerRechthoek.move_ip(-1 * SPELERVERPLAATSSNELHEID, 0)
        if beweegRechts and spelerRechthoek.right < VENSTERBREEDTE:
            spelerRechthoek.move_ip(SPELERVERPLAATSSNELHEID, 0)
        if beweegBoven and spelerRechthoek.top > 0:
            spelerRechthoek.move_ip(0, -1 * SPELERVERPLAATSSNELHEID)
        if beweegOnder and spelerRechthoek.bottom < VENSTERHOOGTE:
            spelerRechthoek.move_ip(0, SPELERVERPLAATSSNELHEID)

        # Beweeg de muis cursor om met de speler overeen te komen.
        pygame.mouse.set_pos(spelerRechthoek.centerx, spelerRechthoek.centery)

        # Beweeg de slechteriken naar beneden.
        for s in slechteriken:
            if not valsspelenOmgekeerd and not valsspelenTraag:
                s['rechthoek'].move_ip(0, s['snelheid'])
            elif valsspelenOmgekeerd:
                s['rechthoek'].move_ip(0, -5)
            elif valsspelenTraag:
                s['rechthoek'].move_ip(0, 1)

        # Verwijder slechteriken die van het venster afgevallen zijn
        for s in slechteriken[:]:
            if s['rechthoek'].top > VENSTERHOOGTE:
                slechteriken.remove(s)

        # Teken de spelwereld op het scherm.
        vensterOppervlak.fill(ACHTERGRONDKLEUR)

        # Teken de score en de hoogste score.
        tekenTekst('Score: %s' % (score), lettertype, vensterOppervlak, 10, 0)
        tekenTekst('Top Score: %s' % (besteScore), lettertype, vensterOppervlak, 10, 40)

        # Teken de rechthoek van de speler
        vensterOppervlak.blit(spelerAfbeelding, spelerRechthoek)

        # Teken alle slechteriken
        for s in slechteriken:
            vensterOppervlak.blit(s['oppervlak'], s['rechthoek'])

        pygame.display.update()

        # Controleer of er slechteriken de speler aanraken.
        if spelerRaaktSlechterik(spelerRechthoek, slechteriken):
            if score > besteScore:
                besteScore = score # pas de beste score aan
            break

        hoofdKlok.tick(FPS)

    # Stop het spel en ga naar het 'GAME OVER' scherm
    pygame.mixer.music.stop()
    spelVoorbijGeluid.play()

    tekenTekst('GAME OVER', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3), (VENSTERHOOGTE / 3))
    tekenTekst('Druk op een toets om opnieuw te spelen.', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3) - 80, (VENSTERHOOGTE / 3) + 50)
    pygame.display.update()
    wachtToSpelerToetsIndrukt()

    spelVoorbijGeluid.stop()
