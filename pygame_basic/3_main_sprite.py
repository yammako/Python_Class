import pygame

pygame.init()       # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game v1")

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

# 이벤트 루프
running = True  # 게임 진행중인 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 창을 닫는 이벤트일 경우
            running = False         # 게임이 진행중이 아님

    # screen.fill((0, 0, 255))        # 파란색으로 배경 이미지 디스플레이 설정
    screen.blit(background, (0, 0))     # 배경 이미지 디스플레이

    screen.blit(character, (character_x_pos, character_y_pos))     # 배경 이미지 디스플레이

    pygame.display.update()         # 배경 이미지를 다시 그리기
# 게임 종료일 경우 종료
pygame.quit()