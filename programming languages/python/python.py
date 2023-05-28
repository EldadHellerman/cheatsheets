# use 'shift+enter' in vscode to execute one line..

# built in help function
help(print)


##################################################
#################### objects  ####################
##################################################

# almost everything is an object.
# basic classes: noneType, int, float, bool, string, complex
print("class types:", type(None), type(5), type(5.4342), type(5==5), type("dsvsdv"), type(3+5j), sep=", ")

# ojbect id is unique for that object in it's liftime:
print("objects id", id(5), id(2+3), id(5.0), id(5+0j), sep='\n')
# int objects in the range [-5,256] are chached at startup, so they always have the same id
print("(255+1 is 255+1): (", (255+1) is (255+1),") always!, but (-10 is -9-1): (", (-10) is (-9-1), ") not guaranteed", sep="")
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




a,b = 3,4
#turns into
(a,b) = (3,4)

#methods are class functions that depened on the object:
print("hello".upper()) #print is a function, upper is a method

def func1():
    pass
def func2():
    pass

if __name__=="__main__":
    pass #pass can be used to fill in empty spaces where an indentatino is needed