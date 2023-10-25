#FILE HANDLING
"""
with open("test.file",'r') as xx:
    #zz = xx.read()
    #print(zz)
    # yy = xx.readlines()
    # print(yy)
    aa = xx.readline()
    print(aa)
"""
#READ
"""def read_file(file_name):
    try:
        with open(file_name,'r') as xx:
            zz = xx.read()
            return zz
    except:
        print("found error")
d = read_file("test.file")
print(d)"""

"""def write_file(file_name):
    try:
        with open(file_name,'w') as pp:
            xx = pp.write("maxell")
            return xx
    except:
        print("error is found")

d = write_file("test.file")
print(d)"""


def write_file(file_name):
    try:
        with open(file_name,'a') as pp:
            xx = pp.write("smith")
            return xx
    except:
        print("error is found")

d = write_file("test.file")
print(d)



