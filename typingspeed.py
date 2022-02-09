from email import message
from this import d
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
        self.random_sentence = ''
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

    def draw_text(self, screen, message, y, font_size, color):
        font = pygame.font.Font(None, font_size)
        text = font.render(message, color)
        text_rect = text.get_rect(center=(self.width/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        file = open('sentences.txt').read()
        sentences = file.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def reset(self):
        self.screen.blit(self.open_img, (0, 0))
        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.active = False
        self.end = False
        self.input_text = ''
        self.word = ''
        self.start_time = 0
        self.total_time = 0
        self.wpm = 0
        self.random_sentence = self.get_sentence
        if (not self.word):
            self.reset

        self.screen.fill(0, 0, 0)
        self.screen.blit(self.bg, (0, 0))
        message = 'Typing Speed Test'
        self.draw_text(self.screen, message, 80, 80, self.HEAD_C)
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        self.draw_text(self.screen, self.random_sentence, 28, self.TEXT_C)
        pygame.display.update()

    def run(self):  # TODO
        self.reset()
        self.running = True
        while (self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if (x >= 50 and x <= 650 and y >= 250 and y < 350):
                        self.active = True
                        self.input_text = ''
                        self.start_time = time.time()
                    if (x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_stats(self.screen)
                            print(self.stats)
                            self.draw_text(self.screen, self.stats, 350, 28, self.RESULT_C)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            pygame.display.update()
        clock.tick(60)

    def show_stats(self):  # TODO
        print('TODO')
