#OOPS:OBJECT  ORIENTED PROGRAMMING SYSYTEM


#DISPLAY METHOD
"""class Prakash:
    def akhil(self,args):
        for i in args:
            yield i
    def syed(self):
        return "bitthhiri"
ss = Prakash()
print(list(ss.akhil("leo")))
print(ss.syed())"""
#CLASS METHOD

"""class Akhil:
    @classmethod
    def syed(cls,args):
        return args*args

    @classmethod
    def prakash(cls,args):
        return args.isupper()
    @classmethod
    def yaswanth(cls,weight,age):
        return f"the weight and age is {weight} {age}"
xx = Akhil()
print(xx.syed(25))
print(xx.prakash("PRAKASH"))
print(xx.yaswanth(40,21))"""


#STATIC METHOD

"""class Leo:
    @staticmethod
    def lokesh():
        return "LCU"
    
xx = Leo()
print(xx.lokesh())"""

#INITIALIZER

"""class Pspk:
    def __init__(self,title,title2):
        self.title = title
        self.title2 = title2
        print(f"the title is {self.title} {self.title2}")


xx = Pspk("ustad ","bhagat")

class Pawan:
    def __init__(self,title,title2):
        self.title = title
        self.title2 = title2
        print(f"the name is {self.title} {self.title2}")

    def function(self,arg):
        return self.title+self.title2+arg

xx = Pawan("bhagat","singh")
print(xx.function("singh"))"""

class Lcu:
    x = 50
    def function(self,arg):
        return Lcu.x+arg


    def __del__(self):
        print("object is no more")

ss = Lcu()
print(ss.function(50))
del ss
print(ss.function(40))




