"""
print("Hello world", "add nothing")
print(10*"add nothing")
#comment in sinle line




print("Enter your number :")
n=input()
print("Your number is",n)

print("Enter a string :")
a=input()
print("Present string is",a+'cd')

num=input("Enter a number ")
print(num)
name=raw_input("What is your name ")
print name
print(type(num))
print(type)


n1=input("Enter first number : ")
n2=input("Enter second number :")
print("Sum of two numbers are :",n1+n2)

mystr="Hii My name is Dipannita"
print(mystr)
print(mystr[5])
print(mystr[0:4])
print(len(mystr))
print(mystr[0:22:2])
print(mystr[::])
print(mystr[-5:-2])
print(mystr[5:2:-1])
print(mystr.endswith('tad'))
print(mystr.find("name"))
print(mystr.lower())
print(mystr.replace('Dipannita','Souav'))

grocery=["dal","rice","deo","vim",56]
print(grocery)
print(grocery[1])
print(grocery[::-2])
number=[1,7,5,3,10]
print(number)
number.sort()
print(number)
number.reverse()
number.append(71)
number.insert(2,55)
number.remove(7)
number.pop()

print(number)

tp=(1,2,3)
print(tp)
a=10
b=20
a,b=b,a
print(a,b)

d1={"Dipa":"fish","sourav":"vat","Pupu":"milk"}
print(d1)
print(d1["sourav"])
del d1["sourav"]
print(d1)
d1["Gourav"]="phone"
print(d1)

d3={"mutable":"can change","immutable":"cant change","1":"one","2":"two"}
print("enter a word :")
n=raw_input()
print(d3[n])


n=input("Enter your age :")
if(n>18):
    print("you can drive")
elif(n==18):
    print("not decided")
else:
    print("you cant")

list=[1,"new",7,"old",8,12,3,4,"dps",10,0,2,5,"sou",9]

for item in list:
    if str(item).isnumeric() and item>=6 :
        print(item)
      

i=0
while(True):
    if(i<10):
        i=i+1
        continue
    if(i==20):
        break
    print(i)
    i=i+1]

guess=5
n=18
while(guess):

        print("Enter a number :")
        take=input()
        if(take>n):
            print("Guess a smaller number")
            guess=guess-1
        elif(take<n):
            print("Guess a large number")
            guess=guess-1
        else:
            print("You win..")
            break

    
if(guess==0):
    print("You loss")

num1=input("enter a number:")
num2=input("Enter another number :")
try:
    print("Sum of two numbers :", num1+num2)
except Exception as r:
    print(r)
print("this is important")


#factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print("Enter a number")
n=input()
fac=fact(n)
print("Factorial of", n ,fac)


#fibonacci
def fib(n):
    if  n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=input("Enter the number :")
z=fib(n)
print("Result ",z)


#print pattern
num=input("Enter the number of row ")
print("Enter 0 or 1")
val=input()
if val==1:
    for i in range(0,num+1):
        print("*"*i)
if val==0:
    for i in range(num,0,-1):
        print("*"*i)


#Lambda function
#def a_first(a):
    #return a[0]

a_first=lambda a:a[1]


a=[[5,14],[23,0],[1,19],[8,5]]
print("Before sorting",a)
a.sort(key=a_first)
print("After sorting",a)

me="Misty" 
a1="3" 
b="dipannita"
a=f"this is {me} {a1} {b}"
print(a)


"""

def funargs(*ar,**kwar):
    print(ar)
    print(kwar)
list=["aa","b","c","d","e"]
dic={"1":"one","2":"two","3":"three"}
funargs(*list,**dic)