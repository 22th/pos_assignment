import pygame
import random
pygame.init()
def Button(screen,c1,c2,c3,xcoord,ycoord,mc1,mc2,mc3,mpos,mstat,font,text,tc1,tc2,tc3):
    xcv1=font.render(text,1,(tc1,tc2,tc3))
    bwidth=pygame.Surface.get_width(xcv1)
    bheight=pygame.Surface.get_height(xcv1)
    pygame.draw.rect(screen,(c1,c2,c3),(xcoord,ycoord,bwidth,bheight))
    if xcoord+bwidth > mpos[0] > xcoord and ycoord+bheight > mpos[1] >ycoord:
        pygame.draw.rect(screen,(mc1,mc2,mc3),(xcoord,ycoord,bwidth,bheight))
        screen.blit(xcv1,(xcoord,ycoord))
        return mstat[0];
    
    
    screen.blit(xcv1,(xcoord,ycoord))
    
def imgButton(screen,img,xcoord,ycoord,mpos,mstat):
    screen.blit(img,(xcoord,ycoord))
    height=img.get_height()
    width=img.get_width()
    if xcoord+width > mpos[0] > xcoord and ycoord+height > mpos[1] > ycoord:
        return mstat[0];
    
def shuffle(arrayToBeShuff,arrayreplace):
    i = 0
    shuff_array=[]
    while i < len(arrayToBeShuff):
        shuff_array.append(i)
        i = i + 1
    #print(shuff_array)
    random.shuffle(shuff_array)
    #print(shuff_array)
    i = 0
    while i < len(arrayToBeShuff):
        arrayreplace==shuff_array[i]
        print(arrayreplace)
        i = i + 1
