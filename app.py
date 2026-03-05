import sys
def add(a,b):
    return a+b
if _name_=="main":
    m=int(sys.argv[1])
    n=int(sys.argv[2])
    result=add(m,n)
    print(f"{result}")
