# Імпорт Pygame
import pygame

# Визначення кольорів
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Black = (0, 0, 0)

# Запуск Pygame, створення вікна
pygame.init()
Window = pygame.display.set_mode((600, 400))
Window.fill(Green)

# Цикл подій
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Малювання кола
    Circle = pygame.draw.circle(Window, Red, (300, 200), 100)
    pygame.draw.rect(Window, Blue, (100, 50, 400, 100))
    pygame.draw.ellipse(Window, Yellow, (100, 250, 400, 100), 3)
    pygame.draw.line(Window, Black, (50, 50), (550, 350), 5)
    pygame.display.update()

# Завершення Pygame
pygame.quit()
