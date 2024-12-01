"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""
import pygame
from random import randint
from boutton import Checkbox,TextInput
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 10


FPS=1000   #vitesse du jeu

ROUGE=(255,0,0)
NOIR=(0,0,0)
BLANC=(255,255,255)
VERT=(0,255,0)
BLEU=(0,0,125)
MAGENTA=(255,0,255)
cellcolor=(15,240,46)
grillecolor=NOIR
background_color=grillecolor


global nbCellHeight, nbCellWidth
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE

clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)
#endregion





#Trace la grille
def tracerGrille():
    for i in range(0,WINDOWWIDTH+1,CELLSIZE):
        pygame.draw.line(fenetre,grillecolor,(0+i,0),(0+i,700),1)
    for j in range(0,WINDOWHEIGHT+1,CELLSIZE):
        pygame.draw.line(fenetre,grillecolor,(0,0+j),(1366,0+j),1)
    pass


#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire(State):
    return [[randint(0,State-1) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    

COLORS = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    c=10
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=0:
                
                if not colormode: colo = (c*vie[x][y],c*vie[x][y],c*vie[x][y])
                else: 
                    #colo = ((c*vie[x][y])%255,(5*c*vie[x][y])%255,(2*c*vie[x][y])%255)
                    colo = COLORS[vie[x][y]]
                pygame.draw.rect(fenetre, colo, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
    

#DÃ©termine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.


def voisin(x, y, vie):
    nbvoisin = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue 
            nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
            if vie[nx][ny] == (vie[x][y]+1)%State:
                nbvoisin += 1
    return nbvoisin
 






#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            a = voisin(x, y, vie)
            
            if (a ==2 and rule2) or (a == 4 and rule4) or (a == 6 and rule6) or (a == 8 and rule8)\
                or (a == 3 and rule3) or (a == 5 and rule5) or (a == 7 and rule7) or (a == 1 and rule1)\
                    or (a == 0 and rule0):   
                next_vie[x][y] = (vie[x][y]+1)%State
            else:
                next_vie[x][y] = vie[x][y]  
            

    return next_vie



Checkbox1 = Checkbox(100, 100, 50, 50, "Start", (255, 0, 0), False) 
Checkbox2 = Checkbox(100, 200, 50, 50, "Rule 2", (255, 0, 0), True)
Checkbox3 = Checkbox(100, 300, 50, 50, "Rule 4", (255, 0, 0), True)
Checkbox4 = Checkbox(100, 400, 50, 50, "Rule 6", (255, 0, 0), True)
Checkbox5 = Checkbox(100, 500, 50, 50, "Rule 8", (255, 0, 0), True)
Checkbox6 = Checkbox(100, 600, 50, 50, "color mode", (255, 0, 0), False)
Checkbox7 = Checkbox(300, 200, 50, 50, "Rule 3", (255, 0, 0), False)
Checkbox8 = Checkbox(300, 300, 50, 50, "Rule 5", (255, 0, 0), False)
Checkbox9 = Checkbox(300, 400, 50, 50, "Rule 7", (255, 0, 0), False)
Checkbox10 = Checkbox(300, 500, 50, 50, "Rule 1", (255, 0, 0), False)
Checkbox11 = Checkbox(500, 600, 50, 50, "Quit", (255, 0, 0), False)
Checkbox12 = Checkbox(300, 600, 50, 50, "Rule 0", (255, 0, 0), False)
TextInput1= TextInput(200,100,150,50,20)



mousePressed1=False
mousePressed2=False
import time
timer = time.monotonic()
time_interval = 0.01
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loopGame=True
run=True
loopMenu=True

pygame.display.set_caption("Menu")
font = pygame.font.Font('freesansbold.ttf', 20)

def printscreen(text:str,x,y,color):
    txt=font.render(text,True,color)
    fenetre.blit(txt,(x,y))



rule0=False
rule2=False
rule4=False
rule6=False
rule8=False
rule1=False
rule3=False
rule5=False
rule7=False
colormode=False
txtimput= ''

def menu():
    global rule2,rule4,rule6,rule8,colormode,rule3,rule5,rule7,rule1,txtimput
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
                quit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_w:
                    break
            if TextInput1.analyse_event(event) != '' and TextInput1.active == False:
                txtimput = int(TextInput1.text)
        
        fenetre.fill((52,78,91))
        
        if Checkbox1.draw(fenetre):
            break
            
            
        
        
        
        if Checkbox2.draw(fenetre): rule2=True
        else: rule2=False
        
        if Checkbox3.draw(fenetre):rule4=True
        else:rule4=False
        
        if Checkbox4.draw(fenetre):rule6=True
        else:rule6=False
        
        if Checkbox5.draw(fenetre):rule8=True
        else:rule8=False
        
        if Checkbox6.draw(fenetre):colormode=True
        else:colormode=False
        
        if Checkbox7.draw(fenetre):rule3=True
        else:rule3=False
        
        if Checkbox8.draw(fenetre):rule5=True
        else:rule5=False
        
        if Checkbox9.draw(fenetre):rule7=True
        else:rule7=False
        
        if Checkbox10.draw(fenetre):rule1=True
        else:rule1=False
        
        if Checkbox12.draw(fenetre):rule0=True
        else:rule0=False
        
        if Checkbox11.draw(fenetre):
            pygame.quit()
            loopMenu=False
            quit()
            
        TextInput1.draw(fenetre)
        
        
        pygame.display.update()        
        
    
    
menu()
try:
    State=int(txtimput)
except:
    State=4
vie=initialiserCellules()
vie=generationAleatoire(State)
loopGame=True

while loopGame==True:
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loopGame = False            #fermeture de la fenetre (croix rouge)
        
        elif event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP si animation est DéSACTIVER
                #vie=generationAleatoire(vie)
                vie=prochaine_vie(vie)     #manuel
            elif event.key ==pygame.K_w:
                loopGame=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_r:
                vie=generationAleatoire(State)
            elif event.key ==pygame.K_v:
                vie=initialiserCellules()
                
            elif event.key ==pygame.K_ESCAPE:
                Checkbox1.checked=False
                menu()
                
                
               
                
            
            
            elif event.key ==pygame.K_PAGEUP:
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                vie=generationAleatoire(State)
            elif event.key ==pygame.K_PAGEDOWN:
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                vie=generationAleatoire(State)
                
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
            
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=randint(0,3)
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0

    fenetre.fill(background_color)
    remplirGrille(vie)
    #tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    if run and  time.monotonic() - timer > time_interval:
        timer = time.monotonic()
        vie=prochaine_vie(vie)#clock.tick(FPS)



#endregion