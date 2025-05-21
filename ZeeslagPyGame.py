import pygame
import sys

# Initialiseer pygame
pygame.init()

# Kleuren
ACHTERGROND_KLEUR = (173, 216, 230)  # Lichtblauw
LIJN_KLEUR = (0, 0, 0)               # Zwart
TEKST_KLEUR = (0, 0, 0)
VAK_GROOTTE = 40
    RAND = 50  # Ruimte voor labels

# Venstergrootte (10 vakken van 40 + randen)
VENSTER_BREEDTE = VAK_GROOTTE * 10 + RAND
VENSTER_HOOGTE = VAK_GROOTTE * 10 + RAND
venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
pygame.display.set_caption("Zeeslagje met Pygame")

# Lettertype
lettertype = pygame.font.SysFont("arial", 20, bold=True)

# Letters voor bovenaan
kolomletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def teken_raster():
    venster.fill(ACHTERGROND_KLEUR)

    # Teken kolomletters
    for i, letter in enumerate(kolomletters):
        tekst = lettertype.render(letter, True, TEKST_KLEUR)
        x = RAND + i * VAK_GROOTTE + VAK_GROOTTE // 2 - tekst.get_width() // 2
        y = RAND // 2 - tekst.get_height() // 2
        venster.blit(tekst, (x, y))

    # Teken rijnummers
    for i in range(10):
        tekst = lettertype.render(str(i), True, TEKST_KLEUR)
        x = RAND // 2 - tekst.get_width() // 2
        y = RAND + i * VAK_GROOTTE + VAK_GROOTTE // 2 - tekst.get_height() // 2
        venster.blit(tekst, (x, y))

    # Teken rasterlijnen
    for i in range(11):  # 11 lijnen = 10 vakken
        # Horizontale lijnen
        start_x = RAND
        start_y = RAND + i * VAK_GROOTTE
        eind_x = RAND + 10 * VAK_GROOTTE
        pygame.draw.line(venster, LIJN_KLEUR, (start_x, start_y), (eind_x, start_y), 2)

        # Verticale lijnen
        start_x = RAND + i * VAK_GROOTTE
        start_y = RAND
        eind_y = RAND + 10 * VAK_GROOTTE
        pygame.draw.line(venster, LIJN_KLEUR, (start_x, start_y), (start_x, eind_y), 2)

def main():
    klok = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teken_raster()
        pygame.display.flip()
        klok.tick(60)  # Maximaal 60 frames per seconde

if __name__ == "__main__":
    main()
