import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mid-point Circle Algorithm")
WHITE=(255,255,255)
BLACK=(0,0,0)


def draw_circle(xc,yc,r):
    x=0
    y=r
    d=1-r
    
    while(x<=y):
        screen.set_at((x+xc,y+yc),"RED")
        screen.set_at((y+yc,x+xc),"GREEN")
        screen.set_at((-y+yc,x+xc),"YELLOW")
        screen.set_at((-x+xc,y+yc),"BLUE")
        screen.set_at((-x+xc,-y+yc),"RED")
        screen.set_at((-y+yc,-x+xc),"GREEN")
        screen.set_at((y+yc,-x+xc),"YELLOW")
        screen.set_at((x+xc,-y+yc),"BLUE")
        x=x+1
        if d<0:
            y=y
            d=d+2*x+1
        else:
            y=y-1
            d=d+2*x-2*y+1
            

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        draw_circle(200,200,100)
        pygame.display.flip()   


if __name__=="__main__":
    main()
