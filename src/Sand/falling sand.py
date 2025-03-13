"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien Tg3
"""
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



    


#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------

            

vie=initialiserCellules()



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
                loop = False
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
    if mousePressed1 and grid_x<nbCellWidth and grid_y<nbCellHeight:
        vie[grid_x][grid_y] = seclecteur #placer une celule vivante
    if mousePressed2:
        vie[grid_x][grid_y] = 0 # placer une celule mort
    
    fenetre.fill((0, 0, 0)) #remplir la fenetre de noir
    remplirGrille(vie)         #remplir la grille
    pygame.display.update() #mise a jour
    
    if run and time.monotonic() - timer > time_interval: # boucle de la simulation
        timer = time.monotonic()
        vie=prochaine_vie(vie)

pygame.quit()