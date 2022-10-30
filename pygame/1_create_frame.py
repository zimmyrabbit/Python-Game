import pygame

# pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pyGame")

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get(): # 이벤트 발생 체크
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
                    running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()
