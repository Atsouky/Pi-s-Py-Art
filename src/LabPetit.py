



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