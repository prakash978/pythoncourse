#DATA STRUCTURES===>LIST

#LIST

#APPEND
"""
x = ["D","H","O","N"]

x.append("I")
print(x)#['D', 'H', 'O', 'N', 'I']

x = [23,34,45,56]
x.append(65)
print(x)#[23, 34, 45, 56, 65]
"""
#EXTEND
"""
x = ["DHONI IS THE BEST"]
y = ["FINISHER"]
x.extend(y)
print(x)#['DHONI IS THE BEST', 'FINISHER']
"""
"""
x = ["VIRAT"]

x.extend("18")
print(x)#['VIRAT', '1', '8']
"""
"""
x = [2,3,4]
x.extend(x*2)
print(x)#[2, 3, 4, 2, 3, 4, 2, 3, 4]
"""

#SORT
"""
x = [6,4,5,8,3,1,9]

x.sort()
print(x)[1, 3, 4, 5, 6, 8, 9]
"""
"""
x = [0*2,2*4,8*0,2*2]

x.sort()
print(x)#[0, 0, 4, 8]
"""
"""
x = [3/2,5/2,7/2,9/2]

x.sort()
print(x)#[1.5, 2.5, 3.5, 4.5]
"""
"""
#COUNT

x = [0,4,5,65,4,5,6,3]
print(x.count(4))#2
"""
#INDEX,INSERT,INDEX
"""
x = [4,4,6,7,8,3,]

print(x[3])#7

y = [1,8]
y.insert(1,0)
print(y)#[1, 0, 8]

print(x.index(4))#0
"""
#CLEAR,POP,REMOVE,DEL

x = ["A","K","H","I","L"]
x.pop()
print(x)#['A', 'K', 'H', 'I']

x.remove('K')
print(x)#['A', 'H', 'I']

x.clear()
print()#NOTHING

del x
print(x)#x KHATHAM HOGAYA

























