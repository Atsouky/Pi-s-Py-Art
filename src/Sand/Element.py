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




"""
###Documentation des règles


##pour crée un nouvelle element il faut utiliser le format suivant (valeur > 12):  

dictionairedescouleur = {
    'valeur':(couleurR,couleurG,couleurB),   
}
e={
    'nom':valeur
}
elements = {
    'nom': []
}


##pour ajouter une nouvelle regle a l'element il faut utiliser le format suivant:

'nom': [
    ('@ => |d|', None, 0), #règle faisant tomber un element
]

plusieur règle peuvent etre ajouter



##tout les règle du première element du tuple:


@=>|d|              # règle faisant tomber un element

@=>|u|              # règle faisant monter un element

@=>_|d|_            # règle faisant tomber un element en bas a gauche ou en bas a droite

@=>_|u|_            # règle faisant tomber un element en haut a gauche ou en haut a droite

@=>@_@              # règle faisant glisser un element a droite ou a gauche

@=>@                # element static

@=>None             #destruction de l'element

@+@bis=>            #règle complexe de réaction avec un autre element pour en donner un autre



Pour tout ces règle certain paramètres doivent etre renseignés:

##Parametre :

chaque paramètre doivent etre renseigner sous la forme suivante (avec un /) :

@ => |u| / #create %10      # a 10% de chance d crée un nouvel element dans la cellule du dessu


%n : n chance sur 100
?element : spécifie un element par son nom
#create : crée un nouvel element
#shift : fait glisser un element
#destroy : fait disparaitre un element
*d : direction (uniquement pour static)


##règle complexe :

( @ + @bis => / ?element, elementreaction, 0)
    |               |               |
# règle       produit final     avec quel element faire la reaction

exemple: la glace réagit avec le feu et donne de l'eau

glace:[
    ('@ + @bis => / ?eau', 'feu', 0),
]


##Que veux dire le 0 ou le 1 a la fin ?

0 : rien ne se passe
1 : cette règle n'est effectuée que si la cellule reste immobile

exemple:   #if vie[x][y] == next_vie[x][y]:

sable:[
    (@ => |d| , None,0),  la cellule tombe
    (@ => _|d|_ , None,1),   si elle ne peut aller en bas elle reste immobile 
                            donc grace au 1 de la seconde règle elle tombe en bas a droite ou en bas a gauche
]



"""