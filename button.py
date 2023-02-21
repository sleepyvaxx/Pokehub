import pygame


# button class
class Button:
    def __init__(self, x, y, image, scale, key_name=None):
        width = image.get_width()
        height = image.get_height()
        font = pygame.font.SysFont("Comic Sans MS", 15, True)

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.text_surface = font.render(key_name, True, (0, 0, 0))
        self.key_name = key_name

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.text_surface, (self.rect.x, self.rect.y))

        return action
