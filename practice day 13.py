#EXCEPTIONAL HANDLING
"""
try:
    def function(x,y):
        return x+y
    xx = function(10)
    print(xx)
except:
    print("error is found")#error is found
"""
""""
try:
    def function(x,y):
        return x+y
    xx = function(20)
    print(xx)
except Exception as error:
    print("error is:",error)#function() missing 1 required positional argument: 'y'
"""
"""
try:
    def function(x,y):
        return x*y
    xx = function(10)
    print(xx)

except TypeError:
    print("type error")

except Exception as error:
    print("error is:",error)
"""
"""
try:
    def function(**args):
        return sum(args)
    xx = function("praksh")
    print(xx)
except Exception as error:
    print("error is:",error)
finally:
    print("final")
"""
"""
try:
    def function(*args):
        return sum(args)
    xx = function(1,2,3,4,5)
    print(xx)
except Exception as error:
    print("error is:",error)
else:
    print("error is not found")

finally:
    print("final")
"""
x = "give"
y = "money"
print(x+y)
raise Exception("cant give money")

