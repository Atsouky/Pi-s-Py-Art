#Projet : Pi's Py Art
#Auteurs : Damien Gazi & Jenny Richard


import pygame,time,os,json
from random import randint,uniform
from math import * 
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
# pygame initialisation
clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((0, 0), pygame.NOFRAME)
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)

# Variables de l'écran
info = pygame.display.get_surface().get_size()
cellcolor = (0, 255, 0)
CELLSIZE = 10

#offset de la écran
offset_x = 0
offset_y = 0

nbCellWidth=info[0]//CELLSIZE
nbCellHeight=info[1]//CELLSIZE

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
          qpixmap=QPixmap(os.path.join("data","jeu de la vie.png"))
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
          self.l11 = QLineEdit(parent=self,text='x')
          
          
          
          
          self.number = [self.l1,self.l2,self.l3,self.l4,self.l5,self.l6,self.l7,self.l8,self.l9]
          self.ll = [self.l1,self.l2,self.l3,self.l4,self.l5,self.l6,self.l7,self.l8,self.l9,self.l10,self.l11]
          for i in self.number:
             i.setText(str(round(uniform(-1,1),4)))
          for i in range(11):
              self.ll[i].setStyleSheet("background-color: gray")
              self.ll[i].resize(200,50)
          
          self.l10.move(775,350) 
          self.l11.move(75,500)  
        
          k=0
          for i in range(3):
              for j in range(3):
                self.ll[k].move(75+i*210,160+j*55)
                k+=1
          
          
     def start(self):
         global voisins_fliter,activation_formula
         for i,j in enumerate(self.number):
             voisins_fliter[i][2] = float(j.text())
         
         activation_formula = compile_activation(self.l11.text())
         self.hide()
     def exit(self):
         quit()
         exit()
     def Random(self):
         for i in self.number:
             i.setText(str(round(uniform(-1,1),4)))
     
     def Save(self):
        
        data = {"text"+str(i):self.number[i].text() for i in range(len(self.number))}
        
        
        
        os.makedirs("saves", exist_ok=True)
        os.makedirs(os.path.join("saves","neuronal"), exist_ok=True)
        with open(os.path.join("saves","neuronal",f"{self.l10.text()}.json"), "w") as f:
            json.dump(data, f)
        
        
     
     def Load(self):
        try:
            with open(os.path.join("saves","neuronal",f"{self.l10.text()}.json"), "r") as f:
                data = json.load(f)
                for i,j in enumerate(data.values()):
                    self.number[i].setText(str(j)) 
            print("sauvegarde chargé")
            
        except FileNotFoundError:
            print("Aucune sauvegarde trouvée")
           
     




#initialise une liste de cellules CELLWIDTH*CELLHEIGHT
#les cellules seront toutes mortes
def initialiserCellules():
    return [[0.0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]

#Mettre des cellules vivantes au hasard
def generationAleatoire():
    return [[uniform(-1.0,1.0) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    



#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    global offset_x,offset_y
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            value = max(0.0, min(1.0, vie[x][y]))
            intensity = int(value * 255)   
            color = (max(0,intensity-100), 0, max(0,intensity-50))
            pygame.draw.rect(fenetre, color, (x * CELLSIZE+offset_x, y * CELLSIZE+offset_y, CELLSIZE, CELLSIZE))


#Détermine combien de voisins sont en vie
def voisin(x, y, vie):
    nbvoisin = 0.0
    for dx, dy, weight in voisins_fliter:
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        
        nbvoisin += vie[nx][ny] * weight
    return nbvoisin
 





#tuple contenant les valeurs des filtres pour un calcule plus efficace
voisins_fliter = [
    [-1, -1, 0.1], [0, -1, -0.1], [1, -1, 0.3],
    [-1, 0, 0.0], [0, 0, 1.0], [1, 0, -0.3],
    [-1, 1, -0.5], [0, 1, -0.1], [1, 1, 0.2]
]







#compilation de la formule d'activation entrer par l'utilisateur
def compile_activation(formula):
    code = compile(formula, "", "eval")
    return lambda x: max(0.0, min(1.0, eval(code, {"x": x, "sin": sin, "cos": cos , 'pi': pi, 'sqrt': sqrt , 'log': log1p , 'exp': exp , 'tan' : tan, 'abs': abs, 'min': min, 'max': max, 'round': round})))


    



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

activation_formula = compile_activation('x')

app = QApplication(sys.argv)
window = MainWindow()
window.show() 


vie=initialiserCellules()
#vie=generationAleatoire()


mousePressed1=False
mousePressed2=False
middlePressed=False
import time
timer = time.monotonic()
time_interval = 0.01
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
run=True
#region menu



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
                vie = initialiserCellules()
            elif event.key == pygame.K_r: #generation aléatoire
                vie=generationAleatoire()
            elif event.key == pygame.K_ESCAPE:
                window.show()
            elif event.key == pygame.K_a:
                last_mouse_pos = pygame.mouse.get_pos()
                middlePressed = True
            elif event.key == pygame.K_e:
               offset_x = 0
               offset_y = 0    
               CELLSIZE = 10
            
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_a:
                middlePressed = False
                
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