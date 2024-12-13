"""
Programme jeu de la vie rÃ©alisÃ© par nGazi Damien Tg3
"""
import pygame
from random import randint,choice
import time
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran

cellcolor = (0,255,0)

clock = pygame.time.Clock()
pygame.init()

display_info = pygame.display.Info()
l = display_info.current_w
h = display_info.current_h - 65 #pour la barre de menu windows

fenetre = pygame.display.set_mode((l,h), pygame.RESIZABLE)

pygame.display.set_caption("Day&Night")
font = pygame.font.Font('freesansbold.ttf', 20)

#variables de l'écran
WINDOWWIDTH = l
WINDOWHEIGHT = h
CELLSIZE = 5
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

global nbCellHeight, nbCellWidth
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE




def initialiserCellules():
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]

def generationAleatoire():
    return [[randint(0,len(dictionairedescouleur)) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    
dictionairedescouleur={
    1:(255,200,0),      #sable
    2:(0,0,255),        #eau
    3:(201,51,0),       #bois
    4:(255,0,0),        #feu
    5:(100,100,100),    #steam
    6:(0,255,0),        #herbe
    7:(0,255,0),        #herbeTige
    8:(153, 51, 0),     #Terre
    
    
    
    
    
    }

#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=0:
                colo = dictionairedescouleur[vie[x][y]]
                pygame.draw.rect(fenetre, colo, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
                        
            
                
                    
           
def bas(x,y,vie):
    return vie[x][y+1]
def haut(x,y,vie):
    return vie[x][y-1]
def droite(x,y,vie):
    return vie[x+1][y]
def gauche(x,y,vie):
    return vie[x-1][y]
def basdroite(x,y,vie):
    return vie[x+1][y+1]
def basgauche(x,y,vie):
    return vie[x-1][y+1]
def hautdroite(x,y,vie):
    return vie[x+1][y-1]
def hautgauche(x,y,vie):
    return vie[x-1][y-1]


def shiftcell(x,y,x2,y2,vie):
    temp1=vie[x][y]
    vie[x][y]=vie[x2][y2]
    vie[x2][y2]=temp1
    

def autour(x,y,vie,types):
    for i in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),(2,-2),(2,-1),(2,0),(2,1),(2,2)]:
        if vie[x+i[0]][y+i[1]] == types:
            return True
        





#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            #a = voisin(x, y, vie)
            #game of life
            
            
            match vie[x][y]:
            
                case 1 : #sable
                    
                    if bas(x,y,vie) == 2 and bas(x,y,next_vie) == 0 and randint(1,10) == 1:  
                        next_vie[x][y+1] = 1  
                        next_vie[x][y] = 2 
                    
                    
                    
                    elif bas(x,y,vie)==0 and y+1<=nbCellHeight-2 and bas(x,y,next_vie)==0:
                        next_vie[x][y+1] = 1
                        next_vie[x][y] = 0

                    elif bas(x,y,vie) != 0 and y+1<=nbCellHeight-2:
                        ch=[-1,1]
                        cd=choice(ch)
                        if  basgauche(x,y,vie) == 0 and cd == -1 and gauche(x,y,vie) == 0 and basgauche(x,y,next_vie)==0:
                            next_vie[x-1][y+1] = 1
                            next_vie[x][y] = 0
                        elif basdroite(x,y,vie) == 0 and cd == 1 and droite(x,y,vie) == 0 and basdroite(x,y,next_vie)==0:
                            next_vie[x+1][y+1] = 1
                            next_vie[x][y] = 0
                        else:
                            if next_vie[x][y] == 0:
                                next_vie[x][y] = vie[x][y]
                    else:
                        if next_vie[x][y] == 0:
                            next_vie[x][y] = vie[x][y]
                        
                case 3: #Bois
                    #print(vie[x][y-1])
                    if haut(x,y,vie)==4 or gauche(x,y,vie)==4 or droite(x,y,vie)==4 or bas(x,y,vie)==4\
                        or hautgauche(x,y,vie)==4 or hautdroite(x,y,vie)==4 or basgauche(x,y,vie)==4 or basdroite(x,y,vie)==4:
                        next_vie[x][y] = 4
                          
                    else:
                        if next_vie[x][y] == 0:
                            next_vie[x][y] = vie[x][y]
                    
                case 2 : #eau
                    
                    if bas(x,y,vie)==4 or gauche(x,y,vie)==4 or droite(x,y,vie)==4:
                        next_vie[x][y+1] = 2
                    
                    elif (vie[x][y+1] == 0 or bas(x,y,vie)==5) and y+1<=nbCellHeight-2 and next_vie[x][y+1]==0:
                        next_vie[x][y+1] = 2
                        next_vie[x][y] = 0

                    elif vie[x][y+1] != 0 and y+1<=nbCellHeight-2:
                        ch=[-1,1]
                        cd=choice(ch)
                        if  vie[x-1][y] == 0 and cd == -1  and next_vie[x-1][y]==0:
                            next_vie[x-1][y] = 2
                            next_vie[x][y] = 0
                        elif vie[x+1][y] == 0 and cd == 1 and next_vie[x+1][y]==0:
                            next_vie[x+1][y] = 2
                            next_vie[x][y] = 0
                        else:
                            if next_vie[x][y] == 0:
                                next_vie[x][y] = vie[x][y]
                    else:
                        if next_vie[x][y] == 0:
                            next_vie[x][y] = vie[x][y]
                       
                case 4 : # feu
                      
                    
                    if haut(x,y,vie)==2:
                        next_vie[x][y] = 2

                    else:
                        if randint(0,100)>99 and haut(x,y,next_vie)==0:
                            next_vie[x][y-1] = 5
                        
                        if next_vie[x][y] == 0:
                            next_vie[x][y] = vie[x][y]
                            
                case 5: #fume
                    
                    if haut(x,y,vie)==0 and y+1<=nbCellHeight-2 and haut(x,y,next_vie)==0 and randint(0,50)>45:
                        next_vie[x][y-1] = 5
                        next_vie[x][y] = 0

                    elif haut(x,y,vie) != 0 and y+1<=nbCellHeight-2:
                        ch=[-1,1]
                        cd=choice(ch)
                        if  hautgauche(x,y,vie) == 0 and cd == -1 and gauche(x,y,vie) == 0 and hautgauche(x,y,next_vie)==0:
                            next_vie[x-1][y-1] = 5
                            next_vie[x][y] = 0
                        elif hautdroite(x,y,vie) == 0 and cd == 1 and droite(x,y,vie) == 0 and hautdroite(x,y,next_vie)==0:
                            next_vie[x+1][y-1] = 5
                            next_vie[x][y] = 0
                        else:
                            next_vie[x][y] = vie[x][y]
                    else:
                        next_vie[x][y] = vie[x][y]
                        
                case 6: #Herbe
                    if bas(x,y,vie)==8 and autour(x,y,vie,2):
                        next_vie[x][y] = 6
                        next_vie[x][y-1] = 7
                    else:
                        next_vie[x][y] = 0
                
                case 7: #Tige
                    if bas(x,y,vie)==8 or bas(x,y,vie)==7:
                        next_vie[x][y] = vie[x][y]
                        if randint(0,100)==1:
                            next_vie[x][y-1] = 7
                    else :
                        next_vie[x][y] = 0

                case 8 : #terre
                    next_vie[x][y] = vie[x][y]
                

                    
                            
                            
                
            


    return next_vie


vie=initialiserCellules()
#vie=generationAleatoire()
timer = time.monotonic()
time_interval = 0.01
key=[]
keyselecteur={}
for i in range(len(dictionairedescouleur.keys())+1):
    key.append(pygame.K_0+i)
    keyselecteur[pygame.K_0+i]=i



    
    
    
print(key)
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
run=True
mousePressed1 = False
mousePressed2 = False
seclecteur = 1
import time
while loop==True:
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        
        elif event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP si animation est DéSACTIVER
                #vie=generationAleatoire(vie)
                vie=prochaine_vie(vie)     #manuel
            elif event.key ==pygame.K_w:
                loop=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_r:
                vie=generationAleatoire()
            elif event.key ==pygame.K_v:
                vie=initialiserCellules()
            
            elif event.key in key:
                seclecteur=keyselecteur[event.key]
            
            
            elif event.key ==pygame.K_RIGHT:
                if time_interval > 0.01: time_interval -= 0.1
            elif event.key ==pygame.K_LEFT:
                time_interval += 0.1
            
            
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mousePressed1 = False
            elif event.button == 3:
                mousePressed2 = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousePressed1 = True
            elif event.button == 3:
                mousePressed2 = True
                
    if mousepos[0]<nbCellWidth*CELLSIZE and mousepos[1]<nbCellHeight*CELLSIZE:
        if mousePressed1:
            if vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]==seclecteur or vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]==0: 
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=seclecteur
            
        elif mousePressed2:
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0
        
            
    fenetre.fill((0,0,0))
    remplirGrille(vie)
    #tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    
    if run and  time.monotonic() - timer > time_interval:
        timer = time.monotonic()
        vie=prochaine_vie(vie)#;time.sleep(0.1)  #pour une animation !!!!!!
    #clock.tick(FPS)

    #vie=prochaine_vie(vie)
pygame.quit()

#endregion