import argparse
import pygame
import random
from utils import *
import time

from GUIObjects.RadioButton import RadioButton
from GUIObjects.Button import Button
from GUIObjects.TextBox import TextBox

# 윈도우 크기, 그리드 월드 크기
window_size = (750, 750)
grid_world_size = (600, 600)

# 사용할 색 지정
black = (0, 0, 0)
white = (255, 255, 255)
gray = (220, 220, 220)
dark_gray = (128, 128, 128)
light_blue = (75, 137, 220)
blue = (0, 0, 255)
red = (255, 0, 0)

# 사용할 폰트
pygame.font.init()
font1 = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 20)

# Button
################################################################################
# 버튼 속성
button_width = 150
button_height = 60
button_margin = 20

# 버튼 문자
button_text = ["Start A* Search", "Random walls", "Reset"]

# 버튼 위치
buttons_x = [button_margin*(i+1) + button_width*(i) + 30 for i in range(3)]
################################################################################

# Text
################################################################################
# 텍스트 상자 속성
text_box_width = 50
text_box_height = 20

# 텍스트 문자
text_box_text = "Heuristic"

# 텍스트 상자 위치
text_box_x = 580
text_box_y = 20
################################################################################

# Radio Button
################################################################################
# 라디오 버튼 속성
radio_button_width = 2
radio_button_radius = 6

# 라디오 버튼 문자
radio_button_text = ["Manhattan", "Euclidean"]

# 라디오 버튼 위치
radio_button_x = text_box_x + 10
radio_button_y = text_box_y + 20
#################################################################################

# 버튼 정의
basic_buttons = [Button(button_text[i], buttons_x[i], button_margin, button_width, button_height,
                        font1, light_blue, white) for i in range(3)]
# 텍스트 상자 정의
text_box = TextBox(text_box_text, text_box_x, text_box_y, text_box_width, text_box_height, font1, white, black)

# 라디오 버튼 정의
radio_buttons = [RadioButton(radio_button_text[i], radio_button_x, radio_button_y+20*i+15, radio_button_width,
                             font2, black, black, radio_button_radius, i) for i in range(2)]

def selected_heuristic():
    for button in radio_buttons:
        if button.selected:
            if button.text == "Manhattan":
                return 0
            elif button.text == "Euclidean":
                return 1

