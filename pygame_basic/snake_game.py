import pygame
from random import *

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
snake = pygame.image.load("C:/Users/3DOS/Desktop/Python_Tutorial/pygame_basic/snake.png")
snake_size = snake.get_rect().size      # 캐릭터 이미지의 크기를 구해옴
snake_width = snake_size[0]
snake_height = snake_size[1]
# 캐릭터를 배경화면 오른쪽 아래에 위치 시킴
snake_x_pos = screen_width - snake_width
snake_y_pos = screen_height - snake_height
to_x = 0
to_y = 0

# 이동 속도
snake_speed = 0.2

# 푸드 캐릭터 만들기
food = pygame.image.load("C:/Users/3DOS/Desktop/Python_Tutorial/pygame_basic/food.png")
food_size = food.get_rect().size      # 캐릭터 이미지의 크기를 구해옴
food_width = food_size[0]
food_height = food_size[1]
# 푸드를 랜덤 위치에
food_x_pos = randint(0, screen_width - food_width + 1)
food_y_pos = randint(0, screen_height - food_height + 1)

# 폰트 정의
game_font = pygame.font.Font(None, 40)      # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 60

# 총 점수
total_score = 0

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()       # 시작 tick을 받아옴


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
                to_x -= snake_speed       # 왼쪽으로 이동
            elif event.key == pygame.K_RIGHT:
                to_x += snake_speed
            elif event.key == pygame.K_UP:
                to_y -= snake_speed
            elif event.key == pygame.K_DOWN:
                to_y += snake_speed

        if event.type == pygame.KEYUP:      # 키를 누르지 않으면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

        # 충돌 처리
        snake_rect = snake.get_rect()
        snake_rect.left = snake_x_pos
        snake_rect.top = snake_y_pos

        food_rect = food.get_rect()
        food_rect.left = food_x_pos
        food_rect.top = food_y_pos

        # 충돌 체크
        if snake_rect.colliderect(food_rect):
            # print("충돌했어요.")
            # running = False
            food_x_pos = randint(0, screen_width - food_width + 1)
            food_y_pos = randint(40, screen_height - food_height + 1)
            total_score += 1
            
            
            #screen.blit(food, (food_x_pos, food_y_pos))     # 배경 이미지 디스플레이
        

    snake_x_pos += to_x * dt
    snake_y_pos += to_y * dt

    if snake_x_pos < 0:
        snake_x_pos = 0
    elif snake_x_pos > screen_width - snake_width:
        snake_x_pos = screen_width - snake_width

    if snake_y_pos < 40:
        snake_y_pos = 40
    elif snake_y_pos > screen_height - snake_height:
        snake_y_pos = screen_height - snake_height


    # screen.fill((0, 0, 255))        # 파란색으로 배경 이미지 디스플레이 설정
    screen.blit(background, (0, 0))     # 배경 이미지 디스플레이

    screen.blit(snake, (snake_x_pos, snake_y_pos))     # 배경 이미지 디스플레이
    screen.blit(food, (food_x_pos, food_y_pos))     # 배경 이미지 디스플레이
    
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render("TIME : " + str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    score = game_font.render("SCORE : " + str(int(total_score)), True, (255, 255, 255))
    screen.blit(score, (300, 10))

    pygame.display.update()         # 배경 이미지를 다시 그리기

    if total_time - elapsed_time <= 0:
        screen.blit(background, (0, 0))
        game_over_font = pygame.font.Font(None, 60)      # 폰트 객체 생성 (폰트, 크기)
        game_over = game_over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over, (screen_width/2 - 150, screen_height/2 - 50))
        score_over = game_over_font.render("TOTAL SCORE : " + str(total_score), True, (255, 0, 0))
        screen.blit(score_over, (screen_width/2 - 150, screen_height/2 + 50))
        pygame.display.update()
        running = False
    
# 게임 종료일 경우 종료
# 잠시 대기
pygame.time.delay(5000)         # 5초 딜레이
pygame.quit()