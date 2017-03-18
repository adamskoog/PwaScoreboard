import pygame, shapes

def drawNumber(number, screen, x, y, w, h):
    strNumber = "00"
    
    if number < 10:
        strNumber = "0" + str(number)
    else:
        strNumber = str(number)
    
    drawHighlight(strNumber[0], screen, x+1, y+1, (w/2)-1, h-2)
    drawHighlight(strNumber[1], screen, x+(w/2)+1, y+1, (w/2)-1, h-2)
    

def drawHighlight(number, screen, x, y, w, h):
    if number == "0":
        drawNumberZero(screen, x, y, w, h)
    elif number == "1":
        drawNumberOne(screen, x, y, w, h)
    elif number == "2":
        drawNumberTwo(screen, x, y, w, h)
    elif number == "3":
        drawNumberThree(screen, x, y, w, h)
    elif number == "4":
        drawNumberFour(screen, x, y, w, h)
    elif number == "5":
        drawNumberFive(screen, x, y, w, h)
    elif number == "6":
        drawNumberSix(screen, x, y, w, h)
    elif number == "7":
        drawNumberSeven(screen, x, y, w, h)
    elif number == "8":
        drawNumberEight(screen, x, y, w, h)
    elif number == "9":
        drawNumberNine(screen, x, y, w, h)
    
    
def drawNumberZero(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, ORANGE)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, BLACK)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, ORANGE)
    
def drawNumberOne(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, BLACK)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, BLACK)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, BLACK)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, BLACK)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, BLACK)
    
def drawNumberTwo(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, BLACK)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, ORANGE)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, BLACK)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, ORANGE)
    
def drawNumberThree(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, BLACK)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, BLACK)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, ORANGE)
    
def drawNumberFour(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, BLACK)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, BLACK)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, BLACK)
    
def drawNumberFive(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, BLACK)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, BLACK)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, ORANGE)
    
def drawNumberSix(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, ORANGE)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, BLACK)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, ORANGE)
    
def drawNumberSeven(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, BLACK)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, BLACK)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, BLACK)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, BLACK)
    
def drawNumberEight(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, ORANGE)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, ORANGE)
    
def drawNumberNine(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    #left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, BLACK)
    
    #right side
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y, w/5, h/2, ORANGE)
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5), y+h/2, w/5, h/2, ORANGE)
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h/2, (h-pad)/2, w/5, ORANGE)
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, (y-pad)+h, (h-pad)/2, w/5, ORANGE)