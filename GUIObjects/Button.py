import pygame

class Button:

    def __init__(self, text, x, y, width, height, font, button_color, text_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.button_color = button_color
        self.text_color = text_color


    def draw_button(self, screen):
        pygame.draw.rect(screen, self.button_color, (self.x, self.y, self.width, self.height))
        button_text = self.font.render(self.text, True, self.text_color)
        text_rect = button_text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(button_text, text_rect)
