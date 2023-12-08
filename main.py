import pygame
from sys import exit
from random import randint
import asyncio


pygame.init()

# Screen info
clock = pygame.time.Clock()
screen_width = 450
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
pygame.display.set_caption('The Space Race')
test_font = pygame.font.SysFont('Arial', 40)
test_font_2 = pygame.font.SysFont('mangold', 75)
test_font_3 = pygame.font.SysFont('Arial', 40)
game_active = False
score = 0
# Images
background = pygame.image.load('space.jpg')
background_resized = pygame.transform.scale(background, (700, 700))
background_rect = background_resized.get_rect(center=(225, 350))

background_start = pygame.image.load('space.jpg')
background_resized_start = pygame.transform.scale(background, (700, 1000))
background_rect_start = background_resized.get_rect(center=(225, 350))

game_name = test_font_2.render('The space Race', True, 'Gold')
game_rect = game_name.get_rect(center=(225, 100))

game_start_message = test_font.render('press Space to Start', True, 'Gold')
game_start_rect = game_start_message.get_rect(center=(225, 600))

you_win_message = test_font_2.render('You win!', True, 'Gold')
you_win_rect = you_win_message.get_rect(center=(225, 550))

game_hint = test_font_3.render('Try Again if you dare', True, 'Red')
game_hint_rect = game_hint.get_rect(center=(225, 660))


label = pygame.image.load('text_box.png')
label = pygame.transform.scale(label, (160, 100))
label_rect = label.get_rect(center=(225, 75))


# obstacles

player = pygame.image.load('rocket.png')
player_rect_x = 200
player_rect_y = 200
player = pygame.transform.scale(player, (player_rect_x, player_rect_y))
player_rect = player.get_rect(center=(200, 550))

player_stand = pygame.image.load('rocket.png')
player_resized = pygame.transform.scale(player_stand, (350, 350))
player_stand_rect = player_resized.get_rect(center=(250, 400))

meteor = pygame.image.load('asteroid.png')
meteor = pygame.transform.scale(meteor, (150, 170))
meteor_rect = meteor.get_rect(center=(randint(50, 325), 0))

meteor_2 = pygame.image.load('asteroid.png')
meteor_2 = pygame.transform.scale(meteor_2, (150, 170))
meteor_2_rect = meteor_2.get_rect(center=(randint(50, 325), -525))

meteor_stand = pygame.image.load('asteroid.png')
meteor_stand = pygame.transform.scale(meteor_stand, (125, 125))
meteor_stand_rect = meteor_stand.get_rect(center=(85, 350))

meteor_stand_2 = pygame.image.load('asteroid.png')
meteor_stand_2 = pygame.transform.scale(meteor_stand_2, (125, 125))
meteor_stand_2_rect = meteor_stand_2.get_rect(center=(360, 350))

async def main():

    # Loading game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            screen.blit(background_resized_start, background_rect_start)
            screen.blit(player_stand, player_stand_rect)
            screen.blit(game_name, game_rect)
            screen.blit(meteor_stand, meteor_stand_rect)
            screen.blit(meteor_stand_2, meteor_stand_2_rect)
        global game_active
        global score

        if game_active:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_rect.x -= 9
            elif keys[pygame.K_RIGHT]:
                player_rect.x += 9
            # elif keys[pygame.K_UP]:
                # player_rect.y -= 9
            # elif keys[pygame.K_DOWN]:
                # player_rect.y += 9

            # obstacle movement
            meteor_rect.y += 5
            meteor_2_rect.y += 5

            screen.blit(background_resized, background_rect)
            screen.blit(label, label_rect)
            if meteor_rect.top == player_rect.bottom:
                score += 1
            if meteor_2_rect.top == player_rect.bottom:
                score += 1
            score_text = test_font.render(f'{score}', True, 'blue')
            score_rect = score_text.get_rect(center=(225, 75))
            screen.blit(score_text, score_rect)

            if meteor_rect.y > screen_height:
                meteor_rect.x = randint(50, 325)
                meteor_rect.y = -400
            screen.blit(meteor, meteor_rect)
            if meteor_2_rect.y > screen_height:
                meteor_2_rect.x = randint(50, 325)
                meteor_2_rect.y = -400
            screen.blit(meteor_2, meteor_2_rect)
            screen.blit(player, player_rect)

            if player_rect.left < -75:
                player_rect.left = -75
            if player_rect.right > screen_width + 75:
                player_rect.right = screen_width + 75
            if player_rect.top <= 0:
                player_rect.top = 0
            if player_rect.bottom >= screen_height + 75:
                player_rect.bottom = screen_height + 75

            screen_rect = screen.get_rect()

            if player_rect.colliderect(meteor_rect):
                game_active = False

            if player_rect.colliderect(meteor_2_rect):
                game_active = False

        elif game_active == False:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    meteor_rect.y = -200
                    meteor_2_rect.y = -725
                    player_rect.x = 225
                    score = 0

            if score == 0:
                screen.blit(game_start_message, game_start_rect)

        if score == 1000:
            game_active = False
            screen.blit(you_win_message, you_win_rect)

        if score != 0 and score != 1000 and game_active == False:
            score_message = test_font_2.render(f'Your score is {score}', True, 'Gold')
            score_message_rect = score_message.get_rect(center=(225, 600))
            screen.blit(score_message, score_message_rect)
            screen.blit(game_hint, game_hint_rect)






        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())
