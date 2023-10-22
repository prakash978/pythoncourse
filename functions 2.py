def function():
    return "PRAKASH"

x = function()
print(x)

print(x.count("P"))#1
print(x.count("R"))#1
print(x.count("A"))#2
print(x.count("K"))#1
print(x.count("S"))#1
print(x.count("H"))#1

def function(**kwargs):
    return(kwargs)


xx = function(P=1,R=1,A=2,K=1,S=1,H=1)
print(xx)#{'P': 1, 'R': 1, 'A': 2, 'K': 1, 'S': 1, 'H': 1}




