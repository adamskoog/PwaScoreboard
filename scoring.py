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
    

def drawGenericNumber(screen, x, y, w, h, colors):
    pad = h * 0.05 #padding
    
    x += pad
    y += pad
    w -= pad*4
    h -= pad*2
    
    # Left side
    shapes.ScoreboardHighlightVertical(screen, x, y, w/5, h/2, colors[0])
    shapes.ScoreboardHighlightVertical(screen, x, y+h/2, w/5, h/2, colors[1])
    
    # Right side
    # Note: the (+10) for the width will obviously not scale, but getting this positioned
    # this good was a paid. Will need to revisit.
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5)+10, y, w/5, h/2, colors[2])
    shapes.ScoreboardHighlightVertical(screen, x+w+(pad*2)-(w/5)+10, y+h/2, w/5, h/2, colors[3])
    
    shapes.ScoreboardHighlightHorizontal(screen, x+pad, y-pad, (h)/2, w/5, colors[4])
    shapes.ScoreboardHighlightHorizontal(screen, x+pad+2, ((y-pad)+h/2)+2, (h-pad)/2, w/5, colors[5])
    shapes.ScoreboardHighlightHorizontal(screen, x+pad+2, (y-pad)+(h+pad/2), (h-pad)/2, w/5, colors[6])

    
def drawNumberZero(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    colors = [ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, BLACK, ORANGE]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberOne(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    colors = [BLACK, BLACK, ORANGE, ORANGE, BLACK, BLACK, BLACK]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberTwo(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    colors = [BLACK, ORANGE, ORANGE, BLACK, ORANGE, ORANGE, ORANGE]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberThree(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    colors = [BLACK, BLACK, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberFour(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    colors = [ORANGE, BLACK, ORANGE, ORANGE, BLACK, ORANGE, BLACK]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberFive(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    colors = [ORANGE, BLACK, BLACK, ORANGE, ORANGE, ORANGE, ORANGE]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberSix(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    colors = [ORANGE, ORANGE, BLACK, ORANGE, ORANGE, ORANGE, ORANGE]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberSeven(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)
    
    colors = [BLACK, BLACK, ORANGE, ORANGE, ORANGE, BLACK, BLACK]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberEight(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    colors = [ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE]
    drawGenericNumber(screen, x, y, w, h, colors)
    
def drawNumberNine(screen, x, y, w, h):
    ORANGE  = (255,126,2)
    BLACK   = (0,0,0)

    colors = [ORANGE, BLACK, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE]
    drawGenericNumber(screen, x, y, w, h, colors)