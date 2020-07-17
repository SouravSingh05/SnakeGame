import pygame
import random
pygame.init()  # initialising the components of pygame
window = pygame.display.set_mode((500, 500))  # creating game window
pygame.display.set_caption("Snakes")  # adding caption
pygame.display.update()
# game variable starts
font = pygame.font.SysFont(None, 55)  # selecting the font
fps = 30
clock = pygame.time.Clock()
with open("highscore.txt", "r") as f:
    hi = f.read()
high = hi
def show(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, (x, y))


def game():
    exit = False  # game will close when it is true
    over = False  # game will be over when it is true
    white = (255, 255, 255)  # defining colors
    red = (255, 0, 0)
    black = (0, 0, 0)
    snake_x = 250
    snake_y = 250
    snake_length = 15
    snake_breadth = 15

    vel = 3
    k = 0
    j = 0
    food_x = random.randint(10, 480)
    food_y = random.randint(10, 480)
    food_size = random.randint(8, 15)
    score = 0

    snake_list = []
    snake_len = 1
    flag = 0

    while not exit:  # creating game loop
        for event in pygame.event.get():  # capturing the events of mouse and keyboard
            if event.type == pygame.QUIT:  # comapring event
                exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j = k
                    k = 1
                if event.key == pygame.K_LEFT:
                    j = k
                    k = 2
                if event.key == pygame.K_UP:
                    j = k
                    k = 3
                if event.key == pygame.K_DOWN:
                    j = k
                    k = 4
        if k == 1:
            if j != 2:
                snake_x = snake_x + vel
            else:
                snake_x = snake_x - vel
                k = 2
        if k == 2:
            if j != 1:
                snake_x = snake_x - vel
            else:
                snake_x = snake_x + vel
                k = 1
        if k == 3:
            if j != 4:
                snake_y = snake_y - vel
            else:
                snake_y = snake_y + vel
                k = 4
        if k == 4:
            if j != 3:
                snake_y = snake_y + vel
            else:
                snake_y = snake_y - vel
                k = 3
        window.fill(white)  # filling window with white color
        show(("Score: " + str(score))+"  High Score: "+str(high), red, 5, 5)
        if snake_x<0 or snake_x>500:
            show("Game Over", red, 150, 150)
            show("Press Space to continue", red, 10, 200)
            show("Press Esc to exit", red, 50, 250)
            flag = 1
            if score>int(high):
                with open("highscore.txt", "w") as f:
                    f.write(str(score))
            pygame.event.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                if event.key == pygame.K_ESCAPE:
                    exit = True
        if snake_y<0 or snake_y>500:
            show("Game Over", red, 150, 150)
            show("Press Spcae to continue", red, 10, 200)
            show("Press Esc to exit", red, 50, 250)
            flag = 1
            if score>int(high):
                with open("highscore.txt", "w") as f:
                    f.write(str(score))
            pygame.event.get()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game()
                    if event.key == pygame.K_ESCAPE:
                        exit = True
        if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
            snake_len = snake_len + 5
            score = score + 10
            food_x = random.randint(10, 480)
            food_y = random.randint(10, 480)
            food_size = random.randint(8, 15)
        if flag == 0:
            head = [snake_x, snake_y]
            snake_list.append(head)
        if len(snake_list)>snake_len:
            del snake_list[0]
        for snake_x, snake_y in snake_list:
            pygame.draw.rect(window, black, [snake_x, snake_y, snake_length, snake_breadth])
            # creating the head of the snake
        pygame.draw.rect(window, red, [food_x, food_y, food_size, food_size])
        if head in snake_list[:-1]:
            show("Game Over", red, 150, 150)
            show("Press Spcae to continue", red, 10, 200)
            show("Press Esc to exit", red, 50, 250)
            flag = 1
            if score>int(high):
                with open("highscore.txt", "w") as f:
                    f.write(str(score))
            pygame.event.get()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game()
                    if event.key == pygame.K_ESCAPE:
                        exit = True
        pygame.display.update()
        clock.tick(fps)  # number of frames per second
    pygame.quit()
    quit()
game()
