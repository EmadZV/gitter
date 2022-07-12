from email.mime import image
from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
import time
import pygame
import random

from pygame.locals import (
    K_w as w,
    K_a as a,
    K_s as s,
    K_d as d,
    K_l as l,
    K_LSHIFT as shift,
    K_ESCAPE as esc,
    KEYDOWN,
    QUIT,
)


#استارت گیمو بزنیم
pygame.init()


#screen asli
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

#clocke bazi
clock = pygame.time.Clock()

#tarif rang ha
green = (0, 255, 0)
red = (213, 50, 80)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (50, 153, 213)

#tarif rang baraye har chi , baraye daste bandi behtar
snakecolor = green
screencolor = black
losecolor = red
foodcolor = white


#font matnaye to bazi
font_style = pygame.font.SysFont("bahnschrift", 15)
score_font = pygame.font.SysFont("comicsansms", 25)

#function baraye call kardan neveshtan matn ro safe
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/2, screen_height/2])
def scoreshow(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [20, 20])

#function baraye list shodan o deraz shodan maar
def snake (snake_block, snake_list):


    for x in snake_list :
        kalex , kaley = 200, 25
        # if len(x) > 0 :
        #     kale = pygame.image.load("kalemar.png")
        #     kale = pygame.transform.rotate(kale, 90)
        #     screen.blit(kale, (x[0],x[1]))

        badan = pygame.image.load("badanmaar.png")

        screen.blit(badan, (x[0],x[1]))


def gameloop() :
    global kale
    kale = pygame.image.load("kalemar.png")

    running = True
    gameover = False

    #az vasat safe shoro shan
    xplace = screen_height/2
    yplace = screen_width/2

    xchange = 0
    ychange = 0

    #spec haye mohem maar
    snake_block=10
    snake_speed=15

    snakelist = []
    snakelen = 1

    sc, dc, wc, ac = 0, 0, 0, 0

    #tarif abaad qaza
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0

    global last_event

    last_event = 0

    while running: #لوپ اصلی بازی

        while gameover :

            screen.fill(blue)
            message("bakhti! L bezan dobare berim.", red)

            pygame.display.update()

            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == l:
                        gameloop()
                    if event.key == esc : #اتمام بازی با دکمه اسکیپ
                        running = False
                        gameover = False
                elif event.type == QUIT : #اتمام بازی با دکمه بالای برنامه
                    running = False
                    gameover = False
        #تشخیص ایونت
        for event in pygame.event.get() :
            print (event)

            if event.type == KEYDOWN : #تشخیص ورودی کیبوردی از کاربر

                if event.key == shift :
                    snake_speed += 15

                if event.key == w and last_event != s :
                    # if sc == 1 :
                    #     event.key == d
                    #     pass
                    xchange = 0
                    ychange = -snake_block
                    # wc = 1
                    # return wc
                    kale = pygame.image.load("kalemar.png")

                    kale = pygame.transform.rotate(kale, 90)

                if event.key == a and last_event != d :
                    xchange = -snake_block
                    ychange = 0
                    # ac = 1
                    # return ac
                    kale = pygame.image.load("kalemar.png")
                    kale = pygame.transform.rotate(kale, 180)

                    

                if event.key == s and last_event != w:
                    xchange = 0
                    ychange = snake_block
                    # sc = 1
                    # return sc
                    kale = pygame.image.load("kalemar.png")

                    kale = pygame.transform.rotate(kale, -90)

                if event.key == d and last_event != a :
                    xchange = snake_block
                    ychange = 0
                    # dc = 1
                    # return dc
                    kale = pygame.image.load("kalemar.png")

                    kale = pygame.transform.rotate(kale, 0)


                last_event =  event.key

                if event.key == esc : #اتمام بازی با دکمه اسکیپ
                    running = False
            elif event.type == QUIT : #اتمام بازی با دکمه بالای برنامه
                running = False

            elif event.type == pygame.KEYUP :
                if event.key == shift :
                    snake_speed -= 15

        if xplace >= screen_width or xplace < 0 or yplace >= screen_height or yplace < 0:
            xchange = 0
            gameover = True

        xplace += xchange
        yplace += ychange

        screen.fill (yellow)

        #qaza print

        foodimg = pygame.image.load("sib.png")

        rectfood = pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])

        screen.blit(foodimg, rectfood)
        snakehead = []
        snakehead.append(xplace)
        snakehead.append(yplace)




        snakelist.append(snakehead)
        if len(snakelist) > snakelen :
            del snakelist[0]

        #age saresh bokhore khodesh mimire
        for x in snakelist[:-1] :
            if x == snakehead :
                gameover = True


        snake(snake_block , snakelist)

        rectkale = pygame.draw.rect(screen, white, [xplace, yplace, snake_block, snake_block])
        screen.blit(kale, rectkale)

        scoreshow(f"your score : {str(snakelen)}", red)
        pygame.display.update()

        if xplace == foodx and yplace == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snakelen += 1

        clock.tick(snake_speed)




    pygame.quit()
    quit()

gameloop()













