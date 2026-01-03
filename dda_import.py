import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DDA Algorithm")
WHITE=(255,255,255)
BLACK=(0,0,0)

def draw_line_dda(x1,y1,x2,y2):
     dx=x2-x1
     dy=y2-y1
     if dx>dy:
        step=dx
     else:
        step=dy
     xinc=dx/step
     yinc=dy/step
     x=x1
     y=y1
     for i in range(0,step):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),WHITE) 

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        draw_line_dda(20,20,100,100)
        pygame.display.flip()           

if __name__=="__main__":
    main()



