#1
'''vowels=['a','e','i','u','o']
s=input("Enter the string: ").lower()
c=0
for i in s:
    if i in vowels:
        c+=1
print(c)        '''
#2
'''def fun(length,start):
    for i in range(start,length+start):
        print(i,end=" ")
   
length=int(input("Enter the length of the array: "))
start=int(input("Enter the start of the array: "))
fun(length,start)'''
#2
'''def generate_sequence(length, start):
    return [start + i for i in range(length)]

l=int(input("Enter the length of the array: "))
s=int(input("Enter the start of the array: "))
print(generate_sequence(l, s))  '''
#3
'''list=[]
for i in range(5):
    list.append(int(input("Enter the number: ")))
list.sort()
print(list)
list.sort(reverse=True)
print(list)'''
#4
'''def devisible(num):
    if num%3==0 and num%5!=0:
        return "Fizz"
    elif num%3!=0 and num%5==0:
        return "Buzz"
    elif num%3==0 and num%5==0:
        return "FizzBuzz"
num=int(input("Enter the number: "))
print(devisible(num))'''
#5
'''def ReversedString(s):
    return s[::-1]
s=input("Enter the string: ")
print(ReversedString(s))'''
#6
'''import math
def AreaAndCircumference(r):
    print(f"Area of circle is: {math.pi*r*r:.2f}")
    print(f"Circumference of circle is: {2*math.pi*r:.2f}")
r=float(input("Enter the radius: "))
AreaAndCircumference(r)'''
#7
'''import re
name=input("Enter your name: ").strip()
while not name.replace(" ", "").isalpha():
    print("Invalid input. Please enter a valid name.")
    name=input("Enter your name: ").strip()
email=input("Enter yout email: ").strip()
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
while not re.match(email_pattern, email):
    print("Invalid input. Please enter a valid email.")
    email=input("Enter your email: ").strip()
print("My name is {0} and my email is {1}".format(name,email))'''

#8
'''text=input("Enter text: ")
c=0
c=text.count("iti")
print("iti found {0} times".format(c))'''
#9
'''def longest_alphabetical_substring(s):
    longest = current = s[0]
    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            current += s[i]
        else:
            if len(current) > len(longest):
                 longest = current
            current = s[i] 
    if len(current) > len(longest):
        longest = current
    print(f"Longest substring in alphabetical order is: {longest}")
s=input("Enter the text: ")
longest_alphabetical_substring(s)'''