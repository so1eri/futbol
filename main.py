from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys

import pygame
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('dshajdkwh jkh')

player_rect = pygame.Rect(0, 200, 45, 45)
player_img = pygame.image.load('meeple.png')
player_img = pygame.transform.scale(player_img, (45, 45))

clock = pygame.time.Clock()
while True:
  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if keys[pygame.K_a]:  
        player_rect.x -= 4
    if keys[pygame.K_d]:
           player_rect.x += 4

  screen.fill((250, 250, 250))
  screen.blit(player_img, player_rect)

  
  pygame.display.update()