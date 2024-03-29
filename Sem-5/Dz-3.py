# 40. Создайте программу для игры в ""Крестики-нолики"".

import pygame
import sys

# проверка победы
def check_win(mas, sign):
    zeroes = 0  # пустые клетки
    for row in mas:  # проверка победы по линии
        zeroes += row.count(0)
        if row.count(sign)==3:
            return sign
    for col in range(3):  
        if mas[0][col]==sign and mas[1][col]==sign and mas[2][col]==sign: # проверка победы по столбцу
            return sign
    if mas[0][0]==sign and mas[1][1]==sign and mas[2][2]==sign: # проверка победы по главной диагонали
        return sign
    if mas[0][2]==sign and mas[1][1]==sign and mas[2][0]==sign: # проверка победы по второй диагонали
        return sign
    if zeroes==0:
        return 'Ничья!'
    return False

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

query = 0  # для понимания какой игрок ходит четный или нет
game_over = False

while True: # Проверка событий и отрисовка поля 3х3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # если событие - нажатии мышки то ищем клетку
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'  # "ставит" крестик по найденным координатам (первый игрок)
                else:
                    mas[row][col] = 'o'  # "ставит" нолик если игрок 2
                query += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # если событие - нажатии пробела то рестарт
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red  # указываем цвет крестика
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white  # цвет пустого поля
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:  # отрикосовка линий имитрующих крестик
                    pygame.draw.line(screen, white, (x+5, y+5),(x + size_block-5, y + size_block-5), 3) # левый верх -> правый низ клетки
                    pygame.draw.line(screen, white, (x + size_block-5, y+5), (x+5, y + size_block-5), 3) # правый верх -> лез низ клетки
                elif color == green: # отрисовка кружка если цвет зеленый
                    pygame.draw.circle(screen, white, (x+size_block//2, y+size_block//2), size_block//2 - 3, 3)
    if (query-1) % 2 == 0:  # X
        game_over = check_win(mas, 'x') #Победил игрок Х. Нажмите пробел для рестарта
    else:
        game_over = check_win(mas, 'o') #Победил игрок O. Нажмите пробел для рестарта
        
    if game_over:
        screen.fill(black) # заливаем экран черным
        font = pygame.font.SysFont('stxingkai', 200) # задаем шрифт и его ширину, текст game_over
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()  # узнаем его координаты
        text_x = screen.get_width() / 2 - text_rect.width / 2  # нахождение центра экрана
        text_y = screen.get_height() / 2 - text_rect.height / 2  
        screen.blit(text1, [text_x, text_y]) # прикрепление текста по найденным координатам
        
        font = pygame.font.SysFont('stxingkai', 22) 
        text2 = font.render('Игра окончена, нажмите пробел для рестарта.', True, white)
        text2_rect = text2.get_rect() 
        text2_x = screen.get_width() / 3 - text2_rect.width / 3  
        text2_y = screen.get_height() / 3 - text2_rect.height / 3  
        screen.blit(text2, [text2_x, text2_y])
        
    pygame.display.update()
