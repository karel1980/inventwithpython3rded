import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
hoofdKlok = pygame.time.Clock()

# set up the window
VENSTERBREEDTE = 400
VENSTERHOOGTE = 400
vensterOppervlak = pygame.display.set_mode((VENSTERBREEDTE, VENSTERHOOGTE), 0, 32)
pygame.display.set_caption('Input')

# set up the colors
ZWART = (0, 0, 0)
GROEN = (0, 255, 0)
WIT = (255, 255, 255)

# set up the speler and food data structure
voedselTeller = 0
NIEUWVOEDSEL = 40
VOEDSELGROOTTE = 20
speler = pygame.Rect(300, 100, 50, 50)
voedsel = []
for i in range(20):
    voedsel.append(pygame.Rect(random.randint(0, VENSTERBREEDTE - VOEDSELGROOTTE), random.randint(0, VENSTERHOOGTE - VOEDSELGROOTTE), VOEDSELGROOTTE, VOEDSELGROOTTE))

# set up movement variables
beweegLinks = False
beweegRechts = False
beweegBoven = False
beweegBeneden = False

BEWEEGSNELHEID = 6


# start de spel-lus
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                beweegRechts = False
                beweegLinks = True
            if event.key == K_RIGHT or event.key == ord('d'):
                beweegLinks = False
                beweegRechts = True
            if event.key == K_UP or event.key == ord('w'):
                beweegBeneden = False
                beweegBoven = True
            if event.key == K_DOWN or event.key == ord('s'):
                beweegBoven = False
                beweegBeneden = True
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
                beweegBeneden = False
            if event.key == ord('x'):
                speler.top = random.randint(0, VENSTERHOOGTE - speler.height)
                speler.left = random.randint(0, VENSTERBREEDTE - speler.width)

        if event.type == MOUSEBUTTONUP:
            voedsel.append(pygame.Rect(event.pos[0], event.pos[1], VOEDSELGROOTTE, VOEDSELGROOTTE))

    voedselTeller += 1
    if voedselTeller >= NIEUWVOEDSEL:
        # voeg nieuw voedsel toe
        voedselTeller = 0
        voedsel.append(pygame.Rect(random.randint(0, VENSTERBREEDTE - VOEDSELGROOTTE), random.randint(0, VENSTERHOOGTE - VOEDSELGROOTTE), VOEDSELGROOTTE, VOEDSELGROOTTE))

    # teken een zwarte achtergrond op het oppervlak
    vensterOppervlak.fill(ZWART)

    # beweeg de speler
    if beweegBeneden and speler.bottom < VENSTERHOOGTE:
        speler.top += BEWEEGSNELHEID
    if beweegBoven and speler.top > 0:
        speler.top -= BEWEEGSNELHEID
    if beweegLinks and speler.left > 0:
        speler.left -= BEWEEGSNELHEID
    if beweegRechts and speler.right < VENSTERBREEDTE:
        speler.right += BEWEEGSNELHEID

    # teken de speler op het oppervlak
    pygame.draw.rect(vensterOppervlak, WIT, speler)

    # controleer of de speler een van de voedsel-vierkanten aanraakt
    for food in voedsel[:]:
        if speler.colliderect(food):
            voedsel.remove(food)

    # teken het voedsel
    for i in range(len(voedsel)):
        pygame.draw.rect(vensterOppervlak, GROEN, voedsel[i])

    # teken het venster op het scherm
    pygame.display.update()
    hoofdKlok.tick(40)
