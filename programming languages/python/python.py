# use 'shift+enter' in vscode to execute one line

def numbers():
    "numbers"
    print(4*3, 4**3, pow(4,3), sep=", ") # multiply, power
    print(8.5//2, 8.5%2, divmod(8.5, 2), sep=", ") # divide whole, mod (remainder), and both in a tuple
    print(round(2232.343452, 1), round(2232.343452, -3), abs(-5.4))
    
    #complex numbers:
    c = complex(1,2)
    print("complex number", c, c.real, c.imag, pow(c,2), c**2, abs(c), c.conjugate())
    #different number bases:
    print("numbers:", 123e-4, 0x03A, 0b10 + 0x1a*1j, complex(0b10, 0x1a), 0b01001, 0o42)
    #converting between them:
    print("converting bases:", hex(255), bin(0b111), oct(64), int("16", base=22), int("0x16",base=0))

    #math module
    import math
    print(math.sqrt(16.4), math.ceil(5/4), math.cos(math.pi), math.factorial(5))

def strings():
    "strings"
    str_1 = "A"
    str_2 = "B"
    print((str_1 + str_2)*3) # adding and multiplying strings
    print(str_1*3 == "aaa".upper(), str_1 == str_2, str_1 < str_2, "a" < str_2)
    print(ord("a"), chr(65))
    #formatting

def logic():
    "logic"
    print(4&6, 4|6, 4^6, 0b01000, ~(0b1000), sep=", ") #bitwise and, or xor, not

    if:
        pass
    elif:
        pass
    #loops
    #case

    #sum runs on iterables supporting cating to int
    sum(range(10))
    print([sum(l) for l in [[], [False, False], [False,True], [True, True], [1,2,3], [1,0,3.5]]])
    #all runs on iterables supporting casting to bool
    print([all(l) for l in [[], [False, False], [False,True], [True, True], [1,2,3], [1,0,3.5], [""], ["a",""], ["a","b"]]])
    print([any(l) for l in [[], [False, False], [False,True], [True, True], [1,2,3], [1,0,3.5], [""], ["a",""], ["a","b"]]])
    any(["dc"])
    #iterables or more than two arguments, supporting comparison
    max(3,4,7,6)
    min(["abc", "b", "abfs"])

def lists():
    "lists and alike"
    a,b = 3,4
    #turns into
    (a,b) = (3,4)

def objects():
    "objects"
    # almost everything is an object.
    # basic classes: noneType, int, float, bool, string, complex
    print("class types:", type(None), type(5), type(5.4342), type(5==5), type("dsvsdv"), type(3+5j), sep=", ")
    
    # ojbect id is unique for that object in it's liftime:
    print("objects id", id(5), id(2+3), id(5.0), id(5+0j), sep='\n')
    
    # int objects in the range [-5,256] are chached at startup, so they always have the same id
    a = 29; b = 30
    c = -10; d = -9
    a += 1; d -= 1
    print("(30 is 29+1): (", a is b, ") always!, but (-10 is -9-1): (", c is d, ") not guaranteed", sep="")
    
    # equal strings are not promised to have the same id. this is call string interning.
    print("string interning, objects id dont have to be the same:", id("hello!"), id("hel"+"lo"+"!"))
    
    # 'is' can be used to check if to objects are the same (meaning they also have the same id):
    a = 5; b = a; c = 7
    print("checking with 'is': ", a is b, b is c)
    # None doesn't implement __eq__ so to speak and therefor must be checked with is,
    a = None
    print("checking if none:", a is None, "" is None, b is not None, not b is None)
    # for other built in singelton classes, 'is' and 'is not' are probably faster and better
    print("'is' vs '==': ",(5==5) is True, b is True, b == True, bool(b is True), bool(b))
    
    #deleting a reference for an object:
    a = 5; b = 4;
    print(a, b) #error - a and b are not defiend
    del(a) #del() is a bit quicker than assigning to None
    b = None
    print(a, b) #a is not defined whie b is None.
    # when an objects references count reaches 0 the memory is (immeaditly) claimed.
    # pythons garbage collection is mainly used for cyclic references.

def exceptions():
    #exception objects
    #try
    pass

def oop():
    "object oriented programming"
    class myclass:
        def func1():
            pass

    #methods are class functions that depened on the object:
    print("hello".upper()) #print is a function, upper is a method

def libraries():
    "libraries and modules"
    #generally, a module is a .py file containing classes, functions, and code,
    #while a library is a collection of modules
    #some built in python modules are:
    #math, datetime, random, os, sys.
    
    #how to import

def general():
    "general things"
    help(print) # built in help function
    dir(__builtins__) #all built in functions
    help(__builtins__)
    #print:
    print("controlling", "seperation","as well as", sep="-", end="|r|n")
    print("end of line")
    # a
    #open and close files:

if __name__ == "__main__": #runs only is this file is the one that's running (and not included from somewhere else)
    pass #pass can be used to fill in empty spaces where an indentation is needed.