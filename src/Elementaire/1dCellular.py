#Projet : Pi's Py Art
#Auteurs : Damien Gazi
import pygame
from random import randint
import sys
import os


project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.append(project_path)

from lib.boutton import Bouton , TextInput
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((0, 0), pygame.NOFRAME)
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)

# Variables de l'écran
info = pygame.display.get_surface().get_size()
cellcolor = (0, 255, 0)
CELLSIZE = 5

#offset de la écran
offset_x = 0
offset_y = 0

nbCellWidth=info[0]//CELLSIZE
nbCellHeight=info[1]//CELLSIZE
background_color = (0, 0, 0)
WINDOWWIDTH = info[0]
WINDOWHEIGHT = info[1]

ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)



import sys
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton

class MainWindow(QMainWindow):
     def __init__(self):
          super(MainWindow, self).__init__()
          loadUi(os.path.join("Elementaire","elementary.ui"), self)
          qpixmap=QPixmap(os.path.join("Elementaire","elementary.png"))
          
          self.salut = QtWidgets.QLineEdit(self)
          self.salut.setGeometry(530, 110, 200, 50)
          
          custboutton = QPushButton(self)
          custboutton.setText("Custom")
          custboutton.setGeometry(530, 170, 200, 50)
          
          self.label.setPixmap(qpixmap)
          
          self.label2.setStyleSheet("background-color: gray")
          
          custboutton.clicked.connect(self.custom)
          self.Start.clicked.connect(self.start)
          self.Exit.clicked.connect(self.exit)
          self.rule30.clicked.connect(self.rule_30)
          self.rule99.clicked.connect(self.rule_99)
          self.rule110.clicked.connect(self.rule_110)
          self.rule184.clicked.connect(self.rule_184)
          
     def convertbin(self,n:int):
        return [int(x) for x in bin(n)[2:].zfill(8)]
     def createRule(self,rule):
        a= self.convertbin(rule)
        
        dicte={
            '000':None,
            '001':None,
            '010':None,
            '011':None,
            '100':None,
            '101':None,
            '110':None,
            '111':None
            }
        for i,j in enumerate(dicte):
            
            dicte[j]=a[len(dicte)-i-1]
        return dicte
     def start(self):
         self.hide()

     def exit(self):
        sys.exit()

     def rule_30(self):
         global rule30R,rule110R,rule184R,rule99R
         rule110R=False
         rule99R=False
         rule184R=False
         rule30R=True

     def rule_99(self):
         global rule30R,rule110R,rule184R,rule99R,ruleMod
         ruleMod=False
         rule110R=False
         rule99R=True
         rule184R=False
         rule30R=False

     def rule_110(self):
         global rule30R,rule110R,rule184R,rule99R,ruleMod
         rule110R=True
         ruleMod=False
         rule99R=False
         rule184R=False
         rule30R=False

     def rule_184(self):
         global rule30R,rule110R,rule184R,rule99R,ruleMod
         rule110R=False
         rule99R=False
         ruleMod=False
         rule184R=True
         rule30R=False
    
     def custom(self):
         global rule30R,rule110R,rule184R,rule99R,ruleMod,ruleModDict
         rule110R=False
         rule99R=False
         rule184R=False
         rule30R=False
         ruleMod=True
         lab = self.salut.text()
         try: ruleModDict = self.createRule(int(lab))
         except: pass
         print(ruleModDict)


app = QApplication(sys.argv)
window = MainWindow()
window.show()





#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire():
    for x in range(nbCellWidth):
        vie[x][0]=randint(0,1)
    return vie
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            
            if vie[x][y]==1:
                if (10+x)< 255: cellcolor = (0,(10+x)%255,0)
                else: cellcolor = (0,255,0)
                pygame.draw.rect(fenetre, cellcolor, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
    

def prochaine_vie(vie):
    #next_vie=initialiserCellules()
    vs=''
    for i in range(nbCellWidth):
        for j in range(nbCellHeight):
            for dx in [-1, 0, 1]:
                if vie[(i+dx)%nbCellWidth][j]:
                    vs+=str(1)
                else:
                    vs+=str(0)
            
            #next_vie[i][j+1]=rule30[vs]
            if rule110R:
                vie[i][j+1]=rule110[vs]
            elif rule30R:
                vie[i][j+1]=rule30[vs]
            elif rule184R:
                vie[i][j+1]=rule184[vs]
            elif rule99R:
                vie[i][j+1]=rule99[vs]
            elif ruleMod:
                vie[i][j+1]=ruleModDict[vs]
            
            vs=''

    return vie
    
    
    


def convertbin(n:int):
    return [int(x) for x in bin(n)[2:].zfill(8)]

def createRule(rule):
    a= convertbin(rule)
    
    dicte={
        '000':None,
        '001':None,
        '010':None,
        '011':None,
        '100':None,
        '101':None,
        '110':None,
        '111':None
        }
    for i,j in enumerate(dicte):
        
        dicte[j]=a[len(dicte)-i-1]
    return dicte
        


rule30 = createRule(30)
rule110 = createRule(110)
rule184=createRule(184)
rule99 = createRule(86)



#menu



rule30R = False
rule110R = False
rule184R = False
rule99R = False
ruleMod = False
ruleModDict = {
    '000':None,
    '001':None,
    '010':None,
    '011':None,
    '100':None,
    '101':None,
    '110':None,
    '111':None
}


vie=initialiserCellules()

if rule184R:
    vie=generationAleatoire()
    
else : vie[nbCellWidth//2+1][0]=1

vie=prochaine_vie(vie)
#remplirGrille(vie)
    
mousePressed1=False
mousePressed2=False
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
               
            if event.key ==pygame.K_ESCAPE:
                window.show()
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_v:
                vie=initialiserCellules()
            elif event.key ==pygame.K_r:
                vie=generationAleatoire()
                
            elif event.key ==pygame.K_RIGHT:
                if time_interval > 0.01: time_interval -= 0.1
            elif event.key ==pygame.K_LEFT:
                time_interval += 0.1
            
                
            
                
            elif event.key ==pygame.K_PAGEUP:
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                
            elif event.key ==pygame.K_PAGEDOWN:
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                
                            
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                
                #vie=prochaine_vie(vie)
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
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=1
            
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0

    fenetre.fill(background_color)
    remplirGrille(vie)
    vie=prochaine_vie(vie)
    #tracerGrille()
    pygame.display.update()
    
    

pygame.quit()

#endregion