import pygame

pygame.init()       # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game v1")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
# background = pygame.image.load("C:\\Users\\3DOS\\Desktop\\Python_Tutorial\\pygame_basic\\background.png")
background = pygame.image.load("C:/Users/3DOS/Desktop/Python_Tutorial/pygame_basic/background.png")

# 스프라이트 (캐릭터) 불러오기
character = pygame.image.load("C:/Users/3DOS/Desktop/Python_Tutorial/pygame_basic/character.png")
character_size = character.get_rect().size      # 캐릭터 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
# 캐릭터를 배경화면 중앙 아래에 위치 시킴
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6
# 이벤트 루프
running = True  # 게임 진행중인 확인
while running:
    dt = clock.tick(60)     # 프레임 수

    # print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():        # 이벤트를 받음
        if event.type == pygame.QUIT:       # 창을 닫는 이벤트일 경우
            running = False         # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed       # 왼쪽으로 5만큼 이동
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:      # 키를 누르지 않으면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # screen.fill((0, 0, 255))        # 파란색으로 배경 이미지 디스플레이 설정
    screen.blit(background, (0, 0))     # 배경 이미지 디스플레이

    screen.blit(character, (character_x_pos, character_y_pos))     # 배경 이미지 디스플레이

    pygame.display.update()         # 배경 이미지를 다시 그리기
# 게임 종료일 경우 종료
pygame.quit()