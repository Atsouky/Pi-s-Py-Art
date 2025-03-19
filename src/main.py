#Projet : Pi's Py Art
#Auteurs : Jenny Richard

import pygame, sys
import subprocess

pygame.init()
fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")
font = pygame.font.SysFont('freesansbold.ttf', 150)
click=False
click1=False
# Récupération de la taille de l'écran
info = pygame.display.get_surface().get_size()
x=info[0]
y=info[1]
# importation des images
#image de fond
image0 =pygame.transform.scale (pygame.image.load("data/menu.png"),(info))
selectsim =pygame.transform.scale (pygame.image.load("data/sim.png"),(info))
selectjv =pygame.transform.scale(pygame.image.load("data/jeu de la vie.png"),(info))
option=pygame.transform.scale (pygame.image.load("data/option.png"),(x,y))
#image menu principal
start=pygame.transform.scale (pygame.image.load("data/start_b.png"),(x/5,y/9))
option_b=pygame.transform.scale (pygame.image.load("data/options_b.png"),(x/5,y/9))
quitter=pygame.transform.scale (pygame.image.load("data/quit_b.png"),(x/5,y/9))
#image pour le choix de simulation
back=pygame.transform.scale (pygame.image.load("data/back_b.png"),(x/5,y/9))
bouttons_jv=pygame.transform.scale (pygame.image.load("data/game of life/boutton_jv.png"),(x/5,y/3))
bouttons_sand=pygame.transform.scale (pygame.image.load("data/sand game/boutton_sand.png"),(x/5,y/3))
bouttons_other=pygame.transform.scale (pygame.image.load("data/others/boutton_other.png"),(x/5,y/3))
#image pour les differents automate du jeu de la vie
bouttons_brain=pygame.transform.scale (pygame.image.load("data/game of life/brain_b.png"),(x/5,y/3))
bouttons_day_night=pygame.transform.scale (pygame.image.load("data/game of life/day&night_b.png"),(x/5,y/3))
bouttons_hex=pygame.transform.scale (pygame.image.load("data/game of life/hex_b.png"),(x/5,y/3))
bouttons_hexcycl=pygame.transform.scale (pygame.image.load("data/game of life/hexcycl_b.png"),(x/5,y/3))
bouttons_hexnuro=pygame.transform.scale (pygame.image.load("data/game of life/hexnur_b.png"),(x/5,y/3))
bouttons_highlife=pygame.transform.scale (pygame.image.load("data/game of life/highlife_b.png"),(x/5,y/3))
bouttons_immigration=pygame.transform.scale (pygame.image.load("data/game of life/immigration_b.png"),(x/5,y/3))
bouttons_larger=pygame.transform.scale (pygame.image.load("data/game of life/larger_than_life_b.png"),(x/5,y/3))
bouttons_mnca=pygame.transform.scale (pygame.image.load("data/game of life/mnca_b.png"),(x/5,y/3))
bouttons_seeds=pygame.transform.scale (pygame.image.load("data/game of life/seeds_b.png"),(x/5,y/3))
bouttons_block=pygame.transform.scale (pygame.image.load("data/game of life/block_b.png"),(x/5,y/3))

