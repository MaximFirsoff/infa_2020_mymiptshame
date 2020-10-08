import pygame
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

# И создать окно:
screen = pygame.display.set_mode((500, 500))
screen.fill([125,125,125])
circle(screen, (0, 0, 0), (250, 250), 132)
circle(screen, (255, 255, 0), (250, 250), 130)

circle(screen, (0, 0, 0), (320, 200), 32)
circle(screen, (255, 20, 0), (320, 200), 30)
circle(screen, (0, 0, 0), (320, 200), 12)

circle(screen, (0, 0, 0), (190, 200), 37)
circle(screen, (255, 20, 0), (190, 200), 35)
circle(screen, (0, 0, 0), (190, 200), 22)




pygame.draw.rect(screen, (0, 0, 0), (200, 290, 120, 29))
polygon(screen, (0,0,0),[(150,140),(150,130),(240,175),(240,185)])
polygon(screen, (0,0,0),[(330,150),(330,140),(280,185),(280,195)])





# здесь будут рисоваться фигуры
# ...

# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()