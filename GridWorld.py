import argparse
import pygame
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
light_blue = (75, 137, 220)

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
                             font2, black, black, radio_button_radius) for i in range(2)]

def draw_world(M, N, inc_obstacle_ratio):
    pygame.init()

    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Find a shortest path with A* Algorithm!")

    # 그리드 셀 크기 계산
    cell_width = grid_world_size[0] // M
    cell_height = grid_world_size[1] // N

    # 라디오 버튼 기본 설정
    radio_buttons[0].selected = True

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            # x 버튼 클릭 시 윈도우 종료
            if event.type == pygame.QUIT:
                running = False

            # 마우스 클릭 이벤트
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 왼쪾 마우스 클릭
                if event.button == 1:
                    for button in radio_buttons:
                        if button.is_clicked(event.pos):
                            for other_button in radio_buttons:
                                other_button.selected = False
                            button.selected = True

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
                pygame.draw.rect(screen, black, (75 + (col * cell_width), 100 + (row * cell_height), cell_width, cell_height), 1)

        # 이중 버퍼 활용, 화면 전환
        pygame.display.flip()

    pygame.quit()