bouttons_next=pygame.transform.scale (pygame.image.load("data/next_b.png"),(x/5,y/9))
bouttons_previous=pygame.transform.scale (pygame.image.load("data/previous_b.png"),(x/5,y/9))
#image pour les differentes simulation de jeu bac a sable
bouttons_paint=pygame.transform.scale (pygame.image.load("data/sand game/paint_b.png"),(x/5,y/3))
bouttons_wireworld=pygame.transform.scale (pygame.image.load("data/sand game/wireworld_b.png"),(x/5,y/3))
#image pour les autres simulations
bouttons_additife=pygame.transform.scale (pygame.image.load("data/others/additife_b.png"),(x/5,y/3))
bouttons_csv=pygame.transform.scale (pygame.image.load("data/others/csv_b.png"),(x/5,y/3))
bouttons_cyclique=pygame.transform.scale (pygame.image.load("data/others/cyclique_b.png"),(x/5,y/3))
bouttons_degrade=pygame.transform.scale (pygame.image.load("data/others/degradé_b.png"),(x/5,y/3))
bouttons_elementary=pygame.transform.scale (pygame.image.load("data/others/elementary_b.png"),(x/5,y/3))
bouttons_energy=pygame.transform.scale (pygame.image.load("data/others/energy_b.png"),(x/5,y/3))
bouttons_etoile=pygame.transform.scale (pygame.image.load("data/others/etoile_b.png"),(x/5,y/3))
bouttons_func=pygame.transform.scale (pygame.image.load("data/others/func_b.png"),(x/5,y/3))
bouttons_heat=pygame.transform.scale (pygame.image.load("data/others/heat_b.png"),(x/5,y/3))
bouttons_mandelbrot=pygame.transform.scale (pygame.image.load("data/others/mandelbrot_b.png"),(x/5,y/3))
bouttons_xor=pygame.transform.scale (pygame.image.load("data/others/ou_exlusif_b.png"),(x/5,y/3))
bouttons_pile=pygame.transform.scale (pygame.image.load("data/others/pile_b.png"),(x/5,y/3))
bouttons_quadlife=pygame.transform.scale (pygame.image.load("data/others/quadlife_b.png"),(x/5,y/3))
bouttons_wave=pygame.transform.scale (pygame.image.load("data/others/wave_b.png"),(x/5,y/3))
bouttons_nuro=pygame.transform.scale (pygame.image.load("data/others/nuro_b.png"),(x/5,y/3))

#differente boucle
sim=False
options=False
s_jv=False
s_jv1=False
s_sand=False
s_other=False
s_other1=False
s_other2=False


def printscreen(text:str,font,x:int,y:int,color):
        txt=font.render(text,True,color)
        fenetre.blit(txt,(x,y))

def menu():
    global click, click1
    global sim, options
    while True:
        fenetre.blit(image0,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 =fenetre.blit(start,(x/2.55,y/5))       
        button_2 =fenetre.blit(option_b,(x/2.55,y/3))
        button_4 = fenetre.blit(quitter,(x/2.55,y/2.1))
        if button_1.collidepoint((mx, my)):
            if click:
                sim=True
                select_sim()
        if button_2.collidepoint((mx, my)):
            if click:
                options=True
                settings()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        #printscreen("START",font,x/2.35,y/4.5,(0,0,255))
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_4)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()

