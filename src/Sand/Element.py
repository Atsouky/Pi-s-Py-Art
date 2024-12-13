dictionairedescouleur = {
    
    1:(255,200,0),      #sable
    2:(0,0,255),        #eau
    3:(201,51,0),       #bois
    4:(255,0,0),        #feu
    5:(100,100,100),    #fumee
    6:(0,255,0),        #herbe
    7:(0,255,0),        #tige
    8:(153, 51, 0),     #Terre
    9:(200,10,0),       #feuv
    10:(130,130,130),   #pierre
    11:(0,200,255),     #glace
    
}

e = {
    
    'sable':1,
    'eau':2,
    'bois':3,
    'feu':4,
    'fumee':5,
    'herbe':6,
    'tige':7,
    'terre':8,
    'feuv':9,
    'pierre':10,
    'glace':11,
    
}



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
            ('@ => |u| / #create %1', 'fumee', 0),
            ('@ + @bis => / ?pierre', 'eau', 0),
        ],
        'fumee': [
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
            ('@ + @bis => / ?fumee', 'eau', 0),
        ],
        'pierre': [
            ('@ => @', None, 0),
        ],
        'glace': [
            ('@ => @', None, 0),
            ('@ + @bis => / ?eau', 'feu', 0),
            ('@ + @bis => / ?eau', 'feuv', 0),
        ]
    }




"""
###Documentation des règles


##Pour créer un nouvel element il faut utiliser le format suivant (avec une valeur >= 12) :  

dictionairedescouleur = {
    'valeur':(couleurR,couleurG,couleurB),   
}
e={
    'nom':valeur
}
elements = {
    'nom': []
}

le @ représente la cellule actuelle 
le => montre la transition vers son produit final 
##Pour ajouter une nouvelle regle à l'element, il faut utiliser le format suivant :

'nom': [
    ('@ => |d|', None, 0), #règle faisant tomber un element
]


##Toutes les règles pouvant être ajoutée au premier element du tuple :


@=>|d|              # règle faisant tomber un element

@=>|u|              # règle faisant monter un element

@=>_|d|_            # règle faisant tomber un element en bas à gauche ou en bas à droite

@=>_|u|_            # règle faisant tomber un element en haut à gauche ou en haut à droite

@=>@_@              # règle faisant glisser un element à droite ou à gauche

@=>@                # element statique

@=>None             # destruction de l'element

@+@bis=>            # règle complexe de réaction : element + elementbis => elementfinal



Pour toutes ces règles, certains paramètres doivent etre renseignés :

##Parametre :

Chaque paramètre doivent être renseigné sous la forme suivante (avec un /) :

@ => |u| / #create %10      # à 10% de chance de créer un nouvel element dans la cellule du dessus


%n : n chance sur 100
?element : spécifie un element par son nom
#create : crée un nouvel element
#shift : fait glisser un element
#destroy : fait disparaitre un element
*d : direction (uniquement pour statique)


##Règle complexe :

( @ + @bis => / ?element, elementreaction, 0)
    |               |               |
# règle       produit final     avec quel element faire la reaction


Exemple : La glace réagit avec le feu et donne de l'eau
'glace':[
    ('@ + @bis => / ?eau', 'feu', 0),
]
'herbe':[
    ('@ => @ / ?terre', None, 0),
    ('@ => |u| /#create %100', 'tige', 0),
    ('@ + @bis => / ?feuv', 'feu', 0),          <----- herbe + feu => feuv
    ('@ + @bis => / ?feuv', 'feuv', 0),         <----- herbe + feuv => feuv
]
'tige': [
        ('@ => @ / ?herbe *d', None, 0),
        ('@ => @ / ?tige *d', None, 0),
        ('@ => |u| /#shift %10', 'herbe', 0),
        ('@ + @bis => / ?feuv', 'feu', 0),      <----- tige + feu => feuv
        ('@ + @bis => / ?feuv', 'feuv', 0),     <----- tige + feuv => feuv
        ],

'feuv': [
            ('@ => None /%1', None, 0),
            ('@ + @bis => / ?fumee', 'eau', 0), <----- feuv + eau => fumee
        ],





##Que veut dire le 0 ou le 1 à la fin ?

0 : rien ne se passe
1 : cette règle n'est effectuée que si la cellule reste immobile

Exemple :   

sable:[
    (@ => |d| , None,0),  la cellule tombe
    (@ => _|d|_ , None,1),   si elle ne peut aller en bas elle reste immobile 
                            donc grace au 1 de la seconde règle elle tombe en bas à droite ou en bas à gauche
]

graphique : 
- => vide
# => sable


--------#-----          --------------          --------------
--------#-----          --------#-----          --------------
--------------   ==>    --------#-----  x2==>   --------------   ==> @ => |d| , None, 0
--------------          --------------          --------#-----
--------------          --------------          --------#-----



--------#-----          --------#-----       
--------#-----          -------###----      
--------------   ==>    ------#####---     ==> @ => |d| , None, 0
--------------          -----#######--         @ => _|d|_ , None, 0 ==> cela donne ce resultat car les deux règle sont effectuées a la suite
--------------          ----#########-    



--------#-----          --------------          --------------
--------#-----          --------------          --------------
--------------   x3==>  --------------   ==>    --------------     ==> @ => |d| , None, 0
--------------          ---------#----          --------------         @ => _|d|_ , None, 1  ==> cela donne ce resultat car les deux règle ne sont pas effectuées a la suite
--------------          ---------#----          --------##----                                   mais la seconde attend que la premiere ne soit plus effectuée

"""
