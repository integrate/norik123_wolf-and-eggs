import pygame, random, time
from pygame import display, surface, image, event, draw,transform,font,rect,key,mouse
from random import randint, choices, choice
from time import sleep
pygame.init()
import model


window = display.set_mode([1280, 768])

village = image.load("resources/village.jpg")



wolf_right = image.load("resources/wolf-right.png")
wolf_right.set_colorkey([255, 255, 255])

# wolf_left = image.load("resources/wolf-left.png")
# wolf_left.set_colorkey([255, 255, 255])

wolf_left=pygame.transform.flip(wolf_right,True,False)


ckicken1 = image.load("resources/chicken-right.png")
ckicken1.set_colorkey([255, 255, 255])

ckicken2 = image.load("resources/chicken-right.png")
ckicken2.set_colorkey([255, 255, 255])

ckicken3 = image.load("resources/chicken-left.png")
ckicken3.set_colorkey([255, 255, 255])

ckicken4 = image.load("resources/chicken-left.png")
ckicken4.set_colorkey([255, 255, 255])



broken_egg=image.load("resources/broken_egg.png")
broken_egg.set_colorkey([255, 255, 255])



egg_left = image.load("resources/egg-left.png")
egg_left.set_colorkey([255, 255, 255])


egg_right = image.load("resources/egg-right.png")
egg_right.set_colorkey([255, 255, 255])

count_egg_f = font.Font(None, 80)
count_caught_eggs_f = font.Font(None, 80)
count_broken_egg_f = font.Font(None, 80)
stop=font.Font(None,80)

def draw_screen():
    window.blit(village, [0, 0])

    if model.wolf_leftright=="wolf_left":
        a=wolf_left
    if model.wolf_leftright=="wolf_right":
        a=wolf_right

    window.blit(a, [model.wolf_x,model.wolf_y])
    window.blit(ckicken1, [0, 40])
    window.blit(ckicken2, [0, 230])
    window.blit(ckicken3, [879, 40])
    window.blit(ckicken4, [879, 230])
    window.blit(broken_egg, [model.broken_egg_x, 600])

    wer=rect.Rect(426,0,426,100)
    draw.rect(window,[255,0,210],wer,38,8)
    s=surface.Surface([406,80])
    s.fill([255,255,255])
    window.blit(s,[436,10],[0,0,406,80])


    if not model.game_over:
        egggs = count_egg_f.render(str(model.count_egg), True, [255, 217, 8])
        window.blit(egggs, [590, 30])

        eggggs = count_caught_eggs_f.render(str(model.count_caught_eggs), True, [49, 255, 11])
        window.blit(eggggs, [460, 30])

        eggggggs = count_broken_egg_f.render(str(model.count_broken_egg), True, [255, 31, 6])
        window.blit(eggggggs, [730, 30])

    if model.game_over:
        finish=stop.render("Проиграл",True,[255, 31, 6])
        window.blit(finish,[503,30])


    for egg in model.spisok_eggs:
        if egg["egg"]=="egg_left":
            a=egg_left
        if  egg["egg"]=="egg_right":
            a=egg_right

        window.blit(a, [egg["x"], egg["y"]])

    display.flip()

