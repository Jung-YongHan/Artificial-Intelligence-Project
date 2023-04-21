import pygame

class RadioButton:
    def __init__(self, text, x, y, width, font, button_color, text_color, radius):
        self.x = x
        self.y = y
        self.width = width
        self.text = text
        self.font = font
        self.button_color = button_color
        self.text_color = text_color
        self.radius = radius
        self.selected = False

    def draw_radio_button(self, screen):
        pygame.draw.circle(screen, self.button_color, (self.x, self.y), self.radius, self.width)
        if self.selected:
            pygame.draw.circle(screen, self.button_color, (self.x, self.y), self.radius // self.width)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x + self.radius * 2, self.y - self.radius // 2)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        distance = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5
        return distance <= self.radius