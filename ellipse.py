import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mid-point Ellipse Algorithm")
WHITE=(255,255,255)
BLACK=(0,0,0)


def draw_ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    #For Region 1
    p1=float(ry**2-(rx**2)*ry+1/4*(rx**2))
    while(2*(ry**2)*x <= 2*(rx**2)*y):
        if(p1<0):
            x=x+1
            y=y
            p1=float(p1+2*(ry**2)*x+(ry**2))
        else:
            x=x+1
            y=y-1
            p1=float(p1+2*(ry**2)*x-2*(rx**2)*y+(ry**2))
        screen.set_at((x+xc,y+yc),BLACK)
        screen.set_at((x+xc,-y+yc),BLACK)
        screen.set_at((-x+xc,-y+yc),BLACK)
        screen.set_at((-x+xc,y+yc),BLACK)

    #For Region 2
    p2=float((ry**2)*((x+0.5)**2)+(rx**2)*((y-1)**2)-(rx**2)*(ry**2))
    while(y!=0):
        if(p2>0):
            x=x
            y=y-1
            p2=float(p2-2*(rx**2)*y+(rx**2))
        else:
            x=x+1
            y=y-1
            p2=float(p2+2*(ry**2)*x-2*(rx**2)*y+(rx**2))
        screen.set_at((x+xc,y+yc),BLACK)
        screen.set_at((x+xc,-y+yc),BLACK)
        screen.set_at((-x+xc,-y+yc),BLACK)
        screen.set_at((-x+xc,y+yc),BLACK)


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        draw_ellipse(250,250,150,100)
        pygame.display.flip()   


if __name__=="__main__":
    main()

        