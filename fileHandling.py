'''y= open("food.txt", "a")
y.write("hey")
y.close()


y = open("food.txt", "r")
print(y.read())

v = open("food.txt", "w")
v.write("Ilovefood")
print(v.read())

z = open("demo.py", "r")
print(z.read(10))
print(z.readline())
z.close()

v= open("food.txt", "r")
print(v.read())

a = open("food.txt", "x")
'''
#FUNCTION PARAMETERS

'''def name(fname):
    myname = input("What's yourname? ")
    print(f"My name is {myname}")

 name(fname="faith")'''


'''def name(fname):
    print(f"My name is {fname}")

name("faith")
'''

'''def name(fname, lname):
    print(f'my name is {fname} {lname}')
name("Zita", "Ali")
'''

'''def children(*kids):
    print(" the youngest kis is "+ kids[3])

children("ada", "aka", "chi", "ali")
'''


'''def children(kid1, kid2, kid3, kid4):
    print(f'the eldest child is  {kid1} ')

children(kid3 ="ali", kid1="ada", kid2="aka", kid4="tito")
'''


'''def country(state = "Oyo"):
    print(f"I am from {state}")

country("Abia")
country("Anambra")
country()
country("Imo")
'''

def my_function(x):
    return 10 * x

print(my_function(4))
print(my_function(2))
print(my_function(5))