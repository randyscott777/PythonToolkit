import sys
sys.path.append("c:/users/syrra/onedrive/visualstudio2022/Python_Toolkit") 

from Python_Toolkit import NOW,InputType,MyList,Day,Color,Subset,TupleOps,UnaryOps,Temperature
from Python_Toolkit import Arithematic,Add,Mult,Class_Decorator,Add_Timestamp 
import Python_Toolkit as tools

tools.Help()

print('\nThe PATH is',tools.PATH)
print('NOW is',NOW)
print('The VERSION of python is',tools.VERSION)
print('The URLS are',tools.URLS)

s = tools.MyStr('ABCDEF') # in tools 
print('\nSubstr of "ABCDEF: at pos 2 with XY is',s.Substr(2,'XY'))

print('\nEnum Day where Sunday=1,Monday=2...')
print('Day.SUNDAY.name is',Day.SUNDAY.name) 
print('Day.MONDAY.value is',Day.MONDAY.value) 
print('Day(3) is',Day(3))

print('\nEnum Color where RED=1,GREEN=2,and BLUE=4')
print('Color.RED.name is',Color.RED.name) 
print('Day.GREEN.value is',Color.GREEN.value) 
purple = Color.RED | Color.BLUE
yellow = Color.RED | Color.GREEN
cyan = Color.GREEN | Color.BLUE
white = Color.RED | Color.GREEN | Color.BLUE   
print('Purple is',purple)
print('White is',white)
print('Red is in purple is',Color.RED in purple)

print('\nThe 9th element of Fibonacci series is ')
tools.Fibonacci(9) # has imbedded print

print('\nPrime numbers up to 89 are ',tools.Primes(3,91))

print('\nFactorial of 4 is',tools.Factorial(4))

input('Pause...')

s1 = 'olleh'
s2 = 'world hello'
print('\nAre all chars=olleh in hello world',tools.AllChars(s1,s2))

n1 = (2,4,6,8,10)
n2 = [1,0,-1,-1,-2]
print('\n2,4,6,7,10 has ALL values > 1,0,-1,-1,-2 is',tools.AllGT(n1,n2))

s1 = Subset(list('olleh'))
s2 = list('world hello')
print('\nIs olleh is a subset contained in hello world',s1//s2)

lst = MyList('abcdefghi')
print('\nFor abcdefghi, RemoveAt(3) is',lst.RemoveAt(3))

lst = MyList('abcdefghi')
print('For abcdefghi, InsertAt(3) is',lst.InsertAt(3,'X'))

obj1 = TupleOps(2,3)
obj2 = TupleOps(3,4)
obj3 = TupleOps(4,5)
obj4 = obj1 + obj2 + obj3
print('\nMagic method to add tuples 2,3; 3,4; and 4,5 is',obj4.numbers)

obj1 = TupleOps(1,2,3)
obj2 = TupleOps(4,5,6)
obj4 = obj1 + obj2 
print('Magic method to add tuples 1,2,3 and 4,5,6 is',obj4.numbers)

obj1 = TupleOps(1,2,3,4)
obj2 = TupleOps(1,1,2,2)
obj4 = obj1 + obj2 
print('Magic method to add tuples 1,2,3,4 and 1,1,2,2 is',obj4.numbers)

obj5 = UnaryOps(7)
print('Magic unary method for inverse of 7 is',~obj5)

temp = Temperature(32) # fahen 
print('\nThe temperature of 32 fahrenhit in celius is',temp.cel)
temp.cel = 0 # celius 
print('The temperature of 0 celius in fahrenheit is',temp.fah)

print('\nFunction Decorator for Mult',Arithematic(Mult,2,3))
print('Function Decorator for Add',Arithematic(Add,2,3))

class_dec = Class_Decorator()
class_dec(4,5,x=2,y=3) # has imbedded print stmts

print("\nThe @ symbol is syntactic sugar denoting to apply a decorator to it's following function")
@Add_Timestamp
def DisplayTimestamp(info):
    print(f'{info}') # ie. begin or end
DisplayTimestamp('Begin')
'''
print()
opt = InputType('Enter a integer number','int')
print('The integer number entered was',opt,'and has type of',type(opt))

opt = InputType('Enter a floating point number','float')
print('The floating number entered was',opt,'and has type of',type(opt))

opt = InputType('Enter a date in mm/dd/yyyy format','date')
print('The date entered was',opt,'and has type of',type(opt))

opt = InputType('Enter a list separated by commas','list')
print('The list entered was',opt,'and has type of',type(opt))

opt = InputType('Enter dictionary item(s)','dict')
print('The dict entered was',opt,'and has type of',type(opt))
'''
listofLists = [['Randy','Black Brant','Lpool','NY',13090],['Donna','Black Brant','Lpool','NY',13090],['Randy','Bolvevard St','N Syracuse','NY',13210] ]
for name,str,city,state,zip in listofLists:
    print(name,str,city,state,zip)
    
# Testing from snippets

print("\nCheck if ALL chars in 'hellx' is contained in 'World, hello!'")
str1 = "hellx"
str2 = "World, hello!"
#bools = [ch1 in str2 for ch1 in str1]
#bools = list(map(lambda ch1: ch1 in str2, str1))
#good = all(bools)
if all(ch1 in str2 for ch1 in str1): 
    print("All chars in substring are contained in the main string")
else: print('Not all chars in substring are in the main string')


print("Check if ANY char '12x34' is bad (not in '$0123456789.,')")
number = "12x34"
valids = "$0123456789.,"
if any(ch not in valids for ch in number): print("The number contains bad chars")
else: print('All chars are valid')
    
