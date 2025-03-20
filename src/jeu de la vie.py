#Projet : Pi's Py Art
#Auteurs : Damien Gazi & Jenny Richard

import pygame , time
from random import randint
#pourquoi que des comprhénsions?
#c'est plus rapide que des boucles for

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

# les menus

import os,sys
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
     def __init__(self,rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,
                  rule0S,rule1S,rule2S,rule3S,rule4S,rule5S,rule6S,rule7S,rule8S,vc1,
                  vc2,vc3,vc4,vc5,vc6,vc7,vc8,vc9,vc10,vc11,vc12,vc13,vc14,vc15,vc16,
                  vc17,vc18,vc19,vc20,vc21,vc22,vc23,vc24,vc25,parent=None):
          super(MainWindow, self).__init__()
          loadUi("fond_jv.ui", self)
          qpixmap=QPixmap(os.path.join("data","jeu de la vie.png"))
          self.label.setPixmap(qpixmap)
         
         #Chexbox pour Birth cell rule
          self.Birth.setStyleSheet("background-color: gray")
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

         #Chexbox pour survive cell rule
          self.Survive.setStyleSheet("background-color: gray")
          self.rule0S.stateChanged.connect(self.checkedrule0S)
          self.rule0S.setStyleSheet("background-color: gray")
          self.rule1S.stateChanged.connect(self.checkedrule1S)
          self.rule1S.setStyleSheet("background-color: gray")
          self.rule2S.stateChanged.connect(self.checkedrule2S)
          self.rule2S.setStyleSheet("background-color: gray")
          self.rule3S.stateChanged.connect(self.checkedrule3S)
          self.rule3S.setStyleSheet("background-color: gray")
          self.rule4S.stateChanged.connect(self.checkedrule4S)
          self.rule4S.setStyleSheet("background-color: gray")
          self.rule5S.stateChanged.connect(self.checkedrule5S)
          self.rule5S.setStyleSheet("background-color: gray")
          self.rule6S.stateChanged.connect(self.checkedrule6S)
          self.rule6S.setStyleSheet("background-color: gray")
          self.rule7S.stateChanged.connect(self.checkedrule7S)
          self.rule7S.setStyleSheet("background-color: gray")
          self.rule8S.stateChanged.connect(self.checkedrule8S)
          self.rule8S.setStyleSheet("background-color: gray")

         #Chexbox pour Voisin check
          self.Voisin.setStyleSheet("background-color: gray")
          self.vc1.stateChanged.connect(self.checkedvc1)
          self.vc2.stateChanged.connect(self.checkedvc2)
          self.vc3.stateChanged.connect(self.checkedvc3)
          self.vc4.stateChanged.connect(self.checkedvc4)
          self.vc5.stateChanged.connect(self.checkedvc5)
          self.vc6.stateChanged.connect(self.checkedvc6)
          self.vc7.stateChanged.connect(self.checkedvc7)
          self.vc8.stateChanged.connect(self.checkedvc8)
          self.vc9.stateChanged.connect(self.checkedvc9)
          self.vc10.stateChanged.connect(self.checkedvc10)
          self.vc11.stateChanged.connect(self.checkedvc11)
          self.vc12.stateChanged.connect(self.checkedvc12)
          self.vc13.stateChanged.connect(self.checkedvc13)
          self.vc14.stateChanged.connect(self.checkedvc14)
          self.vc15.stateChanged.connect(self.checkedvc15)
          self.vc16.stateChanged.connect(self.checkedvc16)
          self.vc17.stateChanged.connect(self.checkedvc17)
          self.vc18.stateChanged.connect(self.checkedvc18)
          self.vc19.stateChanged.connect(self.checkedvc19)
          self.vc20.stateChanged.connect(self.checkedvc20)
          self.vc21.stateChanged.connect(self.checkedvc21)
          self.vc22.stateChanged.connect(self.checkedvc22)
          self.vc23.stateChanged.connect(self.checkedvc23)
          self.vc24.stateChanged.connect(self.checkedvc24)
          self.vc25.stateChanged.connect(self.checkedvc25)
        
         #boutons start et exit
          self.Start.clicked.connect(self.start)
          self.Exit.clicked.connect(self.exit)
          
          self.ruelS = [self.rule0S,self.rule1S,self.rule2S,self.rule3S,self.rule4S,self.rule5S,self.rule6S,self.rule7S,self.rule8S]
          self.ruel = [self.rule0,self.rule1,self.rule2,self.rule3,self.rule4,self.rule5,self.rule6,self.rule7,self.rule8]
          self.ruelvc =[self.vc1,self.vc2,self.vc3,self.vc4,self.vc5,self.vc6,self.vc7,self.vc8,self.vc9,self.vc10,
                   self.vc11,self.vc12,self.vc13,self.vc14,self.vc15,self.vc16,self.vc17,self.vc18,self.vc19,self.vc20,
                   self.vc21,self.vc22,self.vc23,self.vc24,self.vc25]

          global ruleS,rulevc,rule
          for i in range(len(self.ruel)):
              if rule[i]==True:
                 self. ruel[i].setChecked(True)
              if ruleS[i]==True:
                  self.ruelS[i].setChecked(True)
          for i in range(len(rulevc)):
              if rulevc[i]==True:
                  self.ruelvc[i].setChecked(True)
         
    #region Check pour Birth cell rule
     def checkedrule0(self, checked):
        global rule0
        if checked:rule0=True
        else:rule0=False
        

     def checkedrule1(self, checked):
        global rule1
        if checked:rule1=True
        else:rule1=False
        

     def checkedrule2(self, checked):
        global rule2
        if checked:rule2=True
        else:rule2=False
        

     def checkedrule3(self, checked):
        global rule3
        if checked:rule3=True
        else:rule3=False
        

     def checkedrule4(self, checked):
        global rule4
        if checked:rule4=True
        else:rule4=False
        

     def checkedrule5(self, checked):
        global rule5
        if checked:rule5=True
        else:rule5=False
        

     def checkedrule6(self, checked):
        global rule6
        if checked:rule6=True
        else:rule6=False
        

     def checkedrule7(self, checked):
        global rule7
        if checked:rule7=True
        else:rule7=False
        

     def checkedrule8(self, checked):
        global rule8
        if checked:rule8=True
        else:rule8=False
        



     #Check pour survive cell rule
     def checkedrule0S(self, checked):
        global rule0S
        if checked:rule0S=True
        else:rule0S=False
        
        
     def checkedrule1S(self, checked):
        global rule1S
        if checked:rule1S=True
        else:rule1S=False
        

     def checkedrule2S(self, checked):
        global rule2S
        if checked:rule2S=True
        else:rule2S=False
        

     def checkedrule3S(self, checked):
        global rule3S
        if checked:rule3S=True
        else:rule3S=False
        

     def checkedrule4S(self, checked):
        global rule4S
        if checked:rule4S=True
        else:rule4S=False
        

     def checkedrule5S(self, checked):
        global rule5S
        if checked:rule5S=True
        else:rule5S=False
        

     def checkedrule6S(self, checked):
        global rule6S
        if checked:rule6S=True
        else:rule6S=False
        

     def checkedrule7S(self, checked):
        global rule7S
        if checked:rule7S=True
        else:rule7S=False
        

     def checkedrule8S(self, checked):
        global rule8S
        if checked:rule8S=True
        else:rule8S=False
        


    #Check pour Voisin check
     def checkedvc1(self, checked):
        global vc1
        if checked:vc1=True
        else:vc1=False
        
        
     def checkedvc2(self, checked):
        global vc2
        if checked:vc2=True
        else:vc2=False
        

     def checkedvc3(self, checked):
        global vc3
        if checked:vc3=True
        else:vc3=False
        

     def checkedvc4(self, checked):
        global vc4
        if checked:vc4=True
        else:vc4=False
        

     def checkedvc5(self, checked):
        global vc5
        if checked:vc5=True
        else:vc5=False
        

     def checkedvc6(self, checked):
        global vc6
        if checked:vc6=True
        else:vc6=False
        

     def checkedvc7(self, checked):
        global vc7
        if checked:vc7=True
        else:vc7=False
        

     def checkedvc8(self, checked):
        global vc8
        if checked:vc8=True
        else:vc8=False
        

     def checkedvc9(self, checked):
        global vc9
        if checked:vc9=True
        else:vc9=False
            
     def checkedvc10(self, checked):
        global vc10
        if checked:vc10=True
        else:vc10=False
        
        
     def checkedvc11(self, checked):
        global vc11
        if checked:vc11=True
        else:vc11=False
        

     def checkedvc12(self, checked):
        global vc12
        if checked:vc12=True
        else:vc12=False
        

     def checkedvc13(self, checked):
        global vc13
        if checked:vc13=True
        else:vc13=False
        

     def checkedvc14(self, checked):
        global vc14
        if checked:vc14=True
        else:vc14=False
        

     def checkedvc15(self, checked):
        global vc15
        if checked:vc15=True
        else:vc15=False
        

     def checkedvc16(self, checked):
        global vc16
        if checked:vc16=True
        else:vc16=False
        

     def checkedvc17(self, checked):
        global vc17
        if checked:vc17=True
        else:vc17=False
        

     def checkedvc18(self, checked):
        global vc18
        if checked:vc18=True
        else:vc18=False
        
     def checkedvc19(self, checked):
        global vc19
        if checked:vc19=True
        else:vc19=False
        
        
     def checkedvc20(self, checked):
        global vc20
        if checked:vc20=True
        else:vc20=False
        

     def checkedvc21(self, checked):
        global vc21
        if checked:vc21=True
        else:vc21=False
        

     def checkedvc22(self, checked):
        global vc22
        if checked:vc22=True
        else:vc22=False
        

     def checkedvc23(self, checked):
        global vc23
        if checked:vc23=True
        else:vc23=False
        

     def checkedvc24(self, checked):
        global vc24
        if checked:vc24=True
        else:vc24=False
        

     def checkedvc25(self, checked):
        global vc25
        if checked:vc25=True
        else:vc25=False
        
   #endregion
     
     
     def start(self):
         global rS,rV,rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule0S,rule1S,rule2S,rule3S,rule4S,rule5S,rule6S,rule7S,rule8S,voisins
         rS=[]
         rV=[]
         for i in range(9):
             if rule0:rV.append(0)
             if rule1:rV.append(1)
             if rule2:rV.append(2)
             if rule3:rV.append(3)
             if rule4:rV.append(4)
             if rule5:rV.append(5)
             if rule6:rV.append(6)
             if rule7:rV.append(7)
             if rule8:rV.append(8)
         for i in range(9):
             if rule0S:rS.append(0)
             if rule1S:rS.append(1)
             if rule2S:rS.append(2)
             if rule3S:rS.append(3)
             if rule4S:rS.append(4)
             if rule5S:rS.append(5)
             if rule6S:rS.append(6)
             if rule7S:rS.append(7)
             if rule8S:rS.append(8)
         voisins=[]
         #ligne 1
         if self.vc1.isChecked():voisins.append((-2,-2))
         if self.vc2.isChecked():voisins.append((-1,-2))
         if self.vc3.isChecked():voisins.append((0,-2))
         if self.vc4.isChecked():voisins.append((1,-2))
         if self.vc5.isChecked():voisins.append((2,-2))
         #ligne 2
         if self.vc16.isChecked():voisins.append((-2,-1))
         if self.vc19.isChecked():voisins.append((1,-1))
         if self.vc17.isChecked():voisins.append((-1,-1))
         if self.vc18.isChecked():voisins.append((0,-1))
         if self.vc6.isChecked():voisins.append((2,-1))
         #ligne 3
         if self.vc7.isChecked():voisins.append((2,0))
         if self.vc24.isChecked():voisins.append((-1,0))
         if self.vc20.isChecked():voisins.append((1,0))
         if self.vc15.isChecked():voisins.append((-2,0))
         #ligne 4
         if self.vc8.isChecked():voisins.append((2,1))
         if self.vc23.isChecked():voisins.append((-1,1))
         if self.vc22.isChecked():voisins.append((0,1))
         if self.vc21.isChecked():voisins.append((1,1))
         if self.vc14.isChecked():voisins.append((-2,1))
         #ligne 5
         if self.vc9.isChecked():voisins.append((2,2))
         if self.vc10.isChecked():voisins.append((1,2))
         if self.vc11.isChecked():voisins.append((0,2))
         if self.vc12.isChecked():voisins.append((-1,2))        
         if self.vc13.isChecked():voisins.append((-2,2))
         
         
         
         
         
         
         
         
         if self.vc25.isChecked():voisins.append(25)
         
         print(voisins)
         self.hide()
     
     def exit(self):
         quit()
         exit()
