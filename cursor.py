import pygame

_HAND = (
"     XX         ",
"    X..X        ",
"    X..X        ",
"    X..X        ",
"    X..XXXXX    ",
"    X..X..X.XX  ",
" XX X..X..X.X.X ",
"X..XX.........X ",
"X...X.........X ",
" X.....X.X....X ",
"  X....X.X....X ",
"  X....X.X...X  ",
"   X...X.X...X  ",
"    X.......X   ",
"     X....X.X   ",
"     XXXXX XX   ")

_ARROW = (
"XX              ",
"X.X             ",
"X..X            ",
"X...X           ",
"X....X          ",
"X.....X         ",
"X......X        ",
"X.......X       ",
"X........X      ",
"X.........X     ",
"X......XXXXX    ",
"X...X..X        ",
"X..XX..X        ",
"X.X XX..X       ",
"XX   X..X       ",
"X     XX        ")
_HCURS, _HMASK = pygame.cursors.compile(_HAND, "X", ".")
HAND_CURSOR = ((16, 16), (5, 1), _HCURS, _HMASK)

_ACURS, _AMASK = pygame.cursors.compile(_ARROW, "X", ".")
ARROW_CURSOR = ((16, 16), (5, 1), _ACURS, _AMASK)


def collide(x,y,image,pos) :
    rect = image.get_rect()
    if pos[0] >= x and pos[0] <=x + rect.width and pos[1] >= y and pos[1] <= y + rect.height :
        return 1
    else :
        return 0
