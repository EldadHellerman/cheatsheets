# python 3.10.7
# use 'shift+enter' in vscode to execute one line

def numbers():
    "numbers"
    print("seperating long numbers:", 0b0111_1001_1100,1.234_567)
    print("multiply and power:", 4*3, 4**3, pow(4,3), sep=", ")
    print("integers divison, mod, both:", 8.5//2, 8.5%2, divmod(8.5, 2), sep=", ")
    print(round(2232.343452, 1), round(2232.343452, -3), abs(-5.4))
    print((3/64), (3/64).as_integer_ratio())
    c = complex(1,2)
    print("complex number:", c, c.real, c.imag, pow(c,2), c**2, abs(c), c.conjugate())
    print("different bases:", 123e-4, 0x03A, 0b10 + 0x1a*1j, complex(0b10, 0x1a), 0b01001, 0o42)
    print("converting between bases:", hex(255), bin(0b111), oct(64), int("16", base=22), int("0x16",base=0))

    
    import math #math module
    print(math.sqrt(16.4), math.ceil(5/4), math.cos(math.pi), math.factorial(5))

def strings():
    "strings"
    str_1 = "A"
    str_2 = "B"
    print('strings with different',"quote styles",'''as
    well''',"""as""", "contcatenation by"
    '-spanning multiple' #can easily comment part of string
    """-lines""")
    print("bytes instead of str:", b"1\n23 hex: \x41 octal: \101 \141", type(b"1234"))
    print("raw strings:", "1\t\t2", r"3\t4", br"5\t6")
    print("🔥 unicode 8-bit: \x41 16-bit: \u05D0\u05D1\u05D2  and 32-bit: \U0001F600")
    
    print("adding and multiplying:", (str_1 + str_2)*3)
    print("comparing:", str_1*3 == "aaa".upper(), str_1 == str_2, str_1 < str_2, "a" < str_2)
    print("unicode/ascii:", ord("a"), chr(65))
    print("converting to string, str() is ment to be user firendly", str({'a': 5, 6: 'c'}), str(range(3)), str("Hi\nthere"))
    print("repr is meant to be eval(repr(a))==a, ascii() is similar but excaping non ascii:", repr("Hi\nthere"), ascii("Hi\nthere"))
    

    print("legacy - formatting strings the %s way, not recom%dnded" % ("very old", 3))
    print("legacy - formating strings - the {1} withmore control ~{0}~".format(5.65/32, "sort of old way"))
    print("legacy - formating strings - referenced by name {first} with {sec\ond}".format(first="f", second="s"))
    print('format specifier: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]')
    print(f"printing expression text with it's value '{3  *6= :d}' (preserves whitespaces)")
    print(f"strings: string {str_1} {str_1*3:s}, escaping {{curly braces}}")
    print(f"integers: decimal {12} {12:d}, hex {256:x} {256:#x}, bin {36:#b}, char {65=:c}")
    print(f"floats: float {1.234:.1f}, scientific {314159:.4E}, general {314159:.4g}, percent (like 100*f){0.4321:.2%}")
    print(f"sign: ('{+12:+2d}', '{-12:+2d}'), ('{+12: 2d}', '{-12: 2d}'), ('{+12:-2d}', '{-12:-2d}')")
    print(f"thousands seperator: '{-1234:+6,d}', '{1234:14_d}'")
    print(f"padding and alignment: '{12}' '{12:4}', '{12:!>4}', '{12:@^4}', '{12:#<4}', '{12:_^+5}', '{12:_=+5}'")
    char, precision = "🔥", 3
    print(f"nested format specifiers '{3*5.25313:{char}^15.{precision}f}'.")
    print(f"converting to str (default) {range(3)!s}, repr {range(3)!r}, ascii {range(3)!a}")
    import datetime
    now = datetime.datetime(2023, 5, 30)
    print(f"formatting date. now is {now:%d.%m.%Y}")
    
    
    #slicing is part of list
    #reverse, join
    d = {'a':3, 'b':5}

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
    min(["abc", "B", "abfs"], key=str.upper) # because ABC < B
    min([[1,2,8], [3,4,9], [4,5,6]], key=max) # list with smallest maximum

def lists():
    "lists and alike"
    a,b = 3,4
    #turns into
    #unpacking lists *
    #unpacking dictionaried * and ** 
    (a,b) = (3,4)

def function():
    "docstring of a function"
    #function parameters - names, defaults
    #parameters with * and ** and names.
    #lambda functions


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

def input_output():
    # ANSI escape code.
    color_foreground = {'BLACK': '\x1B[30m', 'RED': '\x1B[31m', 'GREEN': '\x1B[32m', 'YELLOW': '\x1B[33m', 'BLUE': '\x1B[34m', 'MAGENTA': '\x1B[35m', 'CYAN': '\x1B[36m', 'WHITE': '\x1B[37m', 'RESET': '\x1B[39m'}
    color_foreground_bright = {'BLACK': '\x1B[90m', 'RED': '\x1B[91m', 'GREEN': '\x1B[92m', 'YELLOW': '\x1B[93m', 'BLUE': '\x1B[94m', 'MAGENTA': '\x1B[95m', 'CYAN': '\x1B[96m', 'WHITE': '\x1B[97m'}
    color_background = {'BLACK': '\x1B[40m', 'RED': '\x1B[41m', 'GREEN': '\x1B[42m', 'YELLOW': '\x1B[43m', 'BLUE': '\x1B[44m', 'MAGENTA': '\x1B[45m', 'CYAN': '\x1B[46m', 'WHITE': '\x1B[47m', 'RESET': '\x1B[49m'}
    color_background_bright = {'BLACK': '\x1B[100m', 'RED': '\x1B[101m', 'GREEN': '\x1B[102m', 'YELLOW': '\x1B[103m', 'BLUE': '\x1B[104m', 'MAGENTA': '\x1B[105m', 'CYAN': '\x1B[106m', 'WHITE': '\x1B[107m'}
    style = {'BOLD': '\x1B[1m', 'ITALIC': '\x1B[3m', 'UNDERLINE': '\x1B[4m', 'REVERSE': '\x1B[7m', 'HIDDEN': '\x1B[8m', 'STRIKETHROUGH': '\x1B[9m', 'RESET_ALL': '\x1B[0m',
             'NBOLD': '\x22B[21m', 'NITALIC': '\x1B[23m', 'NUNDERLINE': '\x1B[24m', 'NREVERSE': '\x1B[27m', 'NHIDDEN': '\x1B[28m', 'NSTRIKETHROUGH': '\x1B[29m'}
    RESET_ALL = '\x1B[0m'
    print(color_foreground['RED'] + "ANSI escape " +  color_background['YELLOW'] + "codes and styles: " + style['ITALIC'] + " italic " + style['BOLD'] + " BOLD ")
    print("remains until " + style["UNDERLINE"] + " reset " + style["NUNDERLINE"] + style["STRIKETHROUGH"] + "is performed" + RESET_ALL)
    rgb = lambda c1, c2, c3: str(c1)+";" + str(c2) + ";" + str(c3)
    print("custom rgb " + '\x1B[38;2;'+rgb(70, 20, 90)+'m' "foreground and background: ")
    for g in range(255): print('\x1B[48;2;'+rgb(0, g, 0)+'m' + "B", end='')
    print(RESET_ALL)

    #files
    #open and close files:
    # with a as f1, b as f2:
    # with (a as f1
    #       b as f2):

    #object serialization
    # using json files.
    pass


def general():
    "general things"
    help(print) # built in help function
    dir(__builtins__) #all built in functions
    help(__builtins__)
    print("nackslash ignoring a\
           new line")
    #print:
    print("controlling", "seperation","as well as", sep="-", end="|r|n")
    print("end of line")
    # a


if __name__ == "__main__": #it's __main__ only if this file is the one that's running (and not included from somewhere else)
    pass #pass can be used to fill in empty spaces where an indentation is needed.

