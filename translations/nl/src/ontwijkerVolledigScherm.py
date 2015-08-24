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

# set up pygame, the window, and the mouse cursor
pygame.init()
hoofdKlok = pygame.time.Clock()
vensterOppervlak = pygame.display.set_mode((VENSTERBREEDTE, VENSTERHOOGTE), pygame.FULLSCREEN)
pygame.display.set_caption('Ontwijker')
pygame.mouse.set_visible(False)

# set up lettertype
lettertype = pygame.font.SysFont(None, 48)

# set up sounds
spelVoorbijGeluid = pygame.mixer.Sound('spelvoorbij.wav')
pygame.mixer.music.load('achtergrond.mid')

# set up images
spelerAfbeelding = pygame.image.load('speler.png')
spelerRechthoek = spelerAfbeelding.get_rect()
slechterikAfbeelding = pygame.image.load('slechterik.png')

# show the "Start" screen
tekenTekst('Ontwijker', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3), (VENSTERHOOGTE / 3))
tekenTekst('Druk op een toets om te beginnen.', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3) - 30, (VENSTERHOOGTE / 3) + 50)
pygame.display.update()
wachtToSpelerToetsIndrukt()


besteScore = 0
while True:
    # set up the start of the game
    slechteriken = []
    score = 0
    spelerRechthoek.topleft = (VENSTERBREEDTE / 2, VENSTERHOOGTE - 50)
    beweegLinks = beweegRechts = beweegBoven = beweegOnder = False
    valsspelenOmgekeerd = valsspelenTraag = False
    slechterikTeller = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # the game loop runs while the game part is playing
        score += 1 # increase score

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
                # If the mouse moves, move the speler where the cursor is.
                spelerRechthoek.move_ip(event.pos[0] - spelerRechthoek.centerx, event.pos[1] - spelerRechthoek.centery)

        # Add new slechteriken at the top of the screen, if needed.
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

        # Move the speler around.
        if beweegLinks and spelerRechthoek.left > 0:
            spelerRechthoek.move_ip(-1 * SPELERVERPLAATSSNELHEID, 0)
        if beweegRechts and spelerRechthoek.right < VENSTERBREEDTE:
            spelerRechthoek.move_ip(SPELERVERPLAATSSNELHEID, 0)
        if beweegBoven and spelerRechthoek.top > 0:
            spelerRechthoek.move_ip(0, -1 * SPELERVERPLAATSSNELHEID)
        if beweegOnder and spelerRechthoek.bottom < VENSTERHOOGTE:
            spelerRechthoek.move_ip(0, SPELERVERPLAATSSNELHEID)

        # Move the mouse cursor to match the speler.
        pygame.mouse.set_pos(spelerRechthoek.centerx, spelerRechthoek.centery)

        # Move the slechteriken down.
        for s in slechteriken:
            if not valsspelenOmgekeerd and not valsspelenTraag:
                s['rechthoek'].move_ip(0, s['snelheid'])
            elif valsspelenOmgekeerd:
                s['rechthoek'].move_ip(0, -5)
            elif valsspelenTraag:
                s['rechthoek'].move_ip(0, 1)

        # Delete slechteriken that have fallen past the bottom.
        for s in slechteriken[:]:
            if s['rechthoek'].top > VENSTERHOOGTE:
                slechteriken.remove(s)

        # Draw the game world on the window.
        vensterOppervlak.fill(ACHTERGRONDKLEUR)

        # Draw the score and top score.
        tekenTekst('Score: %s' % (score), lettertype, vensterOppervlak, 10, 0)
        tekenTekst('Top Score: %s' % (besteScore), lettertype, vensterOppervlak, 10, 40)

        # Draw the speler's rectangle
        vensterOppervlak.blit(spelerAfbeelding, spelerRechthoek)

        # Draw each baddie
        for s in slechteriken:
            vensterOppervlak.blit(s['oppervlak'], s['rechthoek'])

        pygame.display.update()

        # Check if any of the slechteriken have hit the speler.
        if spelerRaaktSlechterik(spelerRechthoek, slechteriken):
            if score > besteScore:
                besteScore = score # set new top score
            break

        hoofdKlok.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    spelVoorbijGeluid.play()

    tekenTekst('GAME OVER', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3), (VENSTERHOOGTE / 3))
    tekenTekst('Druk op een toets om opnieuw te spelen.', lettertype, vensterOppervlak, (VENSTERBREEDTE / 3) - 80, (VENSTERHOOGTE / 3) + 50)
    pygame.display.update()
    wachtToSpelerToetsIndrukt()

    spelVoorbijGeluid.stop()
