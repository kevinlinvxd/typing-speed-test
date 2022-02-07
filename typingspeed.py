import pygame
from pygame.locals import *
import sys
import time
import random


class Game:
    def __init__(self):
        self.width = 750
        self.height = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.start_time = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time: 0 Accuracy: 0% WPM: 0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (250, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('startup.jpg')
        self.open_img = pygame.transform.scale(self.open_img, (self.weight, self.height))
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500, 750))
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Typing Speed Test')
