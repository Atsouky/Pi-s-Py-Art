"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""


import pygame
from random import randint
from lib.boutton import Checkbox,TextInput
import colorsys
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 10
offset_x=0
offset_y=0

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



import sys
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QVBoxLayout
import threading

class MainWindow(QMainWindow):
     def __init__(self,parent=None):
         
          super(MainWindow, self).__init__(parent)
          loadUi("fond_cycl.ui", self)
          qpixmap=QPixmap("data/cycl.png")
          self.label.setPixmap(qpixmap)
         
         #Chexbox pour Birth cell rule
          self.rule0.stateChanged.connect(self.checkedrule0)
          self.rule0.setStyleSheet("background-color: gray")
          self.rule1.stateChanged.connect(self.checkedrule1)
          self.rule1.setStyleSheet("background-color: gray")
          self.rule2.stateChanged.connect(self.checkedrule2)
          self.rule2.setStyleSheet("background-color: gray")
          self.rule3.stateChanged.connect(self.checkedrule3)
          self.rule3.setStyleSheet("background-color: gray")
          self.rule4.stateChanged.connect(self.checkedrule4)
          self.rule4.setStyleSheet("background-color: gray")
          self.rule5.stateChanged.connect(self.checkedrule5)
          self.rule5.setStyleSheet("background-color: gray")
          self.rule6.stateChanged.connect(self.checkedrule6)
          self.rule6.setStyleSheet("background-color: gray")
          self.rule7.stateChanged.connect(self.checkedrule7)
          self.rule7.setStyleSheet("background-color: gray")
          self.rule8.stateChanged.connect(self.checkedrule8)
          self.rule8.setStyleSheet("background-color: gray")
          self.modecolor.stateChanged.connect(self.checkedcolorfullb)
          self.modecolor.setStyleSheet("background-color: gray")

          self.Exit.clicked.connect(self.exit)
          self.Start.clicked.connect(self.start)

          
          
          

     def checkedrule0(self, checked):
        global rule0
        if checked:rule0 = True
        else:rule0 = False
        self.show()
        
     def checkedrule1(self, checked):
        global rule1
        if checked:rule1 = True
        else:rule1 = False
        self.show()
     

     def checkedrule2(self, checked):
        global rule2
        if checked:rule2 = True
        else:rule2 = False
        self.show()

     def checkedrule3(self, checked):
        global rule3
        if checked:rule3 = True
        else:rule3 = False
        self.show()

     def checkedrule4(self, checked):
        global rule4
        if checked:rule4 = True
        else:rule4 = False
        self.show()

     def checkedrule5(self, checked):
        global rule5
        if checked:rule5 = True
        else:rule5 = False
        self.show()

     def checkedrule6(self, checked):
        global rule6
        if checked:rule6 = True
        else:rule6 = False
        self.show()

     def checkedrule7(self, checked):
        global rule7
        if checked:rule7 = True
        else:rule7 = False
        self.show()

     def checkedrule8(self, checked):
        global rule8
        if checked:rule8 = True
        else:rule8 = False
        self.show()
     def checkedcolorfullb(self, checked):
        global rulec
        if checked:rulec = True
        else:rulec = False
        self.show()

     def start(self):
         global loopMenu,loopGame
         loopGame=True
         loopMenu=False
         
     def exit(self):
         quit()
         exit()
         





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
    return [[0 for i in range(nbCellHeight)] for j in range(nbCellWidth)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire(State):
    return [[randint(0, State - 1) for i in range(nbCellHeight)] for j in range(nbCellWidth)]
    

COLORS = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]



def generate_colors(State):
    colors = []
    for i in range(State):
        hue = i / State 
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  
        colors.append(tuple(int(c * 255) for c in rgb)) 
    return colors



#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    global COLORS, offset_y,offset_x
    c=10
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=0:
                try:colo = COLORS[vie[x][y]]
                except:colo = (c*vie[x][y],c*vie[x][y],c*vie[x][y])
                pygame.draw.rect(fenetre, colo, (x*CELLSIZE+offset_x, y*CELLSIZE+offset_y, CELLSIZE, CELLSIZE))
    


 


def voisin(x, y, vie):
    global State
    nbvoisin = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue 
            nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
            if vie[nx][ny] == (vie[x][y]+1) % State:
                nbvoisin += 1
    return nbvoisin



#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaine_vie(vie):
    global rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8
    next_vie = [[0] * (nbCellHeight) for i in range(nbCellWidth)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            a = voisin(x, y, vie)
            
            if rule0 and a==0: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule1 and a==1: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule2 and a==2: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule3 and a==3: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule4 and a==4: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule5 and a==5: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule6 and a==6: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule7 and a==7: next_vie[x][y] = (vie[x][y]+1)%State
            elif rule8 and a==8: next_vie[x][y] = (vie[x][y]+1)%State
            
            else:
                next_vie[x][y] = vie[x][y]  
            
            
            
            

    return next_vie

rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8=False,False,False,False,False,False,False,False,False



app = QApplication(sys.argv)
window = MainWindow()
window.show()



mousePressed1=False
mousePressed2=False
middlePressed=False

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




        
    

State = 4

vie=initialiserCellules()
vie=generationAleatoire(State)
loopGame=True

while loopGame:
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


sys.exit(app.exec())