def settings():
    global click, click1
    global options
    while options:
        click=False
        fenetre.blit(option,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = fenetre.blit(back,(x/12,y/20))
        if button_1.collidepoint((mx, my)):
            if click1:
                options=False
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click1 = True

        pygame.display.update() 

def select_sim():
    global click, click1
    global sim,s_jv,s_sand,s_other
    while sim:
        click=False
        fenetre.blit(selectsim,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = fenetre.blit(bouttons_jv,(x/2.55,y/3))
        button_2 = fenetre.blit(bouttons_sand,(x/6,y/3))
        button_3 = fenetre.blit(bouttons_other,(x/1.6,y/3))
        button_4 = fenetre.blit(back,(x/2.55,y/1.3))
        if button_1.collidepoint((mx, my)):
            if click1:
                sim=False
                s_jv=True
                select_jv()
        if button_2.collidepoint((mx, my)):
            if click1:
                sim=False
                s_sand=True
                select_sand()
        if button_3.collidepoint((mx, my)):
            if click1:
                sim=False
                s_other=True
                select_other()
        if button_4.collidepoint((mx, my)):
            if click1:
                sim=False
                menu()
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click1 = True

        pygame.display.update()

def select_jv():
    global click, click1
    global s_jv,sim,s_jv1
    while s_jv:
        click1=False
        fenetre.blit(selectjv,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = fenetre.blit(bouttons_jv,(x/2.55,y/7.5))
        button_2 = fenetre.blit(bouttons_brain,(x/6,y/7.5))
        button_3 = fenetre.blit(bouttons_day_night,(x/1.6,y/7.5))
        button_4 = fenetre.blit(back,(x/2.55,y/1.12))

        button_5 = fenetre.blit(bouttons_hex,(x/2.55,y/2))
        button_6 = fenetre.blit(bouttons_hexcycl,(x/6,y/2))
        button_7 = fenetre.blit(bouttons_hexnuro,(x/1.6,y/2))
        button_8 = fenetre.blit(bouttons_next,(x/1.55,y/1.12))

        if button_1.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "jeu de la vie.py"])
        if button_2.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Jeu de la vie/Brain.py"])
        if button_3.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Jeu de la vie/day&night.py"])
        if button_4.collidepoint((mx, my)):
            if click:
                s_jv=False
                sim=True
                select_sim()
        if button_5.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Hex/Hex.py"])
        if button_6.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Hex/HexCycl.py"])
        if button_7.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Hex/HexNuro.py"])     
        if button_8.collidepoint((mx, my)):
            if click:
                s_jv=False
                s_jv1=True
                select_jv1()
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def select_jv1():
    global click, click1
    global s_jv1,sim,s_jv
    while s_jv1:
        click=False
        fenetre.blit(selectjv,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = fenetre.blit(bouttons_highlife,(x/2.55,y/7.5))
        button_2 = fenetre.blit(bouttons_immigration,(x/6,y/7.5))
        button_3 = fenetre.blit(bouttons_larger,(x/1.6,y/7.5))
        button_4 = fenetre.blit(back,(x/2.55,y/1.12))

        button_5 = fenetre.blit(bouttons_mnca,(x/2.55,y/2))
        button_6 = fenetre.blit(bouttons_seeds,(x/6,y/2))
        button_7 = fenetre.blit(bouttons_previous,(x/7.25,y/1.12))
        button_8 = fenetre.blit(bouttons_block,(x/1.6,y/2))
        
        if button_1.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Jeu de la vie/highlife.py"])
        if button_2.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Jeu de la vie/immigration.py"])
        if button_3.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "MNCA/larger than life.py"])
        if button_4.collidepoint((mx, my)):
            if click1:
                s_jv1=False
                sim=True
                select_sim()
        if button_5.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Multi-neigborhood Cellular Automata.py"], cwd="MNCA")
                
        if button_6.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Jeu de la vie/Seeds.py"])  
        if button_7.collidepoint((mx, my)):
            if click1:
                s_jv1=False
                s_jv=True
                select_jv()
        if button_8.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Block.py"])
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click1 = True

        pygame.display.update()

def select_sand():
    global click, click1
    global sim,s_sand
    while s_sand:
        click1=False
        fenetre.blit(selectsim,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = fenetre.blit(bouttons_paint,(x/2.55,y/3))
        button_2 = fenetre.blit(bouttons_sand,(x/6,y/3))
        button_3 = fenetre.blit(bouttons_wireworld,(x/1.6,y/3))
        button_4 = fenetre.blit(back,(x/2.55,y/1.3))
        if button_1.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Autre automate/paint.py"])
        if button_2.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Sand/falling sand.py"])
        if button_3.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Autre automate/wireworld.py"])
        if button_4.collidepoint((mx, my)):
            if click:
                s_sand=False
                sim=True
                select_sim()
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click= False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def select_other():
    global click, click1
    global s_other,sim,s_other1
    while s_other:
        click1=False
        fenetre.blit(selectjv,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = fenetre.blit(bouttons_additife,(x/2.55,y/7.5))
        button_2 = fenetre.blit(bouttons_elementary,(x/6,y/7.5))
        button_3 = fenetre.blit(bouttons_csv,(x/1.6,y/7.5))
        button_4 = fenetre.blit(back,(x/2.55,y/1.12))

        button_5 = fenetre.blit(bouttons_cyclique,(x/3.5,y/2))
        button_6 = fenetre.blit(bouttons_degrade,(x/2,y/2))
        button_7 = fenetre.blit(bouttons_next,(x/1.55,y/1.12))

        if button_1.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Autre automate/Additif.py"])
        if button_2.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Elementaire/1dCellular.py"])
        if button_3.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "CSV file editor.py"], cwd='MNCA')
        if button_4.collidepoint((mx, my)):
            if click:
                s_other=False
                sim=True
                select_sim()
        if button_5.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Cyclique.py"])
        if button_6.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Autre automate/Dégradé.py"]) 
        if button_7.collidepoint((mx, my)):
            if click:
                s_other=False
                s_other1=True
                select_other1()
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def select_other1():
    global click, click1
    global s_other,sim,s_other1,s_other2
    while s_other1:
        click=False
        fenetre.blit(selectjv,(0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = fenetre.blit(bouttons_energy,(x/2.55,y/7.5))
        button_2 = fenetre.blit(bouttons_etoile,(x/6,y/7.5))
        button_3 = fenetre.blit(bouttons_func,(x/1.6,y/7.5))
        button_4 = fenetre.blit(back,(x/2.55,y/1.12))

        button_5 = fenetre.blit(bouttons_heat,(x/3.5,y/2))
        button_6 = fenetre.blit(bouttons_mandelbrot,(x/2,y/2))
        button_7 = fenetre.blit(bouttons_next,(x/1.55,y/1.12))
        button_8 = fenetre.blit(bouttons_previous,(x/7.25,y/1.12))

        if button_1.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Autre automate/Energy.py"])
        if button_2.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Autre projet/étoile.py"])
        if button_3.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Autre projet/Func.py"])
        if button_4.collidepoint((mx, my)):
            if click1:
                s_other1=False
                sim=True
                select_sim()
        if button_5.collidepoint((mx, my)):
            if click1:
                subprocess.run(["python", "Autre automate/Heat.py"])
        if button_6.collidepoint((mx, my)):
            if click1:
                subprocess.run(["cmd.exe", "/c","Autre projet/Game Mandelbrot.bat"]) 
        if button_7.collidepoint((mx, my)):
            if click1:
                s_other=False
                s_other2=True
                select_other2()
        if button_8.collidepoint((mx, my)):
            if click1:
                s_other1=False
                s_other=True
                select_other()
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click1 = True

        pygame.display.update()

def select_other2():
    global click, click1
    global s_other2,sim,s_other1
    while s_other2:
        click1=False
        fenetre.blit(selectjv,(0,0))

        mx, my = pygame.mouse.get_pos()
        button_1 = fenetre.blit(bouttons_xor,(x/2.55,y/7.5))
        button_2 = fenetre.blit(bouttons_pile,(x/6,y/7.5))
        button_3 = fenetre.blit(bouttons_quadlife,(x/2,y/2))
        button_4 = fenetre.blit(back,(x/2.55,y/1.12))
        button_7 = fenetre.blit(bouttons_nuro,(x/1.6,y/7.5))
        
        button_5 = fenetre.blit(bouttons_wave,(x/3.55,y/2))
        button_6 = fenetre.blit(bouttons_previous,(x/7.25,y/1.12))

        if button_1.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Autre projet/ou exclusif.py"])
        if button_2.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Autre automate/Pile de sable.py"])
        if button_3.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Jeu de la vie/Quadlife.py"])
        if button_4.collidepoint((mx, my)):
            if click:
                s_other2=False
                sim=True
                select_sim()
        if button_5.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "Autre automate/Wave.py"])  
        if button_6.collidepoint((mx, my)):
            if click:
                s_other2=False
                s_other1=True
                select_other1()
        if button_7.collidepoint((mx, my)):
            if click:
                subprocess.run(["python", "neuronalcellular.py"])
        #pygame.draw.rect(fenetre, (255, 0, 0), button_2)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        #pygame.draw.rect(fenetre, (255, 0, 0), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

menu()