voisins=[]
vc1,vc2,vc3,vc4,vc5,vc6,vc7,vc8,vc9,vc10,vc11,vc12,vc13,vc14,vc15,vc16,vc17,vc18,vc19,vc20,vc21,vc22,vc23,vc24,vc25 = False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False
rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8 = False,False, False, True, False, False, False, False, False
rule0S,rule1S,rule2S,rule3S,rule4S,rule5S,rule6S,rule7S,rule8S = False,False, True, False, False, False, False, False, False
ruleS = [rule0S,rule1S,rule2S,rule3S,rule4S,rule5S,rule6S,rule7S,rule8S]
rulevc = [vc1,vc2,vc3,vc4,vc5,vc6,vc7,vc8,vc9,vc10,vc11,vc12,vc13,vc14,vc15,vc16,vc17,vc18,vc19,vc20,vc21,vc22,vc23,vc24,vc25]
rule = [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8]

rS = [2]
rV=[3]

app = QApplication(sys.argv)
window = MainWindow(rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,
                    rule0S,rule1S,rule2S,rule3S,rule4S,rule5S,rule6S,rule7S,rule8S,
                    vc1,vc2,vc3,vc4,vc5,vc6,vc7,vc8,vc9,vc10,vc11,vc12,vc13,vc14,vc15,vc16,vc17,vc18,vc19,vc20,vc21,vc22,vc23,vc24,vc25)
