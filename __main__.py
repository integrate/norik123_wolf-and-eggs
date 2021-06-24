import pygame
from pygame import display,surface,image,event

window=display.set_mode([700,700])
village=image.load("resources/village.jpg")

while True:
    event.get()
    window.blit(village,[0,0])
    display.flip()
