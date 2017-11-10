# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:24:55 2017

@author: TimMu
"""

import pygame
import random
import math

pygame.init()
pygame.display.set_caption('Flappy Bird @TimMu')
SIZE = WIDTH, HEIGHT = 500, 668
screen= pygame.display.set_mode(SIZE)


game_img = pygame.image.load('atlas.png')  
bg_rect = pygame.Rect(0,0,288,512)  
bg_img = game_img.subsurface(bg_rect).convert()
bg_img = pygame.transform.scale(bg_img, (550,668))  
#config bird  
bird_rect = pygame.Rect(0,970,48,48)  
#bird_pos = [100,230]  
bird_img = game_img.subsurface(bird_rect).convert_alpha() 
bird_img = pygame.transform.scale(bird_img, (70,70))   
#self.bird_width = 70
# self.bird_height = 50
#self.bird = pygame.transform.scale(self.bird, (self.bird_width, self.bird_height))
        
pipe_up_rect = pygame.Rect(110, 640,58,325)
pipe_up_img = game_img.subsurface(pipe_up_rect).convert_alpha()
pipe_down_rect = pygame.Rect(165, 640,58,300)
pipe_down_img = game_img.subsurface(pipe_down_rect).convert_alpha()

logo_rect = pygame.Rect(681, 178,200,50)
logo_img = game_img.subsurface(logo_rect).convert_alpha()

LIGHT_GREY = (100, 100, 100)
LIGHTER_GREY = (200, 200, 200)

clock = pygame.time.Clock()

class FlappyBird:

    def __init__(self):
       
        self.display = pygame.display.set_mode(SIZE)

        self.background = bg_img

        self.logo = logo_img
        self.logo = pygame.transform.scale(self.logo, (430, 110))

        self.font = pygame.font.Font('flappyfont.TTF', 100)
        self.font_x = WIDTH / 2 - 20
        self.font_y = 60

        self.medium_font = pygame.font.Font('flappyfont.TTF', 70)

        self.text_font = pygame.font.Font('flappyfont.TTF', 35)

        self.score = 0
        self.scores = []
        self.max_score = 0

        self.bird = bird_img
        self.bird_width = 70
        self.bird_height = 50
        
        self.bird_rect = self.bird.get_rect()
        self.bird_x = 20
        self.bird_y = HEIGHT / 2

        self.pipes = [pipe_up_img, pipe_down_img]
        self.pipe_dist = 180
        self.pipe_width = 130
        self.pipe_height = 420
        self.pipe_x = WIDTH + self.pipe_width
        self.pipe_speed = 2.5

        self.resize_pipes()

        self.top_py = 0
        self.bottom_py = 0
        self.pipe_ys = [self.top_py, self.bottom_py]

        self.generate_pipe_coords()

        self.top_pipe = self.pipes[0]
        self.bottom_pipe = self.pipes[1]
        self.top_pipe_rect = self.top_pipe.get_rect()
        self.bottom_pipe_rect = self.bottom_pipe.get_rect()

        # Everything related to the physics of the game.
        self.velocity = 0.2
        self.gravity = -5
        self.jump_dist = 1
        self.bird_speed = self.velocity + self.gravity
        #===============================================

        # Button coords.
        self.play_btn_x = 155
        self.play_btn_y = HEIGHT / 2 + 70
        self.play_btn_size = self.place_intr_text(self.font, 'PLAY', self.play_btn_x, self.play_btn_y, LIGHT_GREY, LIGHTER_GREY, return_size=True)

        self.help_btn_x = 190
        self.help_btn_y = HEIGHT / 2 + 180
        self.help_btn_size = self.place_intr_text(self.medium_font, 'HELP', self.help_btn_x, self.help_btn_y, LIGHT_GREY, LIGHTER_GREY, return_size=True)

        self.back_btn_x = 40
        self.back_btn_y = HEIGHT - 100
        self.back_btn_size = self.place_intr_text(self.font, 'BACK', self.back_btn_x, self.back_btn_y, LIGHT_GREY, LIGHTER_GREY, return_size=True)

        self.play2_btn_x = WIDTH - 180
        self.play2_btn_y = HEIGHT - 100
        self.play2_btn_size = self.place_intr_text(self.font, 'PLAY', self.play2_btn_x, self.play2_btn_y, LIGHT_GREY, LIGHTER_GREY, return_size=True)

        self.restart_btn_x = WIDTH / 2 - 195
        self.restart_btn_y = HEIGHT / 2 + 100
        self.restart_btn_size = self.place_intr_text(self.font, 'RESTART', self.restart_btn_x, self.restart_btn_y, LIGHT_GREY, LIGHTER_GREY, return_size=True)

        self.start_scene()

    def game_scene(self):
        
        while True:
            clock.tick(120)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jump()
                    if event.key == pygame.K_p:
                        self.pause_scene()

            self.bird_y += self.bird_speed
            self.bird_speed += self.velocity

            self.place_background()
            self.move_pipes()
            self.place_pipes()
            self.place_score()
            self.place_bird()

            self.has_gone_off_bounds()
            self.has_collided()

    def start_scene(self):
       
        start = True
        while start:
            clock.tick(60)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start = False
                        self.game_scene()
                    if event.key == pygame.K_q:
                        self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.mouse_in_region(self.play_btn_x, self.play_btn_y, self.play_btn_size[0], self.play_btn_size[1]):
                        self.game_scene()
                    if self.mouse_in_region(self.help_btn_x, self.help_btn_y, self.help_btn_size[0], self.help_btn_size[1]):
                        self.help_scene()

            self.place_background()
            self.place_logo()
            self.place_bird(WIDTH / 2 - self.bird_rect.center[0], HEIGHT / 2 - self.bird_rect.center[0])
            self.place_intr_text(self.font, 'PLAY', self.play_btn_x, self.play_btn_y, LIGHT_GREY, LIGHTER_GREY)
            self.place_intr_text(self.medium_font, 'HELP', self.help_btn_x, self.help_btn_y, LIGHT_GREY, LIGHTER_GREY)

    def help_scene(self):
        helping = True

        pause_x = 85
        pause_y = 280

        quit_x = 100
        quit_y = 400
        while helping:
            clock.tick(60)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_scene()
                    if event.key == pygame.K_q:
                        self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.mouse_in_region(self.back_btn_x, self.back_btn_y, self.back_btn_size[0], self.back_btn_size[1]):
                        self.start_scene()
                    if self.mouse_in_region(self.play2_btn_x, self.play2_btn_y, self.play2_btn_size[0], self.play2_btn_size[1]):
                        self.game_scene()

            self.place_background()
            self.place_logo()

            # The Pause text.
            self.place_text('''PRESS 'P' TO PAUSE''', pause_x, pause_y)
            self.place_text('''THE GAME''', pause_x + 82, pause_y + 40)

            # The Quit text.
            self.place_text('''PRESS 'Q' TO QUIT''', quit_x, quit_y)
            self.place_text('''THE GAME''', quit_x + 65, quit_y + 40)

            # Placing the interactive text.
            self.place_intr_text(self.medium_font, 'BACK', self.back_btn_x, self.back_btn_y, LIGHT_GREY, LIGHTER_GREY)
            self.place_intr_text(self.medium_font, 'PLAY', self.play2_btn_x, self.play2_btn_y, LIGHT_GREY, LIGHTER_GREY)

    def pause_scene(self):
        paused = True
        while paused:
            clock.tick(60)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                    if event.key == pygame.K_q:
                        self.quit()

            self.place_text('''PRESS 'SPACE' TO RESUME''', 30, 200)
            self.place_text('''PRESS 'Q' TO QUIT''', 100, 240)

    def game_over(self):
       
        game_over = True
        while game_over:
            clock.tick(60)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_over = False
                        FlappyBird()
                    if event.key == pygame.K_q:
                        self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.mouse_in_region(self.restart_btn_x, self.restart_btn_y, self.restart_btn_size[0], self.restart_btn_size[1]):
                        FlappyBird()

            self.place_background()
            self.place_score()
            self.place_bird(WIDTH / 2 - self.bird_rect.center[0], HEIGHT / 2 - self.bird_rect.center[0])
            # self, given_font, text, x, y, icolor, acolor, return_size=False
            self.place_intr_text(self.font, 'RESTART', self.restart_btn_x, self.restart_btn_y, LIGHT_GREY, LIGHTER_GREY)

    def place_background(self):
       
        self.display.blit(self.background, (0, 0))

    def place_bird(self, x=None, y=None):
       
        if x == None and y == None:
            x = self.bird_x
            y = self.bird_y

        self.display.blit(self.bird, (x, y))

    def place_pipes(self):
       
        self.display.blit(self.pipes[0], (self.pipe_x, self.top_py))
        self.display.blit(self.pipes[1], (self.pipe_x, self.bottom_py))

    def place_score(self):
       
        if self.pipe_x + self.pipe_width == self.bird_x:
            self.score += 1

        self.display.blit(self.font.render(str(self.score), True, LIGHT_GREY), (self.font_x, self.font_y))

    def place_max_score(self):
       
        self.display.blit(self.font.render(str(self.max_score), True, LIGHT_GREY), (self.font_x, self.font_y))

    def place_logo(self):
      
        self.display.blit(self.logo, (35, HEIGHT / 6))

    def place_text(self, text, x, y):
        
        self.display.blit(self.text_font.render(text, True, LIGHT_GREY), (x, y))

    def place_intr_text(self, given_font, text, x, y, icolor, acolor, return_size=False):
        
        mouse = pygame.mouse.get_pos()
        text_size = given_font.size(text)

        if not return_size:
            if x <= mouse[0] <= x + text_size[0] and y <= mouse[1] <= y + text_size[1]:
                self.display.blit(given_font.render(text, True, acolor), (x, y))
            else:
                self.display.blit(given_font.render(text, True, icolor), (x, y))
        else:
            return text_size

    def resize_pipes(self):
       
        self.pipes[0] = pygame.transform.scale(self.pipes[0], (self.pipe_width, self.pipe_height))
        self.pipes[1] = pygame.transform.scale(self.pipes[1], (self.pipe_width, self.pipe_height))

    def move_pipes(self):
       
        self.pipe_x -= self.pipe_speed

        if self.pipe_x + self.pipe_width < 0:
            self.pipe_x = WIDTH + self.pipe_width
            self.generate_pipe_coords()

    def generate_pipe_coords(self):
       
        self.top_py = random.randint(-150, 0)
        self.bottom_py = self.top_py + self.pipe_height + self.pipe_dist

    def mouse_in_region(self, x, y, width, height):
       
        mouse = pygame.mouse.get_pos()
        return x <= mouse[0] <= x + width and y <= mouse[1] <= y + height

    def has_gone_off_bounds(self):
      
        if self.bird_y + self.bird_height >= HEIGHT or self.bird_y <= 0:
            self.restart()

    def jump(self):
       
        self.bird_speed = -self.velocity + self.gravity - self.jump_dist

    def has_collided(self):
       
        if self.pipe_x + self.pipe_width >= self.bird_x + self.bird_width >= self.pipe_x or self.pipe_x <= self.bird_x <= self.pipe_x + self.pipe_width:
            if self.top_py <= self.bird_y <= self.top_py + self.pipe_height or self.bottom_py <= self.bird_y + self.bird_height <= self.bottom_py + self.pipe_height:
                self.restart()

    def restart(self):
   
        with open('scores.txt', 'a') as file_app:
            if not self.score == 0:
                file_app.write(str(self.score) + ',')

            file_app.seek(0)

        with open('scores.txt', 'r') as file_read:
            self.scores = file_read.read().split(',')
            self.scores.remove('')

            try:
                self.max_score = max(self.scores)[0]
            except ValueError:
                self.max_score = 0

            file_read.seek(0)

        self.game_over()

    def quit(self):
        pygame.quit()
        quit()


if __name__ == '__main__':
    FlappyBird()