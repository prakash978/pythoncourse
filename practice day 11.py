#LAMBDA
"""
LCU = lambda x,y:x+y
print(LCU("LEO","VIKRAM"))#LEOVIKRAM

x = lambda x,y:x+y
print(x(100,200))#300


y = lambda x,y:x*y
print(y(2,5))#10

z = lambda *args:sum(args)

print(z(20,50))#70

h = lambda *args:len(args)
print(h(2,3,4,5,6,6,7,8))#8
"""

#GENERATOR
"""
def function(*args):
    for i in args:
        return i+i

xx = function("pop","top","kop")
print(xx)#poppop


def function(*args):
    for i in args:
        yield i+i

xx = function("pop","top","kop")
print(list(xx))#['poppop', 'toptop', 'kopkop']
"""

#ITERATION
"""
x = list("PRAKASH")
xx = iter(x)

print(next(xx))#P
print(next(xx))#R
print(next(xx))#A
print(next(xx))#K
print(next(xx))#A
print(next(xx))#S
print(next(xx))#H
"""

#INNER FUNCTION OR OUTER FUNCTION

def inner_function():
    def outer_function():
            return "shirt"
    x = outer_function()

    return x

x = inner_function()
print(x)#shirt


def bat():
    def ball():
        return "kokaborra"
    def gloves():
        return "sg"

    y = gloves()

    return y

y = bat()
print(y)#sg




    



























