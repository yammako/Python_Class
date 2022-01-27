import pygame

pygame.init()       # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game v1")

# 이벤트 루프
running = True  # 게임 진행중인 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 창을 닫는 이벤트일 경우
            running = False         # 게임이 진행중이 아님

# 게임 종료일 경우 종료
pygame.quit()