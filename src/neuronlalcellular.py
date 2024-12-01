"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien
Version 0.1.5
"""
import pygame
from random import uniform
from boutton import TextInput,Bouton
from math import *
#test
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'écrans
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 7
background_color=(0,0,0)
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE
screen =(WINDOWWIDTH,WINDOWHEIGHT)

pygame.init()
fenetre = pygame.display.set_mode(screen,pygame.RESIZABLE)
pygame.display.set_caption("Neuronal")
font = pygame.font.Font('freesansbold.ttf', 20)
#endregion



#initialise une liste de cellules CELLWIDTH*CELLHEIGHT
#les cellules seront toutes mortes
def initialiserCellules():
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]

#Mettre des cellules vivantes au hasard
def generationAleatoire():
    return [[uniform(-1.0,1.0) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    
def rescale(vie):
    nvie = [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    for x in range(min(len(vie), nbCellWidth)):
        for y in range(min(len(vie[0]), nbCellHeight)):
            nvie[x][y] = vie[x][y]
            
    return nvie


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            value = max(0.0, min(1.0, vie[x][y]))
            intensity = int(value * 255)   
            color = (max(0,intensity-100), 0, max(0,intensity-50))
            pygame.draw.rect(fenetre, color, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))


#Détermine combien de voisins sont en vie
def voisin(x, y, vie):
    nbvoisin = 0.0
    for dx, dy, weight in voisins_fliter:
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        nbvoisin += vie[nx][ny] * weight
    return nbvoisin
 



#dictionnaire des filtres pour la fonction voisin
filtere = {
    "-1,-1": 0.1, "0,-1": -0.1, "1,-1": 0.3,
    "-1,0": 0.0, "0,0": 1.0, "1,0": -0.3,
    "-1,1": -0.5, "0,1": -0.1, "1,1": 0.2
}
#tuple contenant les valeurs des filtres pour un calcule plus efficace
voisins_fliter = [
    [-1, -1, 0.1], [0, -1, -0.1], [1, -1, 0.3],
    [-1, 0, 0.0], [0, 0, 1.0], [1, 0, -0.3],
    [-1, 1, -0.5], [0, 1, -0.1], [1, 1, 0.2]
]

textinput10 = TextInput(10, 370, 140, 32, 16)

#compilation de la formule d'activation entrer par l'utilisateur
def compile_activation(formula):
    try:
        code = compile(formula, "<string>", "eval")
        return lambda x: max(0.0, min(1.0, eval(code, {"x": x, "__builtins__": None})))
    except Exception as e:
        print(f"Failed to compile formula: {e}")
        return lambda x: 0.0  
    
textinput10.text="x"
activation_formula = compile_activation(textinput10.text)

#fonction d'activation
def activation(x):
    return activation_formula(x)



#calcule la prochaine étape, retourne une nouvelle liste

def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):

            next_vie[x][y] = activation(voisin(x, y, vie))

    return next_vie


import os 
import json
savelocation ='save'
def save():
    data = {
        "txt1" : textinput.text,
        "txt2" : textinput2.text,
        "txt3" : textinput3.text,
        "txt4" : textinput4.text,
        "txt5" : textinput5.text,
        "txt6" : textinput6.text,
        "txt7" : textinput7.text,
        "txt8" : textinput8.text,
        "txt9" : textinput9.text,
        "txt10" : textinput10.text
    }
    os.makedirs("saves", exist_ok=True)
    with open(f"saves/{savelocation}.json", "w") as f:
        json.dump(data, f)
    print("sauvegarde effectuer")
    boutonprint.txt = 'sauvegarde effectuer'


def load():
    try:
        with open(f"saves/{savelocation}.json", "r") as f:
            data = json.load(f)
            textinput.text = data["txt1"]
            textinput2.text = data["txt2"]
            textinput3.text = data["txt3"]
            textinput4.text = data["txt4"]
            textinput5.text = data["txt5"]
            textinput6.text = data["txt6"]
            textinput7.text = data["txt7"]
            textinput8.text = data["txt8"]
            textinput9.text = data["txt9"]
            textinput10.text = data["txt10"]
        print("sauvegarde chargé")
        boutonprint.txt = 'sauvegarde chargé'
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée")
        boutonprint.txt = 'Aucune sauvegarde trouvée'
    
    


vie=initialiserCellules()
#vie=generationAleatoire()


mousePressed1=False
mousePressed2=False
import time
timer = time.monotonic()
time_interval = 0.01
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
run=True

textinput = TextInput(10, 10, 140, 32, 16)
textinput2 = TextInput(155, 10, 140, 32, 16)
textinput3 = TextInput(300, 10, 140, 32, 16)
textinput4 = TextInput(10, 50, 140, 32, 16)
textinput5 = TextInput(155, 50, 140, 32, 16)
textinput6 = TextInput(300, 50, 140, 32, 16)
textinput7 = TextInput(10, 90, 140, 32, 16)
textinput8 = TextInput(155, 90, 140, 32, 16)
textinput9 = TextInput(300, 90, 140, 32, 16)

boutonSave = Bouton(10, 130, 140, 32, 'Save', (0, 0, 0), (255, 255, 255))
boutonLoad = Bouton(10, 170, 140, 32, 'Load', (0, 0, 0), (255, 255, 255))
textinputSavelocation = TextInput(150, 150, 140, 32, 16)
boutonprint = Bouton(10, 210, 140, 32, '', (0, 0, 0), (255, 255, 255))

Bouton1 = Bouton(10, 410, 140, 32, 'Start', (0, 0, 0), (255, 255, 255))
Bouton2 = Bouton(450, 10, 140, 32, 'Random', (0, 0, 0), (255, 255, 255))
BoutonExit = Bouton(WINDOWWIDTH - 150, WINDOWHEIGHT - 50, 140, 32, 'Exit', (0, 0, 0), (255, 255, 255))
txt=[textinput,textinput2,textinput3,textinput4,textinput5,textinput6,textinput7,textinput8,textinput9,textinput10,textinputSavelocation]



textinput.text="0.1"
textinput2.text="-0.1"
textinput3.text="0.3"
textinput4.text="0.0"
textinput5.text="1.0"
textinput6.text="-0.3"
textinput7.text="-0.5"
textinput8.text="-0.1"
textinput9.text="0.2"
textinput10.text="x"

def menu():
    global filtere,activation_formula , voisins_fliter,savelocation
    while True:
        
        fenetre.fill((0, 0, 0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()        
            
            elif event.type == pygame.KEYDOWN: 
                if event.key ==pygame.K_w:
                    pygame.quit()
                elif event.type == pygame.K_ESCAPE:
                    Bouton1.action = True
                    break
            for i in txt:
                i.analyse_event(event)    
                
        if boutonSave.draw(fenetre):
            save()
            
        if boutonLoad.draw(fenetre):
            load()    
        
        if BoutonExit.draw(fenetre):
            pygame.quit()
                    
        if Bouton1.draw(fenetre):
            break     
                    
        if boutonprint.draw(fenetre):
            pass
        
        if Bouton2.draw(fenetre):
            textinput.text=str(round(uniform(-1.0,1.0),2))
            textinput2.text=str(round(uniform(-1.0,1.0),2))
            textinput3.text=str(round(uniform(-1.0,1.0),2))
            textinput4.text=str(round(uniform(-1.0,1.0),2))
            textinput5.text=str(round(uniform(-1.0,1.0),2))
            textinput6.text=str(round(uniform(-1.0,1.0),2))
            textinput7.text=str(round(uniform(-1.0,1.0),2))
            textinput8.text=str(round(uniform(-1.0,1.0),2))
            textinput9.text=str(round(uniform(-1.0,1.0),2))
            

        
        for i in txt:
            i.draw(fenetre)
            
        if textinputSavelocation.text!="save" or textinputSavelocation.text!="":
            savelocation = textinputSavelocation.text
        
        pygame.display.update()
            
    for i in txt:
        if i.text!="":
            filtere = {
                "-1,-1": float(textinput.text), "0,-1": float(textinput2.text), "1,-1": float(textinput3.text),
                "-1,0": float(textinput4.text), "0,0": float(textinput5.text), "1,0": float(textinput6.text),
                "-1,1": float(textinput7.text), "0,1": float(textinput8.text), "1,1": float(textinput9.text)
            }
            
            
    for i,j in enumerate(voisins_fliter):
        voisins_fliter[i][2]=filtere[str(j[0])+","+str(j[1])]
        

    activation_formula = compile_activation(textinput10.text)
    
menu()

while loop==True:
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False       
        
        elif event.type == pygame.VIDEORESIZE:
            fenetre = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
            nbCellWidth = event.w // CELLSIZE
            nbCellHeight = event.h // CELLSIZE
            vie = rescale(vie)
        
        elif event.type == pygame.KEYDOWN:  
  
            if event.key ==pygame.K_w:
                loop=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_r:
                vie=generationAleatoire()
            elif event.key ==pygame.K_v:
                vie=initialiserCellules()
                
            elif event.key ==pygame.K_ESCAPE:
                menu()
                
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
                
        elif event.type == pygame.MOUSEWHEEL:
            if event.y>0:
                #if CELLSIZE < min(WINDOWWIDTH, WINDOWHEIGHT):
                    CELLSIZE+=1
                    CELLWIDTH = WINDOWWIDTH // CELLSIZE
                    CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                    vie = rescale(vie)

            elif event.y<0:
                if CELLSIZE>1:
                    CELLSIZE-=1
                    nbCellWidth = WINDOWWIDTH // CELLSIZE
                    nbCellHeight = WINDOWHEIGHT // CELLSIZE
                    vie = rescale(vie)

            
    if mousepos[0]<nbCellWidth*CELLSIZE and mousepos[1]<nbCellHeight*CELLSIZE: 
        if mousePressed1:
            
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=1
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0

    
    if run and  time.monotonic() - timer > time_interval:
        timer = time.monotonic()
        vie=prochaine_vie(vie)
    
    
    fenetre.fill(background_color)
    remplirGrille(vie)
    pygame.display.update()

pygame.quit()

#endregion