def draw_world(M, N, inc_obstacle_ratio):
    pygame.init()

    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Find a shortest path with A* Algorithm!")

    grid_world = [['O' for _ in range(N)] for _ in range(M)]
    ###### 그리드 만들어서 장애물, 시작, 도착지점 구현하기

    # 그리드 셀 크기 계산
    cell_width = grid_world_size[0] // M
    cell_height = grid_world_size[1] // N

    # 라디오 버튼 기본 설정
    radio_buttons[0].selected = True

    # 드래그 상태 기본 설정
    drag_start = False
    drag_goal = False

    # 시작, 도착 위치
    start, goal = generate_start_goal(M, N, grid_world)

    # 시작, 도착값 변환을 위한 변수
    prev_start = start
    prev_goal = goal

    # 경로 및 탐색 노드 개수
    path = []
    explored_node = 0

    # 선이 그려진 경우, 경로 알고리즘 실행한 경우
    lines = []
    line_finished = False
    astar_start = False
    print_result = None

    # game loop
    running = True
    while running:

        screen.fill(white)

        # 버튼
        for i in range(3):
            basic_buttons[i].draw_button(screen)
        # 텍스트 상자
        text_box.draw_text_box(screen)
        # 라디오 버튼
        for i in range(2):
            radio_buttons[i].draw_radio_button(screen)

        # Grid World
        for row in range(M):
            for col in range(N):
                pygame.draw.rect(screen, black,
                                 (75 + (col * cell_width), 100 + (row * cell_height), cell_width, cell_height), 1)

        # 장애물 개수
        obstacle_count_text = font1.render(f"Obstacles: {count_obstacles(grid_world)}", True, black)
        screen.blit(obstacle_count_text, (window_size[0] - 150, window_size[1] - 35))

        # 시작, 도착 박스
        start_text_box = TextBox("S", 75 + start[1] * cell_width, 100 + start[0] * cell_height, cell_width, cell_height, font1, blue, white)
        goal_text_box = TextBox("G", 75 + goal[1] * cell_width, 100 + goal[0] * cell_height, cell_width, cell_height, font1, red, white)
        start_text_box.draw_text_box(screen)
        goal_text_box.draw_text_box(screen)

        # 장애물
        for row in range(M):
            for col in range(N):
                if grid_world[row][col] == 'X':
                    pygame.draw.rect(screen, dark_gray,
                                     (75 + (col * cell_width), 100 + (row * cell_height), cell_width, cell_height))
                    pygame.draw.rect(screen, black,
                                     (75 + (col * cell_width), 100 + (row * cell_height), cell_width, cell_height), 1)
                elif grid_world[row][col] == 'O':
                    pygame.draw.rect(screen, black,
                                     (75 + (col * cell_width), 100 + (row * cell_height), cell_width, cell_height), 1)

        # 0.05초 간격 경로 그리기
        if not line_finished and astar_start:
            lines = []
            for i in range(len(path) - 1):
                lines.append(((75 + path[i][1] * cell_width + cell_width // 2,
                               100 + path[i][0] * cell_height + cell_height // 2),
                              (75 + path[i + 1][1] * cell_width + cell_width // 2,
                               100 + path[i + 1][0] * cell_height + cell_height // 2)))
            for line_start, line_end in lines:
                pygame.draw.line(screen, (255, 255, 0), line_start, line_end, 5)
                pygame.time.delay(50)
                pygame.display.flip()
            line_finished = True

        # 경로 유지 및 결과 콘솔 출력
        if line_finished and astar_start:
            for line_start, line_end in lines:
                pygame.draw.line(screen, (255, 255, 0), line_start, line_end, 5)
            if not print_result:
                print_result = True
                if path[-1] == goal:
                    print("Success Finding a Shortes Path!")
                    print(f"Explored nodes : {explored_node}")
                else:
                    print("There are no paths to destination!")
                    print(f"Explored nodes : {explored_node}")

        # events
        for event in pygame.event.get():
            # x 버튼 클릭 시 윈도우 종료
            if event.type == pygame.QUIT:
                running = False

            # 마우스 클릭 이벤트
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 왼쪽 마우스 클릭
                if event.button == 1:

                    # 버튼 Action
                    # 선이 그려진 후 누를 수 있는 버튼은 경로 탐색, 리셋 버튼만 가능
                    if line_finished:

                        if basic_buttons[0].is_clicked(event.pos):
                            path, explored_node = \
                                basic_buttons[0].start_Astar_search(grid_world, start, goal, selected_heuristic())
                            astar_start = True
                            line_finished = False
                            print_result = False
                        if basic_buttons[2].is_clicked(event.pos):
                            astar_start = False
                            line_finished = False
                            print_result = False
                            basic_buttons[2].reset_grid_world(M, N, inc_obstacle_ratio, grid_world)

                        # 라디오 버튼 Action
                        for button in radio_buttons:
                            if button.is_clicked(event.pos):
                                for other_button in radio_buttons:
                                    other_button.selected = False
                                button.selected = True
                    else:
                        if basic_buttons[0].is_clicked(event.pos):
                            path, explored_node = \
                                basic_buttons[0].start_Astar_search(grid_world, start, goal, selected_heuristic())
                            astar_start = True
                        if basic_buttons[1].is_clicked(event.pos):
                            astar_start = False
                            basic_buttons[1].set_randomly_obstacles(grid_world, int(M*N*inc_obstacle_ratio))
                        if basic_buttons[2].is_clicked(event.pos):
                            astar_start = False
                            basic_buttons[2].reset_grid_world(M, N, inc_obstacle_ratio, grid_world)

                        # 라디오 버튼 Action
                        for button in radio_buttons:
                            if button.is_clicked(event.pos):
                                for other_button in radio_buttons:
                                    other_button.selected = False
                                button.selected = True

                        # 드래그 Action
                        pos = pygame.mouse.get_pos()
                        if start_text_box.is_collide_point(pos):
                            drag_start = True
                            offset_x, offset_y = start_text_box.x - pos[0], start_text_box.y - pos[1]
                        if goal_text_box.is_collide_point(pos):
                            drag_goal = True
                            offset_x, offset_y = goal_text_box.x - pos[0], goal_text_box.y - pos[1]

                        # 장애물 Action
                        if is_valid(event.pos[0], event.pos[1], cell_width, cell_height, grid_world):
                            toggle_obstacle(pos, cell_width, cell_height, grid_world)


            if event.type == pygame.MOUSEBUTTONUP:
                drag_start = False
                drag_goal = False

            if event.type == pygame.MOUSEMOTION:
                if drag_start:
                    new_x = event.pos[0] + offset_x
                    new_y = event.pos[1] + offset_y
                    if is_valid_drag(new_x, new_y, cell_width, cell_height, grid_world):
                        grid_world[prev_start[0]][prev_start[1]] = 'O'

                        start_text_box.x = new_x
                        start_text_box.y = new_y
                        start = (start_text_box.y - 100) // cell_height, (start_text_box.x - 75) // cell_width

                        grid_world[start[0]][start[1]] = 'S'
                        prev_start = start

                if drag_goal:
                    new_x = event.pos[0] + offset_x
                    new_y = event.pos[1] + offset_y
                    if is_valid_drag(new_x, new_y, cell_width, cell_height, grid_world):
                        grid_world[prev_goal[0]][prev_goal[1]] = 'O'

                        goal_text_box.x = new_x
                        goal_text_box.y = new_y
                        goal = (goal_text_box.y - 100) // cell_height, (goal_text_box.x - 75) // cell_width

                        grid_world[goal[0]][goal[1]] = 'G'
                        prev_goal = goal

            # 이중 버퍼 활용, 화면 전환
        pygame.display.flip()



    pygame.quit()