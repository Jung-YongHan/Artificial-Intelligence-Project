import pygame

class TextBox:
    def __init__(self, text, x, y, width, height, font, box_color, text_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.box_color = box_color
        self.text_color = text_color

    def draw_text_box(self, screen):
        pygame.draw.rect(screen, self.box_color, (self.x, self.y, self.width, self.height))
        text_box = self.font.render(self.text, True, self.text_color)
        text_rect = text_box.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_box, text_rect)
