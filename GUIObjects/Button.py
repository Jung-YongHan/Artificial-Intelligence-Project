import random
import pygame
from utils import generate_start_goal, set_randomly_obstacles, reset_obstacles
from AstartAlgorithm.Astar import Astar

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

    # A* 알고리즘 실행
    def start_Astar_search(self, grid_world, start, end, heuristic_function):
        model = Astar(grid_world, start, end, heuristic_function)
        path, explored_nodes = model.get_path()
        return path, explored_nodes

    # 장애물 랜덤 배치
    def set_randomly_obstacles(self, grid_world, num_obstacles):
        rows, cols = len(grid_world), len(grid_world[0])
        for _ in range(num_obstacles):
            while True:
                row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
                if grid_world[row][col] != 'S' and grid_world[row][col] != 'G' and grid_world[row][col] != 'X':
                    grid_world[row][col] = 'X'
                    break

    # 리셋
    def reset_grid_world(self, M, N, inc_obstacle_ratio, grid_world):
        reset_obstacle(grid_world)
        start, end = generate_start_goal(M, N, grid_world)
        return start, end