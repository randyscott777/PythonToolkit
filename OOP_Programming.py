'''
Object Oriented Programming (OOP) Concepts

class Dict(dict): # subclass

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs) 

    def append(self,key,value):
        self[key] = value
        
class Str(str): # subclass  
        
    def substr(self,start,length): # new method
        return self[start:start+length]
        
    def replace(self,old,new,count=None): # overriden method
        if count is None:
            return super().replace(old, new) # all occurrences
        else: # Replace only up to 'count' occurrences
            return super().replace(old, new, count)
            
# Monkey-Patching str
_original_replace = str.replace

# Define a new replace method
def new_replace(self, old, new, count=None):
    print(f"Replacing '{old}' with '{new}'")
    if count is None:
        return _original_replace(self, old, new)
    return _original_replace(self, old, new, count)

# Monkey-patch the str class
str.replace = new_replace
'''

print(__doc__)

class Dict(dict):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs) 

    def append(self,key,value):
        self[key] = value

dct = Dict({'a':1,'b':2,'c':3})
print('Before:',dct)
dct.append('d',4)
print('After append:',dct)

class Str(str):   
        
    def substr(self,start,length):
        return self[start:start+length]
        
    def replace(self,old,new,count=None):
        if count is None:
            return super().replace(old, new) # all occurrences
        else: # Replace only up to 'count' occurrences
            return super().replace(old, new, count)

s = Str('abcdefghi')
sub = s.substr(3,2)
print('\nFor string abcdefghi, substr(3,2) is:',sub)
s = s.replace('a','x')
print('replace("a","x") is:',s)

