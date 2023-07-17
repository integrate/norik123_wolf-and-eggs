import pygame, random, time
from pygame import display, surface, image, event, draw,transform,font,rect,key,mouse
from random import randint, choices, choice
from time import sleep
pygame.init()


# point_left_up_start=[288, 152]
# point_left_up_finish=[367,231]
x1=288
y1=152

# point_left_down_start=[288,342]
# point_left_down_finish=[367,421]
x2=288
y2=342

# point_right_up_start=[944,152]
# point_right_up_finish=[863,233]
x3=944
y3=152

# point_right_down_start=[944,342]
# point_right_down_finish=[863,423]
x4=944
y4=342



spisok_eggs=[]
broken_egg_x=-100

count_egg=0
count_broken_egg=0
count_caught_eggs=0

wolf_x=520
wolf_y=348
wolf_leftright="wolf_left"

game_over=False

def run():
    move_eggs()



def create_eggs():
    global count_egg

    if game_over:
        return

    random_leftright = choice(["egg_left", "egg_right"])

    if random_leftright == "egg_left":
        choice_x = 944
        choice_y = choice([y3, y4])

        vocabulary_x = choice_x
        vocabulary_y = choice_y

    if random_leftright == "egg_right":
        choice_xx = 288
        choice_yy = choice([y1, y2])

        vocabulary_x = choice_xx
        vocabulary_y = choice_yy

    egg_go_to_spisok = {"egg": random_leftright, "x": vocabulary_x, "y": vocabulary_y}
    spisok_eggs.append(egg_go_to_spisok)
    count_egg+=1



def move_eggs():
    global broken_egg_x,count_broken_egg,wolf_x,count_caught_eggs,create_egg_start,game_over
    for egg in spisok_eggs:
        if egg["x"] == 367 or egg["x"] == 863:
            egg["y"] += 1

        else:
            egg["y"] += 1
            if egg["egg"] == "egg_right":
                egg["x"] += 1
            if egg["egg"] == "egg_left":
                egg["x"] -= 1

        if egg["y"]>=420 and egg["y"]<=458:
            if wolf_leftright=="wolf_left" and wolf_x==340 and egg["egg"] == "egg_right"\
                    or wolf_leftright=="wolf_right" and wolf_x==580 and egg["egg"] == "egg_left":
                spisok_eggs.remove(egg)
                count_caught_eggs+=1

        elif egg["y"] >=600:
            broken_egg_x = egg["x"]
            count_broken_egg+=1
            spisok_eggs.remove(egg)
            if count_broken_egg>=5:
                game_over=True




def step_left():
    global wolf_leftright,wolf_x
    wolf_leftright = "wolf_left"
    wolf_x -= 60
    if wolf_x <= 340:
        wolf_x = 340


def step_right():
    global wolf_leftright,wolf_x
    wolf_leftright="wolf_right"
    wolf_x+=60
    if wolf_x >= 580:
        wolf_x = 580