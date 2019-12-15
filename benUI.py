import pygame

BUTTON_TEXT_PADDING = 10


class Button:

    def __init__(self, text, font, bg_colour, position):
        self.font = font
        self.text = text
        self.bg_colour = bg_colour
        self.x = position[0]
        self.y = position[1]
        self.draw_text = self.font.render(self.text, 1, (50, 50, 50))
        self.bg_rect = pygame.rect.Rect((self.x, self.y), (2 * BUTTON_TEXT_PADDING + self.draw_text.get_width(), 2 * BUTTON_TEXT_PADDING+ self.draw_text.get_height()))

    def draw(self, win):
        pygame.draw.rect(win, self.bg_colour, self.bg_rect)
        win.blit(self.draw_text, (self.x + BUTTON_TEXT_PADDING, self.y + BUTTON_TEXT_PADDING))

    def clicked(self, mouse_x, mouse_y):
        return self.bg_rect.collidepoint(mouse_x, mouse_y)
