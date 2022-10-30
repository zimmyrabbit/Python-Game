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

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get(): # 이벤트 발생 체크
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
                    running = False # 게임이 진행중이 아님

            if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
                if event.key == pygame.K_LEFT: # 왼쪽
                    to_x -= 5
                elif event.key == pygame.K_RIGHT: # 오른쪽  
                    to_x += 5
                elif event.key == pygame.K_UP: # 위
                    to_y -= 5
                elif event.key == pygame.K_DOWN: # 아래
                    to_y += 5
                
            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 가로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        
    #screen.fill((0,0,255)) # RGB값으로 배경 그리기
    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임 화면 다시 그리기

# pygame 종료
pygame.quit()