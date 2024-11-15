import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x, mole_y = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x * 32 <= mouse_x < (mole_x + 1) * 32 and mole_y * 32 <= mouse_y < (mole_y + 1) * 32:
                        mole_x, mole_y = random.randrange(20), random.randrange(16)

            screen.fill((213, 247, 242))

            for i in range(21):
                pygame.draw.line(screen, "white", (i * 32, 0), (i * 32, 512))
            for j in range(17):
                pygame.draw.line(screen, "white", (0, j * 32), (640, j * 32))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * 32, mole_y * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
