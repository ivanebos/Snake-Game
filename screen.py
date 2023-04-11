import pygame
from food import Food
from snake import Snake

def gameScreen():


    #init
    pygame.init()
    win_size = 600
    block_size = 30
    gap = (win_size-1)/block_size


    black = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)
    green = (0,255,0)

    #set window
    window = pygame.display.set_mode((win_size,win_size))
    pygame.display.set_caption("Snake game")
    clock = pygame.time.Clock()



    food = Food(win_size,block_size)
    snake = Snake(gap,block_size)
    time = 30

    while True:

        if time >= 10:
        #fill window
            window.fill(white)
            pygame.draw.rect(window,red,food.draw())
            
            #draw grid
            for i in range(0,block_size + 1):

                pygame.draw.line(window,black,(i*gap,0),(i*gap,win_size))

            for i in range(0,block_size + 1):

                pygame.draw.line(window,black,(0,i*gap),(win_size,i*gap))
                

            time = 0

            for i in snake.draw():
                pygame.draw.rect(window,green,i)


            snake.update()
        

        #keys hit
        keys = pygame.key.get_pressed()


        if food.posx == snake.chain[0][1] and food.posy == snake.chain[0][0]:
            food.genNewFood()
            snake.grow()
        

        # Player events
        if (keys[pygame.K_d]):
            snake.move_right()
            
        if (keys[pygame.K_a]):
            snake.move_left()

        if (keys[pygame.K_w]):
            snake.move_up()

        if (keys[pygame.K_s]):
            snake.move_down()

        for event in pygame.event.get() : 
            if event.type == pygame.QUIT:
                pygame.quit() 


        #update window
        pygame.display.update() 

        pygame.time.wait(10)
        time += 1
        

        
