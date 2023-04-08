# Імпорт Pygame
import pygame

# Запуск Pygame, створення вікна
pygame.init()
pygame.display.set_mode((600, 400))

# Цикл подій
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершення Pygame
pygame.quit()
