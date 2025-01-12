# This is a module of useful things to be imported
'''
Documentation for Python_Toolkit

DEFINE:
    sys.path.append("c:/users/syrra/onedrive/visualstudio2022/Python_Toolkit") 
    from Python_Toolkit import MyStr
    import Python_Toolkit as tools

VARIABLES:
    PATH = pathlib.Path().resolve()
    VERSION of Python (sys.version)
    NOW = now.strftime('%m/%d/%Y')
    URLS = myjournal, misc, pythonanywhere, rs777.github

FUNCTIONS:   
    InputType - Validates the input accordinf uo type specified]
    AllChars - return True if all chars in 1 string are in another string
    AllGT - return True if all values in 1 string are GT corr value in another string
    Fibonacci up the element index number specified
    Primes up to a number specified
    Factorial of n = n * n-1 * ...      
    
ENUMs:
    Day.MONDAY is MONDAY, Day.MONDAY.value is 1, Day(3) is WEDNESDAY
    Color with flags
    
CLASSES:
    Substr, ie.s = MyStr('ABCDEF'), then s.Substr(2,'X') is 'ABXYEF'
    RemoveAt(index), ie.lst = MyList('ABCDEF'), then lst.EwmoveAt(3) is 'ABCEF'
    Subset using // (__floordiv__) operator, but defined to check for subset
      
OPERATORS and MAGIC/DUNDER METHODS (binary,unary,comparison,extended):
    __init__(self) is not required to instantiate with no arguments
    __floordiv(self,other) //
    binary operators +,-,*,/,//,&,^,|
    unary operators -,+,abs,~,cmp,int,long,float,oct,hex
    comparison operators >,<,==,<=,>=,!=
    extended assignment +=,-=,*=,/=,//=,%=,**=,<<=,>>=,&=,^=,|=
    descriptors: __get__(self,instance,owner),__set__(self,instance,value),__del__()
    | operator (pipe) - TODO
    >> operator (?) - TODO
    ^ operator (?) - TODO
    
DECORATORS: 
    Function Decorator: Add timestamp to info 
    Class Decorator: print the args and kwargs passed   
'''
import Snippets
snippets = Snippets.__doc__

import DDLMenu
ddlMenu = DDLMenu.__doc__

def Help():
    ''' Display main documentation and optionally some others'''
    while True:
        print('\n1. Main tools' ) 
        print('2. Snippets' ) 
        print('3. Python Libraries' ) 
        print('4. Dunder methods' ) 
        print('5. OOP Concepts' ) 
        print('6. DDL Menu - TBD' ) 
        print('9. Exit' ) 
        opt = int(input('Which option 4 (dft) ') or 4)
        if opt == 1: 
            print(__doc__)
            input('Pause...')
            break
        if opt == 2: 
            with open("Snippets.py") as f:
                code = f.read()
            exec(code,{'str2':'make it global'}) # was getting not defined in list compr  
        if opt == 3:  
            with open("Libraries.py") as f:
                code = f.read()
            exec(code)
        if opt == 4:  
            with open("Dunder_Module.py") as f:
                code = f.read()
            exec(code)
        if opt == 5:  
            with open("OOP_Programming.py") as f:
                code = f.read()
            exec(code)
        if opt == 6: print(ddlMenu) 
        if opt == 9: exit()
   
from datetime import datetime as dt
import pathlib
from enum import Enum, Flag, auto
import sys

PATH = pathlib.Path().resolve()
NOW = dt.now().strftime('%m/%d/%Y')
VERSION = sys.version
URLS = ['myjournal','misc','pythonanywhere','rs777.github']

class MyStr(str):
    def Substr(self,pos,newValue):
        newString = list(self)
        for i in range(len(self)):
            newString[i] = self[i]
        for x in range(len(newValue)):
                newString[pos+x] = newValue[x]
        return ''.join(newString)
    
