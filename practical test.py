# write a program to check weather a string is a palindrome or not
'''
a=int(input('Enter str1'))
b=a[::-1]
if a==b:
    print('Palindrome')
else:
    print('Not palindrome')  '''

# program to print the table of a number
'''
a=int(input('Enter number'))
for i in range(1,11):
    print('{}*{}={}'.format(a,i,a*i))   '''

# to count the number of vowels in a string
'''
a=str(input('Enter a str: '))
count=0
for x in a:
    if x in ['a','e','i','o','u','A','E','I','O','U']:
        count=count+1

print('Numbers of vowals are',count)  '''

#write a function that return True if length of string is even other return False
'''
def length(a):
    if len(a)%2==0:
        return True
    else:
        return False
    
a=input('Enter a str')
print(length(a))   '''

#write a program to remove a character from a string based on index
'''
s=input('Enter a str: ')
n=int(input('Enter a num: '))
if n<len(s) and n>=-len(s):
    str2=(s[:n]+s[n+1:])
    print(str2)
else:
    print('Index is not valid')   '''

# write a  program to input a seqence of seperated string and convert it into list. Print the elements of list each element
'''
x=input('Enter a # seperated string')
list1=x.split('#')
print(list1)
for d in list1:
    print(d,len(d))   '''

#write a program to input of , seperated strings. convert into list then create a list in which keys are length of each of list and values are elements of list
'''
x=input('Enter a str with comma')
values=x.split(',')
keys=[]
for d in values:
    keys.append(len(d))
d1=dict(zip(keys,values))
print(d1)      '''

#write a map function print areas of circle in which the radius range from 5-10
'''
def area(r):
    return 3.14*r*r

#result= list(map(area,[5,6,7,8,9,10]))
result= list(map(area,[x for x in range(5,11)]))
print(result)       '''

#write a recursive function to print the fabonacci series upto n
'''
def fibb(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fibb(n-1)+fibb(n-2))

n=eval(input('Enter the number of items'))
for i in range(1,n+1):
    print(fibb(i))    '''

#write a program to find factorial of a number

import math
n=int(input('Enter the value of n: '))
print('Factorial of {} is {}'.format(n,math.factorial(n)))
