from turtle import back
import pygame

# pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pyGame")

# 배경 이미지 불러오기
background = pygame.image.load("D:\\sourceTree\\Python Game\\pygame\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("D:\\sourceTree\\Python Game\\pygame\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하도록 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get(): # 이벤트 발생 체크
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
                    running = False # 게임이 진행중이 아님
    
    #screen.fill((0,0,255)) # RGB값으로 배경 그리기
    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임 화면 다시 그리기

# pygame 종료
pygame.quit()