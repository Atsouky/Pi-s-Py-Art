#Projet : Pi's Py Art
#Auteurs : Damien Gazi & Jenny Richard
import pygame , time , re
from random import randint,choice
from Element import elements,dictionairedescouleur,e

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
CELLSIZE = 5

#offset de la écran
offset_x = 0
offset_y = 0

nbCellWidth=info[0]//CELLSIZE
nbCellHeight=info[1]//CELLSIZE
background_color = (0, 0, 0)
WINDOWWIDTH = info[0]
WINDOWHEIGHT = info[1]



import sys
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QVBoxLayout, QPushButton, QComboBox

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi("Sand/fond_sand.ui", self)
        qpixmap=QPixmap("data/sand game/sandbox.png")
        self.label.setPixmap(qpixmap)
        
        
        #combobox de la liste des éléments
       
        self.comboBox.addItems(elements.keys()) # créer une liste dans la parentèse 
        self.comboBox.activated[str].connect(self.onActivated)
        
        #combobox de la liste des couleurs
        
        exit= QPushButton("Quitter", self)
        start= QPushButton("Start", self)
        exit.setGeometry(350, 300, 100, 50)
        start.setGeometry(50, 300, 100, 50)
        
        exit.clicked.connect(self.exit)
        start.clicked.connect(self.start)
        # creating a push button
        sandb = QPushButton("sable", self)
        eaub = QPushButton("eau", self)
        boisb = QPushButton("bois", self)
        pierreb = QPushButton("pierre", self)
        terreb = QPushButton("terre", self)
        herbeb = QPushButton("herbe", self)
        

    # position du boutton
        sandb.setGeometry(400-375, 75, 200, 50)
        sandb.clicked.connect(self.sand)
        eaub.setGeometry(650-375, 75, 200, 50)
        eaub.clicked.connect(self.eau)
        boisb.setGeometry(400-375, 150, 200, 50)
        boisb.clicked.connect(self.bois)
        pierreb.setGeometry(650-375, 150, 200, 50)
        pierreb.clicked.connect(self.pierre)
        terreb.setGeometry(400-375, 225, 200, 50)
        terreb.clicked.connect(self.terre)
        herbeb.setGeometry(650-375, 225, 200, 50)
        herbeb.clicked.connect(self.herbe)
        

    # mettre une image sur le boutton
        sandb.setIcon(QIcon('data/icon/sable.png'))
        eaub.setIcon(QIcon('data/icon/eau.png'))
        boisb.setIcon(QIcon('data/icon/bois.png'))
        pierreb.setIcon(QIcon('data/icon/pierre.png'))
        terreb.setIcon(QIcon('data/icon/dirt.png'))
        herbeb.setIcon(QIcon('data/icon/harbe.png'))
        

    def onActivated(self, text):
        global seclecteur
        if text in elements.keys():
            seclecteur = e[text]
    
    def start(self):
        self.hide()
    
    def exit(self):
        sys.exit()

    def sand(self):
        global seclecteur
        seclecteur = e['sable']
        self.hide()

    def eau(self):
        global seclecteur 
        seclecteur = e['eau']
        self.hide()

    def bois(self):
        global seclecteur
        seclecteur = e['bois']
        self.hide()

    def pierre(self):
        global seclecteur
        seclecteur = e['feu']
        self.hide()

    def terre(self):
        global seclecteur
        seclecteur = e['terre']
        self.hide()

    def herbe(self):
        global seclecteur
        seclecteur = e['herbe']
        self.hide()

    

app = QApplication(sys.argv)
window = MainWindow()
window.show()





def initialiserCellules():
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]

