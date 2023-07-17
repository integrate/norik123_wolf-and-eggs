import pygame, random, time
from pygame import display, surface, image, event, draw,transform,font,rect,key,mouse
from random import randint, choices, choice
from time import sleep
pygame.init()
import model

q=pygame.event.custom_type()
pygame.time.set_timer(q,3000)


def process_events():
    for a in event.get():

        if a.type==q:
            model.create_eggs()

        if a.type==pygame.KEYDOWN:
            if a.key==pygame.K_LEFT:
                model.step_left()

            elif a.key==pygame.K_RIGHT:
                model.step_right()