import pygame, sys
from pygame.locals import *

# Voorbereiding pygame
pygame.init()

# Voorbereiding venster
vensterOppervlak = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# Voorbereiding kleuren
ZWART = (0, 0, 0)
WIT = (255, 255, 255)
ROOD = (255, 0, 0)
GROEN = (0, 255, 0)
BLAUW = (0, 0, 255)

# Voorbereiding lettertype
basisLettertype = pygame.font.SysFont(None, 48)

# Voorbereiden tekst
tekst = basisLettertype.render('Hello world!', True, WIT, BLAUW)
tekstRechthoek = tekst.get_rect()
tekstRechthoek.centerx = vensterOppervlak.get_rect().centerx
tekstRechthoek.centery = vensterOppervlak.get_rect().centery

# Teken witte achtergrond op het oppervlak
vensterOppervlak.fill(WIT)

# teken een groene polygon op het oppervlak
pygame.draw.polygon(vensterOppervlak, GROEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# teken enkele blauwe lijnen op het oppervlak
pygame.draw.line(vensterOppervlak, BLAUW, (60, 60), (120, 60), 4)
pygame.draw.line(vensterOppervlak, BLAUW, (120, 60), (60, 120))
pygame.draw.line(vensterOppervlak, BLAUW, (60, 120), (120, 120), 4)

# teken een blauwe cirkel op het oppervlak
pygame.draw.circle(vensterOppervlak, BLAUW, (300, 50), 20, 0)

# teken een rode ovaal (ellips) op het oppervlak
pygame.draw.ellipse(vensterOppervlak, ROOD, (300, 250, 40, 80), 1)

# teken de achtergrond-rechthoek voor de tekst op het oppervlak
pygame.draw.rect(vensterOppervlak, ROOD, (tekstRechthoek.left - 20, tekstRechthoek.top - 20, tekstRechthoek.width + 40, tekstRechthoek.height + 40))

# haal een pixel-array op van het venster oppervlak
pixArray = pygame.PixelArray(vensterOppervlak)
pixArray[480][380] = ZWART
del pixArray

# teken de tekst op het oppervlak
vensterOppervlak.blit(tekst, tekstRechthoek)

# teken het oppervlak op het scherm
pygame.display.update()

# start de spel-lus
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
