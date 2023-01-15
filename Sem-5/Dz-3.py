# 40. Создайте программу для игры в ""Крестики-нолики"".

import pygame
import sys

# Указывем количество квадратов и пробелов между ними
pygame.init()
size_block = 100
margin = 15
width = heigth = size_block*3 + margin*4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('ДЗ-3. Крестики-нолики')

# Указывем цвета для использования
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]

query = 0 # 1 2 3 4 5..... для понимания какой игрок ходит четный или нет

# Проверка событий и отрисовка поля 3х3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # если событие - нажатии пробела то выход
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN: # если событие - нажатии мышки то ищем клетку
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
            if query %2 == 0:
                mas[row][col] = 'x' # ставит крестик по найденным координатам (первый игрок)
            else:
                mas[row][col] = 'o' # ставит нолик если игрок 2
            query += 1
    for row in range(3):
        for col in range(3):
            if mas[row][col] == 'x':
                color = red # указываем цвет крестика
            elif mas[row][col] == 'o':
                 color = green
            else:
                color = white # цвет пустого поля
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
    pygame.display.update() 
