from pygame import *

def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    An anti aliased Rounded Rectangle: http://pygame.org/project/2349
    
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    #circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)

def ScoreboardHighlightVertical(screen, x, y, w, h, color):
    p1 = (x+(w/2),y)
    p2 = (x+w,y+(h/7))
    p3 = (x+w,y+h-(h/7))
    p4 = (x+(w/2),y+h)
    p5 = (x,y+h-(h/7))
    p6 = (x,y+(h/7))
    draw.polygon(screen, color, [p1,p2,p3,p4,p5,p6])
    
def ScoreboardHighlightHorizontal(screen, x, y, w, h, color):
    p1 = (x,y+(h/2))
    p2 = (x+(w/7),y)
    p3 = (x+w-(w/7),y)
    p4 = (x+w,y+(h/2))
    p5 = (x+w-(w/7),y+h)
    p6 = (x+(w/7),y+h)
    draw.polygon(screen, color, [p1,p2,p3,p4,p5,p6]) 
