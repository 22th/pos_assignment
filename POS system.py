import pygame
import random
import butoonv2
import eztext
import datetime
#str(datetime.now())
pygame.init()
#rsymonds18@student.sacs.nsw.edu.au
#Variables below
order=[]
ordrs=[]
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
lock = pygame.time.Clock()
myfont = pygame.font.SysFont("Comic Sans MS",15)
ordertotal=0
running = True
running1 = False
running2 = False
running3 = False
running4 = False
running5 = False
crunning1 = False
ordernumbers = []
ordertotal=0
v=0
orderholder= open("order.txt", "a")
f=0
txtbx = eztext.Input(maxlength=45, color=(255,255,255), prompt='type here: ')
name=""
ghf=""
#Variables above
def Backtostart():
    global order
    global running1
    global running2
    global running3
    global running4
    global running5
    global crunning1
    running1=False
    running2=False
    running3=False
    running4=False
    running5=False
    crunning1=False
while running == True:
    lock.tick(100)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: 
            running=False
            
    d=pygame.mouse.get_pos()
    x=pygame.mouse.get_pressed()
    screen.fill((50,205,50))
    order=[]
    ordrs=[]
    for i in open("order.txt","r"):
        ordrs.append(i.strip())       
    chef=butoonv2.Button(screen,200,200,200,100,300,120,120,120,d,x,myfont,"Chef                                                                 ",255,255,255)
    if chef == 1:
        crunning1=True
    #print(chef)
    while crunning1 == True:
        lock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Backtostart()
        screen.fill((50,205,50))
        d=pygame.mouse.get_pos()
        x=pygame.mouse.get_pressed()
        events = pygame.event.get()
        ordrs=[]
        for i in open("order.txt","r"):
            ordrs.append(i.strip())               
        qui=butoonv2.Button(screen,200,200,200,10,10,120,120,120,d,x,myfont,"QUIT",255,255,255)
        if qui == 1:
            Backtostart()   
        i=0
        while i < len(ordrs):
            hihg=myfont.render(ordrs[i],1,(255,255,255))
            ycoord= i*25+150
            screen.blit(hihg,(100, ycoord))
            wid=pygame.Surface.get_width(hihg)
            removeorder=0
            if ordrs[i] != "":
                removeorder=butoonv2.Button(screen,200,200,200,110+wid,i*25+150,120,120,120,d,x,myfont,"Remove Item",255,255,255)
            if removeorder == 1:
                with open("order.txt","r+") as f:
                    t = f.read()
                    remove=ordrs[i]
                    f.seek(0)
                    for line in t.split('\n'):
                        if line != remove:
                            f.write(line+"\n")
                    f.truncate()
                del ordrs[i]
            i = i + 1
        pygame.display.flip()
    help=butoonv2.Button(screen,200,200,200,100,100,120,120,120,d,x,myfont,"sales assistant                                                ",255,255,255)
    quit=butoonv2.Button(screen,200,200,200,10,10,120,120,120,d,x,myfont,"QUIT",255,255,255)
    txtbx.update(events)
    # blit txtbx on the sceen
    txtbx.set_pos(100,10)
    txtbx.draw(screen)
    name=txtbx.value
    if quit == 1:
        Backtostart()
    #inp = Inputbox.ask(screen, 'Name')    
    if help == 1:
        running1 = True
    ordertotal=0
    while running1 == True:
        lock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Backtostart()
        screen.fill((50,205,50))
        d=pygame.mouse.get_pos()
        x=pygame.mouse.get_pressed()
        xcv1=myfont.render(str(ordertotal),1,(255,255,255))
        screen.blit(xcv1,(500,100)) 
        f=0
        cvx1=myfont.render(str(order),1,(255,255,255))
        screen.blit(cvx1,(100,100))
        Hokkien=butoonv2.Button(screen,200,200,200,200,200,60,100,200,d,x,myfont,"Hokkien $6",255,255,255)
        if Hokkien == 1:
            ordertotal=ordertotal+6
            running2=True 
            order.append("Hokkien Noodles")
        Egg=butoonv2.Button(screen,200,200,200,200,250,60,100,200,d,x,myfont,"Egg $6.5",255,255,255)
        if Egg == 1:
            ordertotal=ordertotal+6.5
            running2=True   
            order.append("Egg Noodles")
        Rice=butoonv2.Button(screen,200,200,200,200,300,60,100,200,d,x,myfont,"Rice $5.75",255,255,255)
        if Rice == 1:
            ordertotal=ordertotal+5.75
            running2=True  
            order.append("Rice")
        Flat=butoonv2.Button(screen,200,200,200,200,350,60,100,200,d,x,myfont,"Flat Noodles $7",255,255,255)
        if Flat == 1:
            ordertotal=ordertotal+7
            running2=True   
            order.append("Flat")
        Spaghetti=butoonv2.Button(screen,200,200,200,200,400,60,100,200,d,x,myfont,"Spaghetti $5",255,255,255)
        if Spaghetti == 1:
            ordertotal=ordertotal+5
            running2=True 
            order.append("Spaghetti")
        quit=butoonv2.Button(screen,200,200,200,10,10,120,120,120,d,x,myfont,"QUIT",255,255,255)
        if quit == 1:
            Backtostart()
            
        while running2 == True:
            lock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    Backtostart()
            screen.fill((50,205,50))
            d=pygame.mouse.get_pos()
            x=pygame.mouse.get_pressed()
            xcv1=myfont.render(str(ordertotal),1,(255,255,255))
            screen.blit(xcv1,(500,100))  
            cvx1=myfont.render(str(order),1,(255,255,255))
            screen.blit(cvx1,(100,100))  
            quit=butoonv2.Button(screen,200,200,200,10,10,120,120,120,d,x,myfont,"QUIT",255,255,255)
            if quit == 1:
                Backtostart()
                        
            beef=butoonv2.Button(screen,200,200,200,300,200,60,100,200,d,x,myfont,"Beef $4",255,255,255)
            if beef == 1:
                ordertotal=ordertotal+4
                running3=True
                order.append("Beef, ")
            chicken=butoonv2.Button(screen,200,200,200,300,250,60,100,200,d,x,myfont,"Chicken $4",255,255,255)
            if chicken == 1:
                ordertotal=ordertotal+4
                running3=True
                order.append("Chicken, ")
            fish=butoonv2.Button(screen,200,200,200,300,300,60,100,200,d,x,myfont,"Fish $5",255,255,255)
            if fish == 1:
                ordertotal=ordertotal+5
                running3=True 
                order.append("Fish, ")
            Tofu=butoonv2.Button(screen,200,200,200,300,350,60,100,200,d,x,myfont,"Tofu $3.5",255,255,255)
            if Tofu == 1:
                ordertotal=ordertotal+3.5
                running3=True
                order.append("Tofu")
            while running3 == True:
                lock.tick(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        Backtostart()
                screen.fill((50,205,50))
                quit=butoonv2.Button(screen,200,200,200,10,10,120,120,120,d,x,myfont,"QUIT",255,255,255)
                if quit == 1:
                    Backtostart()               
                d=pygame.mouse.get_pos()
                x=pygame.mouse.get_pressed()
                xcv1=myfont.render(str(ordertotal),1,(255,255,255))
                screen.blit(xcv1,(500,100))   
                cvx1=myfont.render(str(order),1,(255,255,255))
                screen.blit(cvx1,(100,100))                
                teriyaki=butoonv2.Button(screen,200,200,200,400,200,60,100,200,d,x,myfont,"Teriyaki $2.75",255,255,255)
                if teriyaki == 1:
                    ordertotal=ordertotal+2.75
                    running4=True
                    order.append("Teriyaki Sauce, ")
                chilli_basil=butoonv2.Button(screen,200,200,200,400,250,60,100,200,d,x,myfont,"Chilli & Basil $3.5",255,255,255)
                if chilli_basil == 1:
                    ordertotal=ordertotal+3.5
                    running4=True
                    order.append("Chilli & Basil Sauce, ")
                Plum=butoonv2.Button(screen,200,200,200,400,300,60,100,200,d,x,myfont,"Plum $2.5",255,255,255)
                if Plum == 1:
                    ordertotal=ordertotal+2.5
                    running4=True
                    order.append("Plum Sauce, ")
                oyster_soy=butoonv2.Button(screen,200,200,200,400,350,60,100,200,d,x,myfont,"Oyster & Soy $3",255,255,255)
                if oyster_soy == 1:
                    ordertotal=ordertotal+3
                    running4=True
                    order.append("Oyster & Soy Sauce")
                while running4 == True:
                    lock.tick(100)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            Backtostart()
                    screen.fill((50,205,50))
                    d=pygame.mouse.get_pos()
                    x=pygame.mouse.get_pressed()
                    New_order=butoonv2.Button(screen,200,200,200,400,420,60,100,200,d,x,myfont,"New Order",255,255,255)
                    #order=order.strip()
                    quit=butoonv2.Button(screen,200,200,200,10,10,120,120,120,d,x,myfont,"QUIT",255,255,255)
                    if quit == 1:
                        Backtostart()
                                        
                    cvx1=myfont.render(str(order),1,(255,255,255))
                    screen.blit(cvx1,(100,100))
                    while running5== True:
                        lock.tick(100)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                Backtostart()
                        screen.fill((50,205,50))
                        d=pygame.mouse.get_pos()
                        x=pygame.mouse.get_pressed()
                        quit=butoonv2.Button(screen,200,200,200,10,10,120,120,120,d,x,myfont,"QUIT",255,255,255)
                        if quit == 1:
                            Backtostart()
                                                
                        New_order=butoonv2.Button(screen,200,200,200,400,400,60,100,200,d,x,myfont,"New order",255,255,255)
                        if New_order == 1:
                            running1=False
                            running2=False
                            running3=False
                            running4=False
                            running5=False
                            
                        if f == 0:
                            orderholder.write(str(order)+" | "+str(ordertotal)+" | "+str(v)+" | "+str(name) +" | "+str(datetime.datetime.now())+"\n")
                            orderholder.close()
                            f=f+1
                        xcv1=myfont.render(str(v),1,(255,255,255))
                        screen.blit(xcv1,(500,100)) 
                        pygame.display.flip()
                        
                    paid=butoonv2.Button(screen,200,200,200,600,200,100,100,100,d,x,myfont,"PAID",255,255,255)
                    if paid == 1:
                        running5=True
                        v=random.randrange(0,100)
                    if New_order == 1:
                        running1=False
                        running2=False
                        running3=False
                        running4=False
                    xcv1=myfont.render(str(ordertotal),1,(255,255,255))
                    if v in ordernumbers:
                        v=random.randrange(0,100)
                    orderholder= open("order.txt", "a")                    
                    screen.blit(xcv1,(500,100)) 
                    pygame.display.flip()
                pygame.display.flip()    
            pygame.display.flip()
        pygame.display.flip() 
    pygame.display.flip()
