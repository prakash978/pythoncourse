
#INHERITANCE

"""class Khaidi:
    def lcu(self,args):
        for i in args:
            yield i

class Vikram(Khaidi):
    def lcu2(self,args):
        return len(args)
xx = Vikram()
print(list(xx.lcu("prakash")))
print(xx.lcu2("1234567"))"""

"""class Grandfather:
    def tablet(self,x="ast",y="hama"):
        return x+y
class Father(Grandfather):

    def gastric(self,x,y):
        return x+y

class Son(Father):
    def fine(self,x):
        return "the fine is",x

xx = Son()
print(xx.tablet("ast","hama"))
print(xx.fine(1005))
print(xx.gastric("panta","prazole"))
"""
"""class Khaidhi:
    def function(self,x,y):
        if x>y and y<x:
            return True
class Vikram:
    def function2(self,x,y):
        if x%y==0:
            return "even number"
        else:
            return "odd number"


class Lcu(Khaidhi,Vikram):
    def function3(self):
        return "all are inter link"

xx = Lcu()
print(xx.function(20,10))
print(xx.function2(3,2))
print(xx.function3())"""

#POLYMORPHISM
#METHOD OVERRIDING
"""class Panipuri:
    def chats(self,):
        print("rajasthan")

    def chats(self,):
        print("andhra")

xx = Panipuri()
xx.chats()"""

"""class Addition:
    def ex1(self,x=5,y=10):
        return x+y
class Multi(Addition):
    def ex2(self,x=10,y=10):
        return x*y
class Division(Multi):
    def ex3(self,x=10,y=2):
        print(Multi.ex2(self))
        print(Addition.ex1(self))
        return x%y

ss = Division()
print(ss.ex3())

"""