window.show()


def generationAleatoire(): # initialisation de la grille
    global vie, offset_x, offset_y 
    vie = { (x,y): 1 for x in range(info[0]//CELLSIZE) for y in range(info[1]//CELLSIZE) if randint(0, 1) == 0}

def remplirGrille(): # affiche la grille uniquement les cellule vivante et dans l'écran
    for (x, y) in vie:
        screen_x = (x * CELLSIZE) + offset_x
        screen_y = (y * CELLSIZE) + offset_y
        pygame.draw.rect(fenetre, cellcolor, (screen_x, screen_y, CELLSIZE, CELLSIZE))

def voisin(x, y): # calcule le nombre de voisin avec un compréhention
   global voisins
   return sum(vie.get((x+dx, y+dy), 0) for dx, dy in voisins)

def prochaine_vie(): # calcule la prochaine étape 
    global vie,rS,rV
    new_vie = {}
    #toute les cellule autour des cellule vivante
    candidates = set(vie.keys()) | { (x+dx, y+dy) for x, y in vie for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]}
    
    #calcule la prochaine étape
    for cell in candidates:
        n = voisin(*cell)
        if n in rV or (cell in vie and n in rS):
            new_vie[cell] = 1
    vie = new_vie

#variable d'événement

mousePressed1 = False
mousePressed2 = False
middlePressed = False
last_mouse_pos = (0, 0)

timer = time.monotonic()
time_interval = 0.01
loop = True
run = True

generationAleatoire()

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
            elif event.key == pygame.K_ESCAPE:
                window.show()
            elif event.key == pygame.K_a:
                last_mouse_pos = pygame.mouse.get_pos()
                middlePressed = True
            elif event.key == pygame.K_e:
               offset_x = 0
               offset_y = 0            
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
        vie[(grid_x, grid_y)] = 1 #placer une celule vivante
    if mousePressed2:
        vie.pop((grid_x, grid_y), None) # placer une celule mort
    
    fenetre.fill((0, 0, 0)) #remplir la fenetre de noir
    remplirGrille()         #remplir la grille
    pygame.display.update() #mise a jour
    
    if run and time.monotonic() - timer > time_interval: # boucle de la simulation
        timer = time.monotonic()
        prochaine_vie()

pygame.quit()