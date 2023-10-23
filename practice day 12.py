
"""
def inner_function():
    def outer_function():
        return "outer"
    
    x = outer_function()
    return x


x = inner_function()
print(x)
"""
"""
def even(func):
    def inner(x,y):
        if x%2==0 and y%2==0:
            xx = func(x,y)
            return xx
        return "x or y is not even numkber"
                   
    return inner
     
@even
def even_numbers(x,y):
    return x*y


print(even_numbers(10,2))
"""
"""
def nat(funct):
    def inner():
        if 

"""

def nat(func):
    def inner(x,y):
        if x.isupper() and y.isupper():
            xx = func(x,y)
            return xx
        return "x or y is not upper case letters"
    return inner
            
          
      


@nat
def function(x,y):
    return x+y
     
    
   
    

zz = function("MAHENDRa ","DHONI")
print(zz)
 
    





    
    