class MyList(list):
    def RemoveAt(self,at):
        lst = list(self)
        del lst[at:at+1]
        return lst
    def InsertAt(self,at,chr):
        lst = list(self)
        lst.insert(at,chr)
        return ''.join(lst)

class Day(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7


class Color(Flag):
    RED = auto()   # 1
    GREEN = auto() # 2
    BLUE = auto()  # 4

def InputType(msg,typ):
    '''Returns a valid int,float,date,list, or dict'''
    while True:
        inpt = input(msg + ' ')
        if typ == 'int':
            if not AllChars(inpt,'0123456789'): print('Not all chars are numeric'); continue
            return int(inpt)
        if typ == 'float':
            if not AllChars(inpt,'0123456789.'): print('Not all chars are numeric or decimal point'); continue
            return float(inpt)       
        if typ == 'date':
            try:
                valid_date = dt.strptime(inpt,'%m/%d/%Y').date()
                return valid_date
            except ValueError:
                print('Date is not valid or wrong format'); continue
        if typ == 'list':
            if ',' not in inpt: print('No commas to denote separate items'); continue
            return list(inpt.split(','))  
        if typ == 'dict':
            try:
                pairs = [item.strip() for item in inpt.split(',')]
                result_dict = {}
                for pair in pairs:
                    key, value = [x.strip() for x in pair.split(':', 1)]
                    result_dict[key] = value
                return result_dict
            except Exception as e:
                print(f"Error parsing dict input: {e}")
                continue
            
def Fibonacci(n):
    a = 0
    b = 1
    print('1',end=',')
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print(c,end=',')
        return b
    
def Primes(starting_range, ending_range):
    lst = []
    flag = 0  # Declaring flag variable
    # elements range between starting and ending range
    for i in range(starting_range, ending_range):
        for j in range(2, i):
            if(i % j == 0):  # checking if number is divisible or not
                flag = 1  # if number is divisible, then flag variable will become 1
                break
            else:
                flag = 0
        if(flag == 0):  # if flag variable is 0, then element will append in list
            lst.append(i)
    return lst

def Factorial(n):
    if n == 1: return 1
    return n * Factorial(n-1)


def AllChars(str1, str2):
    '''Returns true if all chars in substring in string'''
    for char in str1:
        if char not in str2:
            return False
    return True

def AllGT(iter1, iter2):
    '''Returns true of all numbers of list are GT corr item other list'''
    results = [a > b for a,b in zip(iter1,iter2)]
    return all(results)

class Subset: 
    def __init__(self,values): # self is the subset
        self.values = values
    
    def __floordiv__(self,superset):
        for char in self.values:
            if char not in superset:
                return False
        return True 
    
class TupleOps:  
    def __init__(self,*arguments): # cause tuple could be (1,2), or (1,2,3), or etc
        self.numbers = arguments
    
    def __add__(self,other): 
        sum = tuple(x + y for x,y in zip(self.numbers,other.numbers))    
        return TupleOps(*sum)
    
class UnaryOps:
    def __init__(self,number):
        self.number = number
    
    def __invert__(self):
        self.number = self.number * -1
        return self.number

class Celius:  # using descriptors
    def __get__(self,instance,owner):
        return 5 * (instance.fah - 32) / 9
    
    def __set__(self,instance,value):
        instance.fah = 32 + 9 * value / 5
    
class Temperature: # using descriptors
    cel = Celius()
    def __init__(self,fah):
        self.fah = fah

def Arithematic(func,a,b):
    strFunc = str(func(a,b))
    descFunc = f'The math of {a} and {b} is '+ strFunc
    return descFunc
def Add(a,b):
    return a + b    
def Mult(a,b):
    return a * b

class Class_Decorator:
    def __init__(self):
        print('\nAn instance of class decorator was initialized')
    def __call__(self,*args,**kwargs):
        print('The arguments are',args,kwargs)

import time
import functools
def Add_Timestamp(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f'Timestamp: {timestamp}',end=' ')
        return func(*args, **kwargs)
    return wrapper



    