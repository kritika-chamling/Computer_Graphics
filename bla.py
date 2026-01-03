import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BLA Algorithm")
WHITE=(255,255,255)
BLACK=(0,0,0)


def draw_line_bla(x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    if x2>x1:
        lx=1
    else:
        lx=-1
    if y2>y1:
        ly=1
    else:
        ly=-1
    x=x1
    y=y1
    if dx>dy:
        p=2*dy-dx
        for i in range(0,dx):
            if p<0:
                x=x+lx
                y=y
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
            screen.set_at((x,y),WHITE)     
    else:
        p=2*dx-dy
        for i in range(0,dy):
            if p<0:
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((x,y),WHITE) 


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        draw_line_bla(100,90,30,50)
        pygame.display.flip()           

if __name__=="__main__":
    main()
