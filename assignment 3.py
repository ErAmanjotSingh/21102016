import math
print("_____________________________________________________________")
print("Program 1")
num=int(input("Enter Your Number:"))
a=bin(num)
print(a)

print("_____________________________________________________________")
print("Program 2")

term_math = input('Enter a mathematical expression:')
print('Result :',eval(term_math))


print("_____________________________________________________________")
print("Program 3")
a=(3+4)*(5)
print(a)
n=int(input("Enter the Number:"))
b=((n)*(n-1))/2
print(b)
r=float(input("Enter the Radius of circle:"))
c=4*math.pi*(r**2)
print("c=",c)
d=math.sqrt(r*((math.cos(a)**2))+r*(math.sin(b)**2))
print("d=",d)
y2=int(input())
y1=int(input())
x2=int(input())
x1=int(input())
e=(y2-y1)/(x2-x1)
print("e=",e)

print("_____________________________________________________________")
print("Program 4")
print("a)")
for i in range(5):
    print(i,end=" ")
print()


print("b)")
for q in range(3,10):
    print(q,end=" ")
print()

print("c)")
for j in range(4,13,3):
    print(j,end=" ")
print()

print("d)")
for k in range(15,5,-2):
    print(k,end=" ")
print()



print("e)")
for m in range(5,3):
    print(m,end=" ")
print()



print("_____________________________________________________________")
print("Program 5")
h= int(input("enter number of hydrogen atoms : "))
c= int(input("enter number of carbon atoms : "))
o= int(input("enter number of oxygen atoms : "))
d=(h*1.00794)+(c*12.0107)+(o*15.9994)
print("combined molecular weight of all atoms is :",d)
