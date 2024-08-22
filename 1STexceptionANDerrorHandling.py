'''
num = 0
print(12/num) #ZERO DIVISION ERROR
'''
'''
try:
    num=0
    print(12/num)
except ZeroDivisionError as z:
    print("Error: ",z)
'''


'''
num= input()
calc=num / 7
print(calc) #TYPE ERROR. UNMATCHING TYPE: The num is a string and calc is intergar. always specify
'''
'''
try:
    num=input()
    calc= num/723
    print(calc)
except TypeError as t:
    print("Error: ", t)
'''


'''
lisst=[1,2,3,4]
print(lisst[5])  #INDEX ERROR when the list put in is out of range
'''
'''
try:
    lisst=[1,2,3,4]
    print(lisst[3])
except IndexError as i:
    print("Error: ", i)
else:
    print('The code runs suceesfully')
'''



'''
print(y) # NAME ERROR because the y is not defined 
'''
'''
try:
    print(y)
except NameError as e:
    print("Error:", e)
'''


'''
try:
    num1=5
    num2= int(input())
    calc= num1 / num2
    print(calc)
except ZeroDivisionError:
    print("This is a Zero Division Error")
except ValueError as v:
    print("Value Error pythonic statement", v) # whether v is added or not no difference
else:
    print("No error thrown")
finally:
    print('Proceed to the next line of code')
'''

'''try:
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
     print(num2)
    else: 
        print("Sorry")
except ValueError:
    print("Value Error noticed")
except IndentationError as i:
    print("Indentation error occuring", i)
except:
    print("An error is being thrown")
else:
    print("No errors found")
'''
'''
age=int(input("Enter your age: "))
if age >= 0:
    raise Exception("Invalid Age") #RAISE ERROR
'''


age=int(input("Enter your age: "))
assert age>= 18, "Age must be 18 or older"
print("You are eligible")