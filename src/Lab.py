"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""
import pygame
from random import randint
from boutton import Checkbox,Bouton,TextInput
from collections import defaultdict


#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 4


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

def remplirGrillejdlv(vie):
    for i,j in vie:
        pygame.draw.rect(fenetre,cellcolor,(i*CELLSIZE,j*CELLSIZE,CELLSIZE,CELLSIZE))
        
def generationAleatoirejdlv():
    #return set([(j,i) for i in range(nbCellHeight+1) for j in range(nbCellWidth+1) if randint(0,10) in [4,5]])
    return [(j,i) for i in range(nbCellHeight+1) for j in range(nbCellWidth+1) if randint(0,10) in [4,5]]
def prochaine_jdlvie(vie,survies,naissances,voisins):
    
    ditctionaire_voisin=defaultdict(int)
    for i,j in vie:
        for x,y in voisins:
            if 0<=i+x<nbCellWidth and 0<=j+y<nbCellHeight:
                ditctionaire_voisin[(i+x,j+y)]+=1
    """
    surv= set({ 
               cell for cell, num, in ditctionaire_voisin.items() if num in survies
               }& vie)
    naiss:set = set({ cell for cell, num in ditctionaire_voisin.items() if num in naissances}-vie)
    print(type(surv),type(naiss))
    """
    
    survie = {cellule for cellule in vie if ditctionaire_voisin[cellule] in survies}
    naissance = {cellule for cellule in ditctionaire_voisin if ditctionaire_voisin[cellule] in naissances and cellule not in vie}
    return survie | naissance
    #return surv | naiss
    
            

    






#region menu

def printscreen(text:str,x,y,color):
    txt=font.render(text,True,color)
    fenetre.blit(txt,(x,y))


CheckboxStart = Checkbox(100, 100, 50, 50, "Start", (255, 0, 0), False) 
CheckboxCl = Checkbox(100, 600, 50, 50, "color mode", (255, 0, 0), False)
CheckboxQuit = Checkbox(500, 600, 50, 50, "Quit", (255, 0, 0), False)
BoutonSave = Bouton(400, 200, 50, 50, "Save", (255, 0, 0), False)
BoutonLoad = Bouton(400, 300, 50, 50, "Load", (255, 0, 0), False)
Savelocation =TextInput(400, 400, 200, 64,32)



Checkbox0 = Checkbox(300, 600, 50, 50, "Rule 0", (255, 0, 0), False)
Checkbox1 = Checkbox(300, 500, 50, 50, "Rule 1", (255, 0, 0), False)
Checkbox2 = Checkbox(100, 200, 50, 50, "Rule 2", (255, 0, 0), False)
Checkbox3 = Checkbox(300, 200, 50, 50, "Rule 3", (255, 0, 0), True)
Checkbox4 = Checkbox(100, 300, 50, 50, "Rule 4", (255, 0, 0), False)
Checkbox5 = Checkbox(300, 300, 50, 50, "Rule 5", (255, 0, 0), False)
Checkbox6 = Checkbox(100, 400, 50, 50, "Rule 6", (255, 0, 0), False)
Checkbox7 = Checkbox(300, 400, 50, 50, "Rule 7", (255, 0, 0), False)
Checkbox8 = Checkbox(100, 500, 50, 50, "Rule 8", (255, 0, 0), False)

lst_checkbox=[Checkbox0,Checkbox1,Checkbox2,Checkbox3,Checkbox4,Checkbox5,Checkbox6,Checkbox7,Checkbox8]

Checkboxb0 = Checkbox(900, 600, 50, 50, "Rule 0", (255, 0, 0), False)
Checkboxb1 = Checkbox(900, 500, 50, 50, "Rule 1", (255, 0, 0), False)
Checkboxb2 = Checkbox(700, 200, 50, 50, "Rule 2", (255, 0, 0), True)
Checkboxb3 = Checkbox(900, 200, 50, 50, "Rule 3", (255, 0, 0), True)
Checkboxb4 = Checkbox(700, 300, 50, 50, "Rule 4", (255, 0, 0), False)
Checkboxb5 = Checkbox(900, 300, 50, 50, "Rule 5", (255, 0, 0), False)
Checkboxb6 = Checkbox(700, 400, 50, 50, "Rule 6", (255, 0, 0), False)
Checkboxb7 = Checkbox(900, 400, 50, 50, "Rule 7", (255, 0, 0), False)
Checkboxb8 = Checkbox(700, 500, 50, 50, "Rule 8", (255, 0, 0), False)

lst_checkboxb= [Checkboxb0,Checkboxb1,Checkboxb2,Checkboxb3,Checkboxb4,Checkboxb5,Checkboxb6,Checkboxb7,Checkboxb8]




CheckboxVs=[]
for i in range (5):
    for j in range (5):
        CheckboxVs.append(Checkbox(1100+i*50, 300+j*50, 50, 50, '', (255, 0, 0), False))

for i in [6,7,8,11,13,16,17,18]:
    CheckboxVs[i].checked = True
    
    
    
    
def to_savedata():
    to_save = {}
    for i in range (len(CheckboxVs)):
        to_save[str(i)] = CheckboxVs[i].checked
    for i in range (len(lst_checkbox)):
        to_save[str(i+25)] = lst_checkbox[i].checked
    for i in range (len(lst_checkboxb)):
        to_save[str(i+34)] = lst_checkboxb[i].checked 
    return to_save   

def to_loaddata(data):
    for i in range (len(CheckboxVs)):
        CheckboxVs[i].checked = data[str(i)]
    for i in range (len(lst_checkbox)):
        lst_checkbox[i].checked = data[str(i+25)]
    for i in range (len(lst_checkboxb)):
        lst_checkboxb[i].checked = data[str(i+34)]
    


import os 
import json


boutonprint = Bouton(0, 0, 140, 32, '', (52,78, 91), (0,0,0))

def save():
    if Savelocation.text not in ['day&night']:
        os.makedirs("saves", exist_ok=True)
        os.makedirs("src/saves/jdlv", exist_ok=True)
        with open(f"src/saves/jdlv/{Savelocation.text}.json", "w") as f:
            json.dump(to_savedata(), f)
        print("sauvegarde effectuer")
        boutonprint.txt = 'sauvegarde effectuer'
    else:
        boutonprint.txt = 'sauvegarde impossible ou tentative de réecriture d"une des sauvegarde de base'


def load():
    try:
        with open(f"src/saves/jdlv/{Savelocation.text}.json", "r") as f:
            data = json.load(f)
            to_loaddata(data)
        print("sauvegarde chargé")
        boutonprint.txt = 'sauvegarde chargé'
        
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée")
        boutonprint.txt = 'Aucune sauvegarde trouvée'


rule0S=False
rule1S=False
rule2S=False
rule3S=False
rule4S=False
rule5S=False
rule6S=False
rule7S=False
rule8S=False
survies = []

rule0B=False
rule1B=False
rule2B=False
rule3B=False
rule4B=False
rule5B=False
rule6B=False
rule7B=False
rule8B=False
colormode=False
naissances =[]


