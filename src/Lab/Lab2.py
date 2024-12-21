"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien Tg3
"""
import pygame , time , re
from random import randint,choice

#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran

cellcolor = (0,255,0)

clock = pygame.time.Clock()
pygame.init()

display_info = pygame.display.Info()
l = display_info.current_w
h = display_info.current_h - 75 #pour la barre de menu windows

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
    
dictionairedescouleur = {
    
    1:(255,200,0),      #sable
    2:(0,0,255),        #eau
    3:(201,51,0),       #bois
    4:(255,0,0),        #feu
    5:(100,100,100),    #steam
    6:(0,255,0),        #herbe
    7:(0,255,0),        #tige
    8:(153, 51, 0),     #Terre
    9:(200,10,0),       #feuv
    10:(130,130,130),   #stone
    11:(0,200,255),     #glace
    
}

e = {
    
    'sable':1,
    'eau':2,
    'bois':3,
    'feu':4,
    'steam':5,
    'herbe':6,
    'tige':7,
    'terre':8,
    'feuv':9,
    'stone':10,
    'glace':11,
    
}

#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=0:
                colo = dictionairedescouleur[vie[x][y]]
                pygame.draw.rect(fenetre, colo, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
                        


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
            
                if lhaut(x,y,vie,next_vie) and randint(0,100) < a:  
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
            
            
            
        case '@=>|u|#create':
            
            pass
            
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
    
import json
try:
    with open(f"saves/sand/sand.json", "r") as f:
        elements = json.load(f)
except FileNotFoundError:
    print("Aucune sauvegarde trouvée")

def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    elements = {
        'sable': [
            ('@ => |d|', None, 0),
            ('@ => _|d|_', None, 1),
        ],
        'eau': [
            ('@ => |d|', None, 0),
            ('@ => @_@', None, 1),
            ('@ + @bis=> / ? glace', 'glace', 1),
            ('@ => |u| /#shift %10', 'sable', 0),
        ],
        'bois': [
            ('@ => @', None, 0),
            ('@ + @bis => /?feuv', 'feuv', 0),
            ('@ + @bis => /?feuv', 'feu', 0),
        ],
        'feu': [
            ('@ => |d|', None, 0),
            ('@ => |u| / #create %1', 'steam', 0),
            ('@ + @bis => / ?stone', 'eau', 0),
        ],
        'steam': [
            ('@ => |u| / %20', None, 0),
            ('@ => |u| /#shift %10', 'feu', 0),
            
        ],
        'herbe': [
            ('@ => @ / ?terre', None, 0),
            ('@ => |u| /#create %100', 'tige', 0),
            ('@ + @bis => / ?feuv', 'feu', 0),
            ('@ + @bis => / ?feuv', 'feuv', 0),
        ],
        'tige': [
            ('@ => @ / ?herbe *d', None, 0),
            ('@ => @ / ?tige *d', None, 0),
            ('@ => |u| /#shift %10', 'herbe', 0),
            ('@ + @bis => / ?feuv', 'feu', 0),
            ('@ + @bis => / ?feuv', 'feuv', 0),
        ],
        'terre': [
            ('@ => @', None, 0),
        ],
        'feuv': [
            ('@ => None /%1', None, 0),
            ('@ + @bis => / ?steam', 'eau', 0),
        ],
        'stone': [
            ('@ => @', None, 0),
        ],
        'glace': [
            ('@ => @', None, 0),
            ('@ + @bis => / ?eau', 'feu', 0),
            ('@ + @bis => / ?eau', 'feuv', 0),
        ]
    }
    
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