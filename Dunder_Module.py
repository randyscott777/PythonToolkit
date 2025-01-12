'''
DUNDER_MODULE - DUNDER MAGIC METHODS

Initialization and Construction:
__new__ = for creating immutable objects (str,int,tuple), singleton, etc
__init__
__del__

Numeric methods:
__trunc__
__ceil__
__floor__
__round__
__invert__
__abs__
__neg__
__pos__

Arithmetic operators:
__add__
...

String methods:
__str__
__repr__
...

Comparison methods:
...
'''
import math

class Dunder_Class:
    instances = {} # class level variable
    
    def __new__(cls,*args,**kwargs):
        print('\nCreated a new instance of',cls.__name__)
        print('Instance name is',args[0])
        return super().__new__(cls)
    
    def __init__(self,inst,name,age=76,num=1.1,nums=[0,1,2,3,4,5,6,7,8,9]):
        self.inst = inst
        self.name = name
        self.age = age
        self.num = num
        self.nums = nums
        self.__class__.instances[self.inst] = {'name':self.name,'age':self.age}
        print(f'Initialized instance {self.inst} name={self.name}, and age ={self.age}')
  
    def __instancecheck__(self,other):
        return True

    def __repr__(self): # representation instead of displaying it's address
        return f'instance:{self.inst}, name:{self.name}, age:{self.age}'

    def __str__(self): # representation instead of displaying it's address
        return f'{self.inst} has name={self.name} and age={self.age}'

    def __eq__(self,other): # ==
        return self.name == other.name
    
    def __and__(self,other): # &
        return self.age + other.age
    
    def __or__(self,other): # |
        return [self.name,other.name]
    
    def __rshift__(self,other): # >>
        return [self.age,other.age]
       
    def __index__(self,other): # [x]
        return index(other) + 1
          
    def __divmod__(self,other): # other is the mod#
        return (self.age // other, self.age % other)
             
    def __mod__(self,other): # % other is the mod#
        return divmod(self.age,other)
             
    def __neg__(self): # -x floor
        return int(self.num // 1) 
       
    def __pos__(self): # +x ceiling
        return -int(-self.num // 1)
       
    def __invert__(self): # ~ convert to hex
        return hex(int(self.num))
       
    def __getitem__(self,key): # index via [x]
        return self.nums[key]

print(__doc__)

r = Dunder_Class('r','Randy')
R = Dunder_Class('R','Randy',age=0)
d = Dunder_Class('d','Donna',age=71)
m = Dunder_Class('m','Myrtle',age=16)

print('\n__repr__ for d is',d)
print('__str__ for d is',str(d))
print('All instances and values are',Dunder_Class.instances)
print('__dict__ is',r.__dict__)
x = 1
print('x=1 is instance of Dunder_Class',isinstance(x,Dunder_Class))
print('\nR and r are equal if the names are the same',R==r)
print('Total ages for instances is',r&d)
print('Names in instances are',r|d)
print('Ages in instances is',r>>d)
print('The sequence/indexer of nums[3] is',r.nums[3])
print('\ndivmod 10 of self.age is',divmod(r.age,10))
print('Division and % 10 of self.age is',r%10)
print('Floor of self.num = 1.1 is',(-r))
print('Ceiling of self.num = 1.1 is',(+r))
r.num = 12
print('Hex of self.num = 12 is',(~r))
print('Index 2 of self.nums is',r.nums[2])
#TODO: __reduce__,__index__,__class__,__modules__,__instances__,__getitem__ for dict

print('dir(Dunder_Class) is',dir(Dunder_Class))
input('Pause...')