def menu():
    global rule0B,rule1B,rule2B,rule3B,rule4B,rule5B,rule6B,rule7B,rule8B
    global rule0S,rule1S,rule2S,rule3S,rule4S,rule5S,rule6S,rule7S,rule8S
    global voisins,colormode , survies , naissances
    voisins=[]
    a,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
                
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_w :
                    pygame.quit()
                    break
                
                elif event.key ==pygame.K_ESCAPE:
                    CheckboxStart.checked = True
                    break
            Savelocation.analyse_event(event)
        
        fenetre.fill((52,78,91))
        
        printscreen("Birth cell rule",150,160,(0,0,0))
        printscreen("Commbient de voisins pour que la cellule soit vivante",0,177,(0,0,0))
        printscreen("Conway Game Of Life ",400,100,(0,0,0))
        printscreen("Commbient de voisins pour que la cellule Survive",600,177,(0,0,0))
        printscreen("Survive cell rule",750,160,(0,0,0))
        printscreen("Voisins check",1150,250,(0,0,0))
            
        if Checkbox0.draw(fenetre): rule0B=True
        else: rule0B=False
        if Checkbox1.draw(fenetre): rule1B=True
        else: rule1B=False
        if Checkbox2.draw(fenetre): rule2B=True
        else: rule2B=False
        if Checkbox3.draw(fenetre): rule3B=True
        else: rule3B=False
        if Checkbox4.draw(fenetre): rule4B=True
        else: rule4B=False
        if Checkbox5.draw(fenetre): rule5B=True
        else: rule5B=False
        if Checkbox6.draw(fenetre): rule6B=True
        else: rule6B=False
        if Checkbox7.draw(fenetre): rule7B=True
        else: rule7B=False
        if Checkbox8.draw(fenetre): rule8B=True
        else: rule8B=False
        if CheckboxCl.draw(fenetre): colormode=True
        else: colormode=False
        
        if Checkboxb0.draw(fenetre): rule0S=True
        else: rule0S=False
        if Checkboxb1.draw(fenetre): rule1S=True
        else: rule1S=False
        if Checkboxb2.draw(fenetre): rule2S=True
        else: rule2S=False
        if Checkboxb3.draw(fenetre): rule3S=True
        else: rule3S=False
        if Checkboxb4.draw(fenetre): rule4S=True
        else: rule4S=False
        if Checkboxb5.draw(fenetre): rule5S=True
        else: rule5S=False
        if Checkboxb6.draw(fenetre): rule6S=True
        else: rule6S=False
        if Checkboxb7.draw(fenetre): rule7S=True
        else: rule7S=False
        if Checkboxb8.draw(fenetre): rule8S=True
        else: rule8S=False
        
        if CheckboxStart.draw(fenetre):
            break
        if CheckboxQuit.draw(fenetre):
            pygame.quit()
            break
        
        
        
        """for i,j in enumerate([(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]):
            if CheckboxVs[i].draw(fenetre):
                voisins.append(j)"""
        
        if CheckboxVs[0].draw(fenetre):a=1
        else: a=0
        if CheckboxVs[1].draw(fenetre):a1=1
        else: a1=0
        if CheckboxVs[2].draw(fenetre):a2=1
        else: a2=0
        if CheckboxVs[3].draw(fenetre):a3=1
        else: a3=0
        if CheckboxVs[4].draw(fenetre):a4=1
        else: a4=0
        if CheckboxVs[5].draw(fenetre):a5=1
        else: a5=0
        if CheckboxVs[6].draw(fenetre):a6=1
        else: a6=0
        if CheckboxVs[7].draw(fenetre):a7=1
        else: a7=0
        if CheckboxVs[8].draw(fenetre):a8=1
        else: a8=0
        if CheckboxVs[9].draw(fenetre):a9=1
        else: a9=0
        if CheckboxVs[10].draw(fenetre):a10=1
        else: a10=0
        if CheckboxVs[11].draw(fenetre):a11=1
        else: a11=0
        if CheckboxVs[12].draw(fenetre):a12=1
        else: a12=0
        if CheckboxVs[13].draw(fenetre):a13=1
        else: a13=0
        if CheckboxVs[14].draw(fenetre):a14=1
        else: a14=0
        if CheckboxVs[15].draw(fenetre):a15=1
        else: a15=0
        if CheckboxVs[16].draw(fenetre):a16=1
        else: a16=0
        if CheckboxVs[17].draw(fenetre):a17=1
        else: a17=0
        if CheckboxVs[18].draw(fenetre):a18=1
        else: a18=0
        if CheckboxVs[19].draw(fenetre):a19=1
        else: a19=0
        if CheckboxVs[20].draw(fenetre):a20=1
        else: a20=0
        if CheckboxVs[21].draw(fenetre):a21=1
        else: a21=0
        if CheckboxVs[22].draw(fenetre):a22=1
        else: a22=0
        if CheckboxVs[23].draw(fenetre):a23=1
        else: a23=0
        if CheckboxVs[24].draw(fenetre):a24=1
        else: a24=0
            
        if BoutonSave.draw(fenetre):save()
        if BoutonLoad.draw(fenetre):load()
        if Savelocation.draw(fenetre):pass
        if boutonprint.draw(fenetre):pass
        
        
        
        pygame.display.update()

    if a ==1:voisins.append((-2, -2))
    if a1 ==1:voisins.append((-2, -1))
    if a2 ==1:voisins.append((-2, 0))
    if a3 ==1:voisins.append((-2, 1))
    if a4 ==1:voisins.append((-2, 2))
    if a5 ==1:voisins.append((-1, -2))
    if a6 ==1:voisins.append((-1, -1))
    if a7 ==1:voisins.append((-1, 0))
    if a8 ==1:voisins.append((-1, 1))
    if a9 ==1:voisins.append((-1, 2))
    if a10 ==1:voisins.append((0, -2))
    if a11 ==1:voisins.append((0, -1))        
    if a12 ==1:voisins.append((0, 0))
    if a13 ==1:voisins.append((0, 1))
    if a14 ==1:voisins.append((0, 2))
    if a15 ==1:voisins.append((1, -2))
    if a16 ==1:voisins.append((1, -1))
    if a17 ==1:voisins.append((1, 0))
    if a18 ==1:voisins.append((1, 1))
    if a19 ==1:voisins.append((1, 2))
    if a20 ==1:voisins.append((2, -2))
    if a21 ==1:voisins.append((2, -1))
    if a22 ==1:voisins.append((2, 0))
    if a23 ==1:voisins.append((2, 1))
    if a24 ==1:voisins.append((2, 2))
    
    if rule0B:naissances.append(0)
    if rule1B:naissances.append(1)
    if rule2B:naissances.append(2)
    if rule3B:naissances.append(3)
    if rule4B:naissances.append(4)
    if rule5B:naissances.append(5)
    if rule6B:naissances.append(6)
    if rule7B:naissances.append(7)
    if rule8B:naissances.append(8)
    
    if rule0S: survies.append(0)
    if rule1S: survies.append(1)
    if rule2S: survies.append(2)
    if rule3S: survies.append(3)
    if rule4S: survies.append(4)
    if rule5S: survies.append(5)
    if rule6S: survies.append(6)
    if rule7S: survies.append(7)
    if rule8S: survies.append(8)
    
    
#voisins=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
voisins=[]

menu()
print(survies)
print(naissances)       
print(voisins)
#endregion

mousePressed1=False
mousePressed2=False
vie = generationAleatoirejdlv()



import time
timer = time.monotonic()
time_interval = 0.01
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
run=True
while loop==True:
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        
        elif event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
              
            if event.key ==pygame.K_w:
                loop=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_r:
                vie=generationAleatoirejdlv()
            #elif event.key ==pygame.K_v:
            #    vie=initialiserCellules()
                
            elif event.key ==pygame.K_ESCAPE:
                CheckboxStart.checked = False
                voisins=[]
                menu()
            
            
            elif event.key ==pygame.K_PAGEUP:
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
            #    vie=initialiserCellules()
                vie=generationAleatoirejdlv()
            elif event.key ==pygame.K_PAGEDOWN:
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
            #    vie=initialiserCellules()
                vie=generationAleatoirejdlv()
                
            elif event.key ==pygame.K_RIGHT:
                if time_interval > 0: time_interval -= 0.1
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
            
            vie.add((mousepos[0]//CELLSIZE,mousepos[1]//CELLSIZE))
        if mousePressed2 and (mousepos[0]//CELLSIZE,mousepos[1]//CELLSIZE) in vie:
            vie.remove((mousepos[0]//CELLSIZE,mousepos[1]//CELLSIZE))

    fenetre.fill(background_color)
    remplirGrillejdlv(vie)
    #tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    if run and  time.monotonic() - timer > time_interval:
        timer = time.monotonic()
        st = time.monotonic()
        vie=prochaine_jdlvie(vie,survies,naissances,voisins    )#clock.tick(FPS)
        end = time.monotonic()
        print("time",end-st)

pygame.quit()

#endregion