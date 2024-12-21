from lib.boutton import Bouton, Boutonsprite #import de la class bouton
import subprocess
import pygame


pygame.init()

fenetre = pygame.display.set_mode()
l,h = fenetre.get_size()
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 10
WINDOWWIDTH = l
WINDOWHEIGHT = h-CELLSIZE*2

pygame.display.set_caption("Menu")
font = pygame.font.Font('freesansbold.ttf', 20)

def printscreen(text:str,x,y,color):
    txt=font.render(text,True,color)
    fenetre.blit(txt,(x,y))

#x, y, image, scale


# x , y , w , h, txt , colo , colo1 

jeu_de_la_vie_Conway = Bouton(0, 0, 200, 200, 'Jeu de la vie Conway',(0,0,0),(255,255,255))
day_and_night = Bouton(200, 0, 100, 100, 'day&night',(0,0,0),(255,255,255))
falling = Bouton(300, 0, 100, 100, '   sand',(0,0,0),(255,255,255))
additif = Bouton(400, 0, 100, 100, 'Additif',(0,0,0),(255,255,255))
highlif = Bouton(500, 0, 100, 100, 'Highlife',(0,0,0),(255,255,255))
immigration = Bouton(600, 0, 100, 100, 'Immigration',(0,0,0),(255,255,255))
ouExc = Bouton(700, 0, 100, 100, 'Ou exclusif',(0,0,0),(255,255,255))
Quadlife = Bouton(800, 0, 100, 100, '  Quadlife',(0,0,0),(255,255,255))
rule184 = Bouton(900, 0, 100, 100, ' Elementary',(0,0,0),(255,255,255))
Seeds = Bouton(1000, 0, 100, 100, ' seeds',(0,0,0),(255,255,255))
exit = Bouton(1266, 600, 100, 100, '      exit',(0,0,0),(255,255,255))
neuronelal = Bouton(1100, 0, 100, 100, 'neuronlal',(0,0,0),(255,255,255))
Cyclique = Bouton(1200, 0, 100, 100, 'Cyclique',(0,0,0),(255,255,255))
Etoile = Bouton(1300, 0, 100, 100, 'Etoile',(0,0,0),(255,255,255))
Dégrade = Bouton(200, 100, 100, 100, 'Dégradé',(0,0,0),(255,255,255))
Brain = Bouton(300, 100, 100, 100, 'Brain',(0,0,0),(255,255,255))
wireWorld = Bouton(400, 100, 100, 100, 'WireWorld',(0,0,0),(255,255,255))
Mandelbrot = Bouton(500, 100, 100, 100, 'Mandelbrot',(0,0,0),(255,255,255))
Func = Bouton(600, 100, 100, 100, 'Func',(0,0,0),(255,255,255))
Hexjdlv = Bouton(700, 100, 100, 100, 'Hex',(0,0,0),(255,255,255))
HexCycl = Bouton(800, 100, 100, 100, 'HexCycl',(0,0,0),(255,255,255))
HexNuro = Bouton(900, 100, 100, 100, 'HexNuro',(0,0,0),(255,255,255))
Energy = Bouton(1000, 100, 100, 100, 'Energy',(0,0,0),(255,255,255))
wave = Bouton(1100, 100, 100, 100, 'Wave',(0,0,0),(255,255,255))



run=True
while run:
    fenetre.fill((52,78,91))
    
    
    if jeu_de_la_vie_Conway.draw(fenetre):
        subprocess.run(["python", "jeu de la vie.py"])
        
    if day_and_night.draw(fenetre):
        subprocess.run(["python", "day&night.py"])
    
    
    if falling.draw(fenetre):
        subprocess.run(["python", "Sand/falling sand.py"])
    
    if additif.draw(fenetre):
        subprocess.run(["python", "Additif.py"])
        
    if highlif.draw(fenetre):
        subprocess.run(["python", "highlife.py"])
        
    if immigration.draw(fenetre):
        subprocess.run(["python", "immigration.py"])
        
    if ouExc.draw(fenetre):
        subprocess.run(["python", "ou exclusif.py"])
        
    if Quadlife.draw(fenetre):
        subprocess.run(["python", "Quadlife.py"])
        
    if rule184.draw(fenetre):
        subprocess.run(["python", "1dCellular.py"])
        
    if Seeds.draw(fenetre):
        subprocess.run(["python", "Seeds.py"])
    
    if neuronelal.draw(fenetre):
        subprocess.run(["python", "neuronlalcellular.py"])
        
    if Cyclique.draw(fenetre):
        subprocess.run(["python", "Cyclique.py"])
    
    if Etoile.draw(fenetre):
        subprocess.run(["python", "étoile.py"])
        
    if Dégrade.draw(fenetre):
        subprocess.run(["python", "Dégradé.py"])
    
    if Brain.draw(fenetre):
        subprocess.run(["python", "Brain.py"])
        
    if wireWorld.draw(fenetre):
        subprocess.run(["python", "wireworld.py"])
        
    if Mandelbrot.draw(fenetre):
        subprocess.run(["cmd.exe", "/c","Game Mandelbrot.bat"])
        
    if Func.draw(fenetre):
        subprocess.run(["python", "Func.py"])
        
    if Hexjdlv.draw(fenetre):
        subprocess.run(["python", "Hex/Hex.py"])
        
    if HexCycl.draw(fenetre):
        subprocess.run(["python", "Hex/HexCycl.py"])
        
    if HexNuro.draw(fenetre):
        subprocess.run(["python", "Hex/HexNuro.py"])
        
    if Energy.draw(fenetre):
        subprocess.run(["python", "Energy.py"])
        
    if wave.draw(fenetre):
        subprocess.run(["python", "Wave.py"])
        
    if exit.draw(fenetre):
        run=False
    
    
    
    printscreen("w pour quiter chaque jeu",150,300,(0,0,0))
    printscreen("r pour reload  chaque jeu",150,320,(0,0,0))
    printscreen("v pour effacer chaque jeu",150,340,(0,0,0))
    printscreen("espace pour pause chaque jeu",150,360,(0,0,0))
    printscreen("fleche gauche pour ralentire le jeu",150,380,(0,0,0))
    printscreen("fleche droite pour accelere le jeu",150,400,(0,0,0))
    printscreen("clique gauche pour mettre une cellule sur chaque jeu",150,420,(0,0,0))
    printscreen("clique droit pour effacer une cellule sur chaque jeu",150,440,(0,0,0))
    printscreen("les touche numériquer 1(&) a 7(è) pour changer de materiaux sur les falling sans",150,460,(0,0,0))
    printscreen("Echape pour Acceder au menu du jeu de la vie, de Cyclique, de Elementary, Neuro",150,480,(0,0,0))
    printscreen("t permetr sur hex Neuro de changer les règle en tant réel",150,500,(0,0,0))
    
    
    
    
    
    
    
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run=False
            quit()
        elif event.type == pygame.KEYDOWN:           
            if event.key == pygame.K_w:
                run=False
        
                
    pygame.display.update()









