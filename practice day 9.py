#SET
"""
x = {1,2,3,4}
print(type(x))
"""
"""
x = set(input("enter the x value:"))
y = set(input("enter the y value:"))

#ADD
x.add(10)
print(x)
"""
"""
#UPDATE
x = {"prakash"}
y = {"dara"}
x.update(y)
print(x)#{'dara', 'prakash'}
"""
#INTERSECTION
"""
x = set(input("enter the x value:"))#456PRAKASH
y = set(input("enter the y value:"))#PRAKASH789
"""
"""
z = x.intersection(y)
print(z)#{'K', 'H', 'A', 'P', 'S', 'R'}
"""
#UNION
"""
z = x.union(y)
print(z)#{'9', 'H', '6', 'A', '4', '8', 'R', '5', 'P', 'S', '7', 'K'}
"""

x = {3,4,5,6}
y = {5,6,8,9}
"""
z = x.difference(y)
print(z)#{3,4}
"""
#POP
"""
for i in x:

    print(i)

x.pop()
print(x)#{4, 5, 6}

x.remove(5)
print(x)#{4, 6}

"""

x = []

for i in y:
    x.append(i*x)
    print(i)
    




