def generationAleatoire():
    return [[randint(0,len(dictionairedescouleur)) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=0:
                colo = dictionairedescouleur[vie[x][y]]
                pygame.draw.rect(fenetre, colo, (x*CELLSIZE+offset_x, y*CELLSIZE+offset_y, CELLSIZE, CELLSIZE))
                        


def symbolic(x,y,Paterne,vie,next_vie,elementreaction = None):
    a = None
    b = None
    c = None
    d = None
    
    v=''
    for i in Paterne:
        if i != ' ':
            v+=i
    Paterne = v
    
    if Paterne.find('/') != -1:
        rule = Paterne.split('/')[0]
        parameter = Paterne.split('/')[1]
        Paterne = rule

        order = {'%': 'a', '?': 'b', '*': 'c', '#': 'd'}
        result = {var: None for var in order.values()}
        pattern = r"([#?%*][^#?%*]*)"
        matches = re.findall(pattern, parameter)
        for match in matches:
            for symbol, var in order.items():
                if match.startswith(symbol):
                    match = match.strip(symbol)
                    result[var] = match
                    break 
                    
        
        a = result['a']
        if a != None:
            a = int(a)
        b = result['b']
        c = result['c']
        d = result['d']
        

    
    match Paterne:
    
        case '@=>|d|':
            
            if d == None:
            
                if lbas(x,y,vie,next_vie):  
                    next_vie[x][y+1] = vie[x][y]
                    
                else:                       
                    next_vie[x][y] = vie[x][y]
                
            elif d == 'create':
                
                if lhaut(x,y,vie,next_vie) and randint(0,100) < a:  
                    next_vie[x][y+1] = e[elementreaction]
                    
            elif d == 'delete':
                
                if lbas(x,y,vie,next_vie) and randint(0,100) < a:  
                    if next_vie[x][y+1] == e[elementreaction]:
                        next_vie[x][y+1] = 0
                    
            elif d == 'shift':
                if whatdown(x,y,vie) == e[elementreaction] and randint(0,100) < a:
                    shiftdown(x,y,vie,next_vie,e[elementreaction])
                    return next_vie
                
                
            return next_vie 
            
        case '@=>|u|':
            
            if d == None:
            
                if lhaut(x,y,vie,next_vie) and randint(0,1000) < a:  
                    next_vie[x][y-1] = vie[x][y]
                    
                else:                       
                    next_vie[x][y] = vie[x][y]
            
            elif d == 'create':
                
                if lhaut(x,y,vie,next_vie) and randint(0,100) < a:  
                    next_vie[x][y-1] = e[elementreaction]
                    
            elif d == 'delete':
                
                if lhaut(x,y,vie,next_vie) and randint(0,100) < a:  
                    if next_vie[x][y-1] == e[elementreaction]:
                        next_vie[x][y-1] = 0
                    
            elif d == 'shift':
                if whatup(x,y,vie) == e[elementreaction] and randint(0,100) < a:
                    shiftup(x,y,vie,next_vie,e[elementreaction])
                    return next_vie
                    
                
            return next_vie
            
            
        
            
        case '@=>_|d|_':
            
            
                
            rd = randint(0,1)
            
            if ldroite(x,y,vie,next_vie):
                if rd == 0 and lbasdroite(x,y,vie,next_vie): 
                    next_vie[x+1][y+1] = vie[x][y]
                    next_vie[x][y] = 0
            elif lgauche(x,y,vie,next_vie):   
                if rd == 1 and lbasgauche(x,y,vie,next_vie): 
                    next_vie[x-1][y+1] = vie[x][y]
                    next_vie[x][y] = 0
                
            else: 
                next_vie[x][y] = vie[x][y]
        
            return next_vie
        
        case '@=>_|u|_':
            
            rd = randint(0,1)
            
            if ldroite(x,y,vie,next_vie):
                if rd == 0 and lhautdroite(x,y,vie,next_vie): 
                    next_vie[x+1][y-1] = vie[x][y]
                    next_vie[x][y] = 0
            elif lgauche(x,y,vie,next_vie):   
                if rd == 1 and lhautgauche(x,y,vie,next_vie): 
                    next_vie[x-1][y-1] = vie[x][y]
                    next_vie[x][y] = 0
                
            else: 
                next_vie[x][y] = vie[x][y]
        
            return next_vie
        
        case '@=>@_@':
            
            rd = randint(0,1)
            
            if rd == 0 and ldroite(x,y,vie,next_vie): 
                next_vie[x+1][y] = vie[x][y]
                next_vie[x][y] = 0
                
            elif rd == 1 and lgauche(x,y,vie,next_vie): 
                next_vie[x-1][y] = vie[x][y]
                next_vie[x][y] = 0
                
            else: 
                next_vie[x][y] = vie[x][y]
        
            return next_vie
        
        
            
        case '@=>@':
            
            if b == None:
                next_vie[x][y] = vie[x][y]
            else:
                if c == None:
                    if neigbour(x,y,vie,e[b]):
                        next_vie[x][y] = vie[x][y]
                elif c == 'd':
                    if whatdown(x,y,vie) == e[b]:
                        next_vie[x][y] = vie[x][y]
                    else:
                        next_vie[x][y] = 0
            
            
            
        
            
        case '@=>None':
            
            if randint(0,100) < a:
                next_vie[x][y] = 0
            else:
                next_vie[x][y] = vie[x][y]
            return next_vie
           
        case '@+@bis=>':
            if neigbour(x,y,vie,e[elementreaction]): 
                if b == 'None':
                    next_vie[x][y] = 0
                else:
                    next_vie[x][y] = e[b]
                    p=getneighbour(x,y,vie,e[elementreaction])
                    next_vie[p[0]][p[1]] = 0
            
    return next_vie
    
#region func

def neigbour(x,y,vie,elementreaction):
    for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        if dx+x <= nbCellWidth-1 and dx+x >= 0 and dy+y <= nbCellHeight-1 and dy+y >= 0:
            if vie[x+dx][y+dy] == elementreaction:
                return True 
def getneighbour(x,y,vie,elementreaction):
    for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        if dx+x <= nbCellWidth-1 and dx+x >= 0 and dy+y <= nbCellHeight-1 and dy+y >= 0:
            if vie[x+dx][y+dy] == elementreaction:
                return (x+dx,y+dy)
    
    

def shiftup(x,y,vie,next_vie,elementreaction):
    next_vie[x][y-1] = vie[x][y]
    next_vie[x][y] = elementreaction
    
def shiftdown(x,y,vie,next_vie,elementreaction):
    next_vie[x][y+1] = vie[x][y]
    next_vie[x][y] = elementreaction
               
def whatup(x,y,vie):
    return vie[x][y-1]

def whatdown(x,y,vie):
    return vie[x][y+1]

def lbas(x,y,vie,next_vie):
    if vie[x][y+1] == 0 and next_vie[x][y+1] == 0 and y+1<=nbCellHeight-1:
        return True
    
def lhaut(x,y,vie,next_vie):
    if vie[x][y-1] == 0 and next_vie[x][y-1] == 0 and y-1>=0:
        return True

def lbasdroite(x,y,vie,next_vie):
    if vie[x+1][y+1] == 0 and next_vie[x+1][y+1] == 0 and y+1<=nbCellHeight-1 and x+1<=nbCellWidth-1:
        return True

def lbasgauche(x,y,vie,next_vie):
    if vie[x-1][y+1] == 0 and next_vie[x-1][y+1] == 0 and y+1<=nbCellHeight-1 and x-1>=0:
        return True
    
def lhautdroite(x,y,vie,next_vie):
    if vie[x+1][y-1] == 0 and next_vie[x+1][y-1] == 0 and y-1>=0 and x+1<=nbCellWidth-1:
        return True
    
def lhautgauche(x,y,vie,next_vie):
    if vie[x-1][y-1] == 0 and next_vie[x-1][y-1] == 0 and y-1>=0 and x-1>=0:
        return True

def ldroite(x,y,vie,next_vie):
    if vie[x+1][y] == 0 and next_vie[x+1][y] == 0 and x+1<=nbCellWidth-1:
        return True

def lgauche(x,y,vie,next_vie):   
    if vie[x-1][y] == 0 and next_vie[x-1][y] == 0 and x-1>=0:
        return True
    


def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    # tout les elements sont dans le ficher elements pour des modification a volonter
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):        
            value = vie[x][y]     
            if value == 0:
                continue       
            
            nom = [k for k, v in e.items() if v == value][0]
            paterne = elements[nom]      
            for paterne in paterne:
                if paterne[2] == 0:
                    next_vie = symbolic(x, y, paterne[0], vie, next_vie, paterne[1])
                elif paterne[2] == 1:
                    if vie[x][y] == next_vie[x][y]:
                        next_vie = symbolic(x, y, paterne[0], vie, next_vie, paterne[1])
    
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



    
#endregion

#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------

            

vie=initialiserCellules()

pinceaux = 1
pinceauy = 1

pinceaux2 = False
pinceauy2 = False
pinceaux3 = False
pinceauy3 = False
pinceauyTime = time.monotonic()


#variable d'événement

mousePressed1 = False
mousePressed2 = False
middlePressed = False
last_mouse_pos = (0, 0)
seclecteur = 1
timer = time.monotonic()
time_interval = 0.01
loop = True
run = True


while loop:
    for event in pygame.event.get():  # les touche d'action
        if event.type == pygame.QUIT: 
            loop = False
        elif event.type == pygame.KEYDOWN: #quitter 
            if event.key == pygame.K_ESCAPE:
                window.show()
            elif event.key == pygame.K_SPACE: #pause
                run = not run
            elif event.key == pygame.K_v: #vider
                vie = initialiserCellules()
            elif event.key == pygame.K_r: #generation aléatoire
                vie = generationAleatoire()
                
            elif event.key in key:
                seclecteur=keyselecteur[event.key]
                
            elif event.key == pygame.K_a:
                last_mouse_pos = pygame.mouse.get_pos()
                middlePressed = True
            elif event.key == pygame.K_e:
               offset_x = 0
               offset_y = 0
               CELLSIZE = 5   
            
            
            
            elif event.key == pygame.K_RIGHT:
                pinceaux2 = True
            elif event.key == pygame.K_LEFT:                
                pinceaux3 = True
            elif event.key == pygame.K_UP:                
                if pinceauy-1>0:pinceauy3 = True
            elif event.key == pygame.K_DOWN:                
                pinceauy2 = True

                  
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_a:
                middlePressed = False
                
            elif event.key == pygame.K_RIGHT:
                pinceaux2 = False
            elif event.key == pygame.K_LEFT:                
                pinceaux3 = False
            elif event.key == pygame.K_UP:                
                pinceauy3 = False
            elif event.key == pygame.K_DOWN:                
                pinceauy2 = False
            
                
                
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
            
    if time.monotonic()-pinceauyTime>0.02:
        pinceauyTime = time.monotonic()
        if pinceaux2:
            pinceaux+=1
        if pinceauy2:
            pinceauy+=1
        if pinceaux3:
            if pinceaux-1>0:pinceaux-=1
        if pinceauy3:
            if pinceauy-1>0:pinceauy-=1
    
    mousepos = pygame.mouse.get_pos()
    grid_x = (mousepos[0] - offset_x) // CELLSIZE
    grid_y = (mousepos[1] - offset_y) // CELLSIZE
    grid_x -= pinceaux//2
    grid_y -= pinceauy//2
    if mousePressed1 and grid_x<nbCellWidth and grid_y<nbCellHeight:
        if vie[grid_x][grid_y] == 0:
            for i in range(pinceaux):
                for j in range(pinceauy):
                    if grid_x+i<nbCellWidth and grid_y+j<nbCellHeight and vie[grid_x+i][grid_y+j] == 0 :
                        vie[grid_x+i][grid_y+j] = seclecteur                    #placer une celule vivante
        
    if mousePressed2:
        for i in range(pinceaux):
            for j in range(pinceauy):
                if grid_x+i<nbCellWidth and grid_y+j<nbCellHeight and vie[grid_x+i][grid_y+j] != 0:
                    vie[grid_x+i][grid_y+j] = 0 # placer une celule mort
    
    fenetre.fill((0, 0, 0)) #remplir la fenetre de noir
    remplirGrille(vie)         #remplir la grille
    pygame.display.update() #mise a jour
    
    
    clock.tick(60)
    
    if run and time.monotonic() - timer > time_interval: # boucle de la simulation
        timer = time.monotonic()
        vie=prochaine_vie(vie)

pygame.quit()