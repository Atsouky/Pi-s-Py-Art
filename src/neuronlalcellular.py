"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien
Version 0.1.8
"""
import pygame
from random import uniform
from lib.boutton import TextInput,Bouton
from math import *

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

import sys
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit

class MainWindow(QMainWindow):
     def __init__(self):
          super(MainWindow, self).__init__()
          loadUi("fond_nuro.ui", self)
          qpixmap=QPixmap("data/jeu de la vie.png")
          self.label.setPixmap(qpixmap)
         
         #Chexbox pour Birth cell rule
          self.label_2.setStyleSheet("background-color: gray")
          self.label_3.setStyleSheet("background-color: gray")
          self.label_4.setStyleSheet("background-color: gray")
          self.label_5.setStyleSheet("background-color: gray")

          self.Start.clicked.connect(self.start)
          self.Exit.clicked.connect(self.exit)
          self.random.clicked.connect(self.Random)
          self.load.clicked.connect(self.Load)
          self.save.clicked.connect(self.Save)
          
          self.l1 = QLineEdit(parent=self,text="0")
          self.l2 = QLineEdit(parent=self)
          self.l3 = QLineEdit(parent=self)
          self.l4 = QLineEdit(parent=self)
          self.l5 = QLineEdit(parent=self)
          self.l6 = QLineEdit(parent=self)
          self.l7 = QLineEdit(parent=self)
          self.l8 = QLineEdit(parent=self)
          self.l9 = QLineEdit(parent=self)
          self.l10 = QLineEdit(parent=self)
          
          self.l1.resize(200,100)
          self.l1.move(100,0)
          

     def start(self):
         pass
     
     def exit(self):
         
         pass
     def Random(self):
         pass
     
     def Save(self):
         pass
     
     def Load(self):
         pass
     


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec()) 

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

textinput10 = TextInput(10, 370, 440,64, 64)




#compilation de la formule d'activation entrer par l'utilisateur
def compile_activation(formula):
    code = compile(formula, "", "eval")
    return lambda x: max(0.0, min(1.0, eval(code, {"x": x, "sin": sin, "cos": cos , 'pi': pi, 'sqrt': sqrt , 'log': log1p , 'exp': exp , 'tan' : tan, 'abs': abs, 'min': min, 'max': max, 'round': round})))


    
textinput10.text="x"
activation_formula = compile_activation(textinput10.text)

#fonction d'activation
def activation(x):
    try:return activation_formula(x)
    except: return 0



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
    os.makedirs("saves/neuronal", exist_ok=True)
    with open(f"saves/neuronal/{savelocation}.json", "w") as f:
        json.dump(data, f)
    print("sauvegarde effectuer")
    boutonprint.txt = 'sauvegarde effectuer'


def load():
    try:
        with open(f"saves/neuronal/{savelocation}.json", "r") as f:
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
#region menu
textinput = TextInput(10, 10, 140, 32, 32)
textinput2 = TextInput(155, 10, 140, 32, 32)
textinput3 = TextInput(300, 10, 140, 32, 32)
textinput4 = TextInput(10, 50, 140, 32, 32)
textinput5 = TextInput(155, 50, 140, 32, 32)
textinput6 = TextInput(300, 50, 140, 32, 32)
textinput7 = TextInput(10, 90, 140, 32, 32)
textinput8 = TextInput(155, 90, 140, 32, 32)
textinput9 = TextInput(300, 90, 140, 32, 32)

boutonSave = Bouton(10, 130, 140, 32, 'Save', (0, 0, 0), (255, 255, 255))
boutonLoad = Bouton(10, 170, 140, 32, 'Load', (0, 0, 0), (255, 255, 255))
textinputSavelocation = TextInput(150, 150, 140, 32, 32)
boutonprint = Bouton(10, 210, 140, 32, '', (0, 0, 0), (255, 255, 255))

Bouton1 = Bouton(10, 450, 140, 32, 'Start', (0, 0, 0), (255, 255, 255))
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


    


#endregion
while loop:
    for event in pygame.event.get():  # les touche d'action
        if event.type == pygame.QUIT: 
            loop = False
        elif event.type == pygame.KEYDOWN: #quitter 
            if event.key == pygame.K_w:
                loop = False
            elif event.key == pygame.K_SPACE: #pause
                run = not run
            elif event.key == pygame.K_v: #vider
                vie = {}
            elif event.key == pygame.K_r: #generation aléatoire
                generationAleatoire()
        elif event.type == pygame.MOUSEBUTTONDOWN: #les click de la souris
            if event.button == 1:
                mousePressed1 = True
            elif event.button == 3:
                mousePressed2 = True
            elif event.button == 2:
                middlePressed = True
                last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mousePressed1 = False
            elif event.button == 3:
                mousePressed2 = False
            elif event.button == 2:
                middlePressed = False
        elif event.type == pygame.MOUSEMOTION and middlePressed: #le mouvelement de la souris avec le click mollette pour déplace l'offset
            new_mouse_pos = pygame.mouse.get_pos()
            dx = new_mouse_pos[0] - last_mouse_pos[0]
            dy = new_mouse_pos[1] - last_mouse_pos[1]
            offset_x += dx
            offset_y += dy
            last_mouse_pos = new_mouse_pos
        elif event.type == pygame.MOUSEWHEEL:     # le zoom avec la mollette de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            old_cellsize = CELLSIZE
            CELLSIZE = max(2, min(50, CELLSIZE + event.y))  
            scale_factor = CELLSIZE / old_cellsize
            offset_x = int(mouse_x - (mouse_x - offset_x) * scale_factor)
            offset_y = int(mouse_y - (mouse_y - offset_y) * scale_factor)
            
    
    mousepos = pygame.mouse.get_pos()
    grid_x = (mousepos[0] - offset_x) // CELLSIZE
    grid_y = (mousepos[1] - offset_y) // CELLSIZE
    if mousePressed1:
        vie[grid_x][grid_y] = 1 #placer une celule vivante
    if mousePressed2:
        vie[grid_x][grid_y] = 0 # placer une celule mort
    
    fenetre.fill((0, 0, 0)) #remplir la fenetre de noir
    remplirGrille(vie)         #remplir la grille
    pygame.display.update() #mise a jour
    
    if run and time.monotonic() - timer > time_interval: # boucle de la simulation
        timer = time.monotonic()
        vie=prochaine_vie(vie)

pygame.quit()