import re

'''
text= 'We have 3 apples and 14 oranges in 1432 Avenue which is priced for $40.'
pattern='[a-zA-Z]+'
#pattern='[^ a-zA-Z\d\s]'
output=re.findall(pattern,text)
print(output)
'''

'''
text='hello world hello heeello'
pattern = r'h.llo'
output=re.findall(pattern,text)
print(output)'''


'''text='hello world falld heeello'
pattern = r'.ld'
output=re.findall(pattern,text)
print(output)'''

'''text='hello world falld heeello'
pattern = r'.*ld' #everything in between ld starting from the begining
output=re.findall(pattern,text)
print(output)'''

'''text='a aa aaa aaaa aaaaa aaaaaa'
pattern = r'a{3}'
output=re.findall(pattern,text)
print(output)'''

'''text='Daniel and marv are friends'
pattern= ('friends')
output= re.sub(pattern,'enemies',text)
print(output)'''

'''text='ADA and Jesse go to school'
print(text.split())'''
