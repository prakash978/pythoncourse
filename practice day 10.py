#FUNCTIONS
"""
def greetings():
    return "hi man"
    
x = greetings()
print(x)
"""
"""
def function(arg):
    return arg+arg
x = function("DHONI ")
print(x)#DHONI DHONI
"""

#EMPTY ARGUMENTS
"""
def my_name():
    return "Prakash"

x = my_name()
print(x)#Prakash

def tmrw_movie():
    return "LEO"

print(tmrw_movie())#LEO
"""
#POSITIONAL ARGUMENTS
"""
def function(x,y,z):
    if x%y==0 or z%x==0:
        return True
    else:
        return False

zz = function(10,3,30)
print(zz)
"""
#DEFAULT ARGUMENTS
"""
def lokesh(x=10,y=25,z=30):

    if x*y==0 and y*z!=0:
        return True
    else:
        return False
    
xx =lokesh(10,25,30)
print(xx)
"""
#KEYWORD ARGUMENT

def lokesh(x,y):
    return(x+y)
xx = lokesh(x="LEO IS",y = " LCU")
print(xx)#LEO IS LCU

def function(*arg):

    x = []
    for i in arg:
        x.append(i%i==0)

    return x

    
print(function(2,3,4,5))


   




    

   











































    


    
