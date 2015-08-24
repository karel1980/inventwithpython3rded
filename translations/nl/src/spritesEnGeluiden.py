import pygame, sys, time, random
from pygame.locals import *

# voorbereiden pygame
pygame.init()
hoofdKlok = pygame.time.Clock()

# voorbereiden venster
VENSTERBREEDTE = 400
VENSTERHOOGTE = 400
vensterOppervlak = pygame.display.set_mode((VENSTERBREEDTE, VENSTERHOOGTE), 0, 32)
pygame.display.set_caption('Sprites en Geluiden')

# voorbereiden kleuren
ZWART = (0, 0, 0)

# voorbereiding blok-datastructuur
speler = pygame.Rect(300, 100, 40, 40)
spelerAfbeelding = pygame.image.load('speler.png')
spelerUitgerokkenAfbeelding = pygame.transform.scale(spelerAfbeelding, (40, 40))
voedselAfbeelding = pygame.image.load('kers.png')
voedsel = []
for i in range(20):
    voedsel.append(pygame.Rect(random.randint(0, VENSTERBREEDTE - 20), random.randint(0, VENSTERHOOGTE - 20), 20, 20))

voedselTeller = 0
NIEUWVOEDSEL = 40

# voorbereiden toestenbord-variabelen.
beweegLinks = False
beweegRechts = False
beweegBoven = False
beweegOnder = False

BEWEEGSNELHEID = 6

# set up music
opraapGeluid = pygame.mixer.Sound('oprapen.wav')
pygame.mixer.music.load('achtergrond.mid')
pygame.mixer.music.play(-1, 0.0)
muziekAfspelen = True

# start de spel-lus
while True:
    # controleer de 'QUIT' gebeurtenis
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # pas de toetsenbord-variabelen aan
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
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                beweegLinks = False
            if event.key == K_RIGHT or event.key == ord('d'):
                beweegRechts = False
            if event.key == K_UP or event.key == ord('w'):
                beweegBoven = False
            if event.key == K_DOWN or event.key == ord('s'):
                beweegOnder = False
            if event.key == ord('x'):
                speler.top = random.randint(0, VENSTERHOOGTE - speler.height)
                speler.left = random.randint(0, VENSTERBREEDTE - speler.width)
            if event.key == ord('m'):
                if muziekAfspelen:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                muziekAfspelen = not muziekAfspelen

        if event.type == MOUSEBUTTONUP:
            voedsel.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    voedselTeller += 1
    if voedselTeller >= NIEUWVOEDSEL:
        # voeg nieuw voedsel toe
        voedselTeller = 0
        voedsel.append(pygame.Rect(random.randint(0, VENSTERBREEDTE - 20), random.randint(0, VENSTERHOOGTE - 20), 20, 20))

    # teken de zwarte achtergrond op het oppervlak
    vensterOppervlak.fill(ZWART)

    # beweeg de speler
    if beweegOnder and speler.bottom < VENSTERHOOGTE:
        speler.top += BEWEEGSNELHEID
    if beweegBoven and speler.top > 0:
        speler.top -= BEWEEGSNELHEID
    if beweegLinks and speler.left > 0:
        speler.left -= BEWEEGSNELHEID
    if beweegRechts and speler.right < VENSTERBREEDTE:
        speler.right += BEWEEGSNELHEID


    # teken het blok op het oppervlak
    vensterOppervlak.blit(spelerUitgerokkenAfbeelding, speler)

    # controleer of het blok overlapt met een van de voedsel-vierkanten
    for eten in voedsel[:]:
        if speler.colliderect(eten):
            voedsel.remove(eten)
            speler = pygame.Rect(speler.left, speler.top, speler.width + 2, speler.height + 2)
            spelerUitgerokkenAfbeelding = pygame.transform.scale(spelerAfbeelding, (speler.width, speler.height))
            if muziekAfspelen:
                opraapGeluid.play()

    # teken het voedsel
    for eten in voedsel:
        vensterOppervlak.blit(voedselAfbeelding, eten)

    # teken het venster op het scherm
    pygame.display.update()
    hoofdKlok.tick(40)
