import pygame, sys, time
from pygame.locals import *

# pygame instellen
pygame.init()

# venster instellen
VENSTERBREEDTE = 400
VENSTERHOOGTE = 400
vensterOppervlak = pygame.display.set_mode((VENSTERBREEDTE, VENSTERHOOGTE), 0, 32)
pygame.display.set_caption('Animatie')

# richtingsvariabelen instellen
LINKSONDER = 1
RECHTSONDER = 3
LINKSBOVEN = 7
RECHTSBOVEN = 9

BEWEEGSNELHEID = 4

# kleuren instellen
ZWART = (0, 0, 0)
ROOD = (255, 0, 0)
GROEN = (0, 255, 0)
BLAUW = (0, 0, 255)

# blok datastructuren instellen
b1 = {'rechthoek':pygame.Rect(300, 80, 50, 100), 'kleur':ROOD, 'richting':RECHTSBOVEN}
b2 = {'rechthoek':pygame.Rect(200, 200, 20, 20), 'kleur':GROEN, 'richting':LINKSBOVEN}
b3 = {'rechthoek':pygame.Rect(100, 150, 60, 60), 'kleur':BLAUW, 'richting':LINKSONDER}
blokken = [b1, b2, b3]

# start de spel-lus
while True:
    # controleer de 'QUIT' gebeurtenis
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # teken een zwarte achtergrond op het oppervlak
    vensterOppervlak.fill(ZWART)

    for b in blokken:
        # move the block data structure
        if b['richting'] == LINKSONDER:
            b['rechthoek'].left -= BEWEEGSNELHEID
            b['rechthoek'].top += BEWEEGSNELHEID
        if b['richting'] == RECHTSONDER:
            b['rechthoek'].left += BEWEEGSNELHEID
            b['rechthoek'].top += BEWEEGSNELHEID
        if b['richting'] == LINKSBOVEN:
            b['rechthoek'].left -= BEWEEGSNELHEID
            b['rechthoek'].top -= BEWEEGSNELHEID
        if b['richting'] == RECHTSBOVEN:
            b['rechthoek'].left += BEWEEGSNELHEID
            b['rechthoek'].top -= BEWEEGSNELHEID

        # check if the block has move out of the window
        if b['rechthoek'].top < 0:
            # block has moved past the top
            if b['richting'] == LINKSBOVEN:
                b['richting'] = LINKSONDER
            if b['richting'] == RECHTSBOVEN:
                b['richting'] = RECHTSONDER
        if b['rechthoek'].bottom > VENSTERHOOGTE:
            # block has moved past the bottom
            if b['richting'] == LINKSONDER:
                b['richting'] = LINKSBOVEN
            if b['richting'] == RECHTSONDER:
                b['richting'] = RECHTSBOVEN
        if b['rechthoek'].left < 0:
            # block has moved past the left side
            if b['richting'] == LINKSONDER:
                b['richting'] = RECHTSONDER
            if b['richting'] == LINKSBOVEN:
                b['richting'] = RECHTSBOVEN
        if b['rechthoek'].right > VENSTERBREEDTE:
            # block has moved past the right side
            if b['richting'] == RECHTSONDER:
                b['richting'] = LINKSONDER
            if b['richting'] == RECHTSBOVEN:
                b['richting'] = LINKSBOVEN

        # draw the block onto the surface
        pygame.draw.rect(vensterOppervlak, b['kleur'], b['rechthoek'])

    # draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)
