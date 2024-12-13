import pygame, sys, random
from pygame.examples.scrap_clipboard import screen

from game import Game
from menu import Menu
from levelManager import LevelManager

# Khởi tạo pygame và pygame.mixer
pygame.init()
pygame.mixer.init()
 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
OFFSET = 50

GREY = (29, 29, 27)  
YELLOW = (243, 216, 63)

# Tải hình ảnh nền
background_image = pygame.image.load("Graphics/backgroud.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))


pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
menu = Menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

def display_ui():
    # UI elements (Score, Highscore, Lives)
    game.draw_text(screen, 40, "SCORE", 50, 15, 50, 50, YELLOW)
    formatted_score = str(game.score).zfill(5)
    game.draw_text(screen, 40, str(formatted_score), 50, 40, 50, 50, YELLOW)

    game.draw_text(screen, 40, "HIGH-SCORE", 1050, 15, 50, 50, YELLOW)
    formatted_highscore = str(game.highscore).zfill(5)
    game.draw_text(screen, 40, str(formatted_highscore), 1120, 40, 50, 50, YELLOW)

    game.draw_text(screen, 40, f"LEVEL: {game.level_manager.current_level}", 600, 15, 50, 50, YELLOW)

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50


def handle_game_events(event):
    if event.type == SHOOT_LASER and game.run:
        game.alien_shoot_laser()
    if event.type == MYSTERYSHIP and game.run:
        game.create_mystery_ship()
        pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))


def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:  # Quay lại menu bằng phím ESC
        game.toggle_menu()


while True:
    # Kiểm tra các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game.menu_run:  # Khi đang ở trong menu
            selection = menu.handle_input(event)
            if selection == "NEW GAME":
                game.reset()  # Reset game khi bắt đầu trò chơi mới
                game.toggle_menu()
            elif selection == "RESUME" and game.saved_state:
                game.toggle_menu()
            elif selection == "EXIT":
                pygame.quit()
                sys.exit()
        elif game.run:  # Khi đang chạy trò chơi
            handle_game_events(event)
            handle_input()

    if game.menu_run:
        screen.fill(GREY)  # Màu nền menu
        menu.draw()  # Vẽ menu
        pygame.mixer.music.pause()  # Tạm dừng nhạc game
    else:
        pygame.mixer.music.unpause()  # Tiếp tục nhạc game
        screen.blit(background_image,(0,0)) # Màu nền game
        pygame.draw.rect(screen, YELLOW, (10, 10, 1230, 780), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(screen, YELLOW, (25, 730), (1225, 730), 3)
        if game.run:
            # Cập nhật và vẽ các đối tượng trong game
            game.spaceship_group.update()
            game.move_aliens()
            game.alien_lasers_group.update()
            game.mystery_ship_group.update()
            game.check_for_collisions()
            display_ui()
            # Vẽ các nhóm sprite
            game.spaceship_group.draw(screen)
            game.spaceship_group.sprite.lasers_group.draw(screen)
            for obstacle in game.obstacles:
                obstacle.blocks_group.draw(screen)
            game.aliens_group.draw(screen)
            game.alien_lasers_group.draw(screen)
            game.mystery_ship_group.draw(screen)
        else:
            # Game over screen
            game.draw_text(screen, 40, "GAME OVER", 570, 740, 50, 50, YELLOW)

    pygame.display.update()
    clock.tick(40)
