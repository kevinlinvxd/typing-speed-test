import pygame
from pygame.locals import *
import sys
import time
import random


class Game:
    def __init__(self):
        self.width = 1000
        self.height = 600
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
        self.open_img = pygame.transform.scale(self.open_img, (self.width, self.height))
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (600, 1000))
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Typing Speed Test')

    def draw_text(self, screen, message, y, font_size, color):
        font = pygame.font.SysFont("trebuchet ms", font_size)
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(self.width / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    @staticmethod
    def get_sentence():
        file = open('sentences.txt').read()
        sentences = file.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def reset_test(self):
        self.screen.blit(self.open_img, (0, 0))
        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.active = False
        self.end = False
        self.input_text = ''
        self.random_sentence = ''
        self.start_time = 0
        self.total_time = 0
        self.wpm = 0
        self.random_sentence = self.get_sentence()
        if not self.random_sentence:
            self.reset_test()

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        message = 'Typing Speed Test'
        self.draw_text(self.screen, message, 80, 80, self.HEAD_C)
        pygame.draw.rect(self.screen, (255, 192, 25), (60, 250, 900, 50), 2)
        self.draw_text(self.screen, self.random_sentence, 200, 28, self.TEXT_C)
        pygame.display.update()

    def run(self):
        self.reset_test()
        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (60, 250, 900, 50), 2)
            self.draw_text(self.screen, self.input_text, 274, 28, self.TEXT_C)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 650 and 250 <= y < 350:
                        self.active = True
                        self.input_text = ''
                        self.start_time = time.time()
                    if 310 <= x <= 510 and y >= 390 and self.end:
                        self.reset_test()
                        x, y = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_stats(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                                # if self.screen.get_width() > 880:
                                #   self.input_text = self.input_text[:-1]
                            except:
                                pass
            pygame.display.update()
        clock.tick(60)

    def show_stats(self, screen):
        if not self.end:
            self.total_time = time.time() - self.start_time

            count = 0
            for i, c in enumerate(self.random_sentence):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.random_sentence) * 100
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time:' + str(round(self.total_time)) + ' secs   Accuracy:' + str(
                round(self.accuracy)) + '%' + '   WPM: ' + str(round(self.wpm))

            self.time_img = pygame.image.load('refresh-svgrepo-com.svg')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            screen.blit(self.time_img, (self.width / 2 - 75, self.height - 140))
            self.draw_text(screen, 'Reset', self.height - 70, 26, (100, 100, 100))
            pygame.display.update()


Game().run()
