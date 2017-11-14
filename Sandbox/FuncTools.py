import functools

def invoke(f, *args):
    return functools.partial(f).func(*args)

def abc(a,b,c):
    return a + b + c

def funcfind(name = "*"):
    if "*" in name:
        return globals().keys()
    else:
        if name in globals(): return globals()[name]
        
#print invoke(funcfind("abc"), 1, 2, 3)
print funcfind()
