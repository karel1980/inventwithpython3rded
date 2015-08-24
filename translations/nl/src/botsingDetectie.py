import pygame, sys, random
from pygame.locals import *

def rechthoekenOverlappend(rechthoek1, rechthoek2):
    for a, b in [(rechthoek1, rechthoek2), (rechthoek2, rechthoek1)]:
        # Controleer of een van de hoeken van a in b ligt
        if ((ligtPuntInRechthoek(a.left, a.top, b)) or
            (ligtPuntInRechthoek(a.left, a.bottom, b)) or
            (ligtPuntInRechthoek(a.right, a.top, b)) or
            (ligtPuntInRechthoek(a.right, a.bottom, b))):
            return True

    return False

def ligtPuntInRechthoek(x, y, rechthoek):
    if (x > rechthoek.left) and (x < rechthoek.right) and (y > rechthoek.top) and (y < rechthoek.bottom):
        return True
    else:
        return False


# pygame opzetten
pygame.init()
hoofdKlok = pygame.time.Clock()

# venster opzetten
VENSTERBREEDTE = 400
VENSTERHOOGTE = 400
vensterOppervlak = pygame.display.set_mode((VENSTERBREEDTE, VENSTERHOOGTE), 0, 32)
pygame.display.set_caption('Botsingdetectie')

# richtingvariabelen opzetten
LINKSONDER = 1
RECHTSONDER = 3
LINKSBOVEN = 7
RECHTSBOVEN = 9

BEWEEGSNELHEID = 4

# kleuren opzetten
ZWART = (0, 0, 0)
GROEN = (0, 255, 0)
WIT = (255, 255, 255)

# de kaatser en voetsel datastructuren opzetten
voedselTeller = 0
NIEUWVOEDSEL = 40
VOEDSELGROOTTE = 20
kaatser = {'rechthoek':pygame.Rect(300, 100, 50, 50), 'richting':LINKSBOVEN}
voedsel = []
for i in range(20):
    voedsel.append(pygame.Rect(random.randint(0, VENSTERBREEDTE - VOEDSELGROOTTE), random.randint(0, VENSTERHOOGTE - VOEDSELGROOTTE), VOEDSELGROOTTE, VOEDSELGROOTTE))

# start de spel-lus
while True:
    # controleer de 'QUIT' gebeurtenis
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    voedselTeller += 1
    if voedselTeller >= NIEUWVOEDSEL:
        # voeg nieuw voedsel toe
        voedselTeller = 0
        voedsel.append(pygame.Rect(random.randint(0, VENSTERBREEDTE - VOEDSELGROOTTE), random.randint(0, VENSTERHOOGTE - VOEDSELGROOTTE), VOEDSELGROOTTE, VOEDSELGROOTTE))

    # teken een zwarte achtergrond op het oppervlak
    vensterOppervlak.fill(ZWART)

    # verplaats de kaatser datastructuur
    if kaatser['richting'] == LINKSONDER:
        kaatser['rechthoek'].left -= BEWEEGSNELHEID
        kaatser['rechthoek'].top += BEWEEGSNELHEID
    if kaatser['richting'] == RECHTSONDER:
        kaatser['rechthoek'].left += BEWEEGSNELHEID
        kaatser['rechthoek'].top += BEWEEGSNELHEID
    if kaatser['richting'] == LINKSBOVEN:
        kaatser['rechthoek'].left -= BEWEEGSNELHEID
        kaatser['rechthoek'].top -= BEWEEGSNELHEID
    if kaatser['richting'] == RECHTSBOVEN:
        kaatser['rechthoek'].left += BEWEEGSNELHEID
        kaatser['rechthoek'].top -= BEWEEGSNELHEID

    # controleer of de kaatser zich buiten het venster bewoog
    if kaatser['rechthoek'].top < 0:
        # kaatser ging over de bovenkant
        if kaatser['richting'] == LINKSBOVEN:
            kaatser['richting'] = LINKSONDER
        if kaatser['richting'] == RECHTSBOVEN:
            kaatser['richting'] = RECHTSONDER
    if kaatser['rechthoek'].bottom > VENSTERHOOGTE:
        # kaatser ging over de onderkant
        if kaatser['richting'] == LINKSONDER:
            kaatser['richting'] = LINKSBOVEN
        if kaatser['richting'] == RECHTSONDER:
            kaatser['richting'] = RECHTSBOVEN
    if kaatser['rechthoek'].left < 0:
        # kaatser ging over de linkerkant
        if kaatser['richting'] == LINKSONDER:
            kaatser['richting'] = RECHTSONDER
        if kaatser['richting'] == LINKSBOVEN:
            kaatser['richting'] = RECHTSBOVEN
    if kaatser['rechthoek'].right > VENSTERBREEDTE:
        # kaatser ging over de rechter kant
        if kaatser['richting'] == RECHTSONDER:
            kaatser['richting'] = LINKSONDER
        if kaatser['richting'] == RECHTSBOVEN:
            kaatser['richting'] = LINKSBOVEN

    # teken de kaatser op het oppervlak
    pygame.draw.rect(vensterOppervlak, WIT, kaatser['rechthoek'])

    # controleer of de kaatser overlapt met een van de voetsel vierkanten
    for eten in voedsel[:]:
        if rechthoekenOverlappend(kaatser['rechthoek'], eten):
            voedsel.remove(eten)

    # teken het voedsel
    for i in range(len(voedsel)):
        pygame.draw.rect(vensterOppervlak, GROEN, voedsel[i])

    # teken het venster op het scherm
    pygame.display.update()
    hoofdKlok.tick(40)
