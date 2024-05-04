import random
from PIL import Image,ImageDraw
import pygame
import time

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.init()
display_width = 650
display_height = 800
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
tie = font.render('The Game has TIED', True, green, blue)
won = font.render('YOU WON!', True, green, blue)
lost = font.render('YOU LOST!', True, green, blue)
place_some_else = font.render('Place Somewhere Else', True, green, blue)

top_left = (40,155)
top_center = (230,155)
top_right = (425,155)
end_top_right = (614,155)

mid_left = (40,343)
mid_center = (230,343)
mid_right = (425,343)
end_mid_right = (614,343)

bottom_left = (40,540)
bottom_center = (230,540)
bottom_right = (425,540)
end_bottom_right = (614,540)

end_bottom = 720

display_surface = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("TIC TAC TOE")

grid = pygame.image.load('./sprites/grid.png')

cross = pygame.image.load('./sprites/cross.jpg')

circle = pygame.image.load('./sprites/circle.png')
circle = pygame.transform.scale(circle,(100,100))

first = {'a':0,'b':1,'c':2}
revFirst = {0:'a',1:'b',2:'c'}

board = ['⬜⬜⬜','⬜⬜⬜','⬜⬜⬜']

x = '❌'
o = '⭕'

def win(board,var):
    if (board[0][0] == var and board[1][1] == var and board[2][2] == var) or (board[0][0] == var and board[1][0] == var and board[2][0] == var) or (board[0][1] == var and board[1][1] == var and board[2][1] == var) or (board[0][2] == var and board[1][2] == var and board[2][2] == var) or (board[0][2] == var and board[1][1] == var and board[2][0] == var) or (board[0][0] == var and board[0][1] == var and board[0][2] == var) or (board[1][0] == var and board[1][1] == var and board[1][2] == var) or (board[2][0] == var and board[2][1] == var and board[2][2] == var):
        return True
    
    return False

def taken(board,pos):
    row = first[pos[0]]
    col = int(pos[1])

    if board[row][col] == '⬜':
        return False
    return True

def place(board,pos,var):
    r = first[pos[0]]
    
    col = int(pos[1])

    row = board[r]

    if(col==0):
        row = var+row[1]+row[2]
        board[r]=row
    if(col==1):
        row = row[0]+var+row[2]
        board[r]=row
    if(col==2):
        row = row[0]+row[1]+var
        board[r]=row

def unPlace(board,pos,var):
    r = first[pos[0]]
    col = int(pos[1])
    row = board[r]

    if(col==0):
        row = var+row[1]+row[2]
        board[r]=row
    if(col==1):
        row = row[0]+var+row[2]
        board[r]=row
    if(col==2):
        row = row[0]+row[1]+var
        board[r]=row


def emptyBoard(board):

    for i in range(3):
        for j in range(3):
            if board[i][j] == '⬜':
                return True

    return False

def availableMoves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != x and board[i][j] != o:
                moves.append(f"{revFirst[i]}{j+1}")
    
    return moves

gameOver = False

turn = 0

for i in range(3):
    print(board[i])


display_surface.fill((255,255,255))
display_surface.blit(grid,(0,0))

while not gameOver:
    for event in pygame.event.get():
        if win(board,x) or win(board,o):
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            else:
                continue
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if turn == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"MOUSE PRESSED {pygame.mouse.get_pressed()}")
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                print(mouse_x,mouse_y)
                if (mouse_x > top_left[0] and mouse_x < top_center[0]) and (mouse_y > top_left[1] and mouse_y < mid_left[1]): # Top LEFT
                    pos = 'a1'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(top_left[0],top_left[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > top_center[0] and mouse_x < top_right[0]) and (mouse_y > top_center[1] and mouse_y < mid_center[1]): # Top CENTER
                    pos = 'a2'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(top_center[0],top_center[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > top_right[0] and mouse_x < end_top_right[0]) and (mouse_y > top_right[1] and mouse_y < end_mid_right[1]): # Top RIGHT
                    pos = 'a3'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(top_right[0],top_right[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > mid_left[0] and mouse_x < mid_center[0]) and (mouse_y > mid_left[1] and mouse_y < bottom_left[1]): # Mid LEFT
                    pos = 'b1'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(mid_left[0],mid_left[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > mid_center[0] and mouse_x < mid_right[0]) and (mouse_y > mid_center[1] and mouse_y < bottom_center[1]): # Mid CENTER
                    pos = 'b2'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(mid_center[0],mid_center[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > mid_right[0] and mouse_x < end_mid_right[0]) and (mouse_y > mid_right[1] and mouse_y < end_bottom_right[1]): # Mid RIGHT
                    pos = 'b3'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(mid_right[0],mid_right[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > bottom_left[0] and mouse_x < bottom_center[0]) and (mouse_y > bottom_left[1] and mouse_y < end_bottom): # Bottom LEFT
                    pos = 'c1'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(bottom_left[0],bottom_left[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > bottom_center[0] and mouse_x < bottom_right[0]) and (mouse_y > bottom_center[1] and mouse_y < end_bottom): # Bottom CENTER
                    pos = 'c2'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(bottom_center[0],bottom_center[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_width,display_height))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
                elif (mouse_x > bottom_right[0] and mouse_x < end_bottom_right[0]) and (mouse_y > bottom_right[1] and mouse_y < end_bottom): # Bottom RIGHT
                    pos = 'c3'
                    col = int(pos[1]) -1
                    pos = pos[0]+str(col)

                    if not taken(board,pos):
                        place(board,pos,x)
                        display_surface.blit(cross,(bottom_right[0],bottom_right[1]))
                        if not emptyBoard(board):
                            display_surface.blit(tie,(display_height//2-200,display_width//2))
                            break

                        turn=1
                        if win(board,x):
                            display_surface.blit(won,(display_height//2-200,display_width//2))
                            break

                    else:
                        print("Someone already placed there, please try again with a different point")
        
        elif turn == 1:
            col = random.choice(['a','b','c'])
            pos = str(random.randint(0,2))
            pos = col+pos

            if pos == 'a0':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(top_left[0]+50,top_left[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn = 0
                    if win(board,x):
                        display_surface.blit(won,(display_height//2-200,display_width//2))
                        break
            elif pos == 'a1':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(top_center[0]+50,top_center[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn = 0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        break
            elif pos == 'a2':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(top_right[0]+50,top_right[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn = 0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        break
            elif pos == 'b0':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(mid_left[0]+50,mid_left[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn = 0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        break
            elif pos == 'b1':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(mid_center[0]+50,mid_center[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn = 0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        break
            elif pos == 'b2':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(mid_right[0]+50,mid_right[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn = 0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        break
            elif pos == 'c0':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(bottom_left[0]+50,bottom_left[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn=0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        break
            elif pos == 'c1':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(bottom_center[0]+50,bottom_center[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn=0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        break
            elif pos == 'c2':
                if not taken(board,pos):
                    place(board,pos,o)
                    display_surface.blit(circle,(bottom_right[0]+50,bottom_right[1]+50))
                    if not emptyBoard(board):
                        display_surface.blit(tie,(display_height//2-200,display_width//2))
                        break

                    turn=0
                    if win(board,o):
                        display_surface.blit(lost,(display_height//2-200,display_width//2))
                        
                        break
    print(board)
    pygame.display.update()
    clock.tick(60)

        

      