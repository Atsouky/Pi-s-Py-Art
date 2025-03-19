



string = '@ + @bis => |u| /#create *d %10'

v=''
for i in string:
    if i != ' ':
        v=v+i
string = v
cmd = string.split('/')[0]
parameter = string.split('/')[1]



import re
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
    
        
print(result)
    


    



print(v) 
print(cmd)
print(parameter)



#après réflextion c mieux cette version mais trop tard
def symbolic(x,y,paterne,vie,next_vie,arg1=None,arg2=None,arg3=None):
    lst_args = [arg1,arg2,arg3]
    
    match paterne:
    
        case '@=>|d|':
            if arg1 == None:
                next_vie[x][y] = 0
            else:
                next_vie[x][y] = arg1

argfeu = {
    'arg1':'delete',
    'arg2':'6',
}

e  = {
    'feu':[
        ('@ => |d|',argfeu , 0),
    ]
}