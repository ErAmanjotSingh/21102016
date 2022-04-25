# Assignment 1

# 1st question
print()
a = int(input("enter number:"))
b = int(input("enter number:"))
c = int(input("enter number:"))
sum = a + b + c
average = sum/3
print("average of numbers =",average)



# 2nd question
 
print()
tax_rate = 0.2                                                                          # 20%
SD = 10000                                                                   # Standard Deduction
DD = 3000                                                              # Department Deduction          
GI = int(input("Enter Gross Income: "))                                       # Gross Income
no_of_dependents = int(input("Enter number of dependents : "))
taxable_income = GI -SD-(DD * no_of_dependents)
print("Taxable Income:", taxable_income)
tax = taxable_income * tax_rate
print("Tax:", tax)



# 3rd question


SID=input("Enter the SID")
Name=input("Enter the name")
Gender=input("Enter your Gender ")
Course_name=input("Enter the course name")
CGPA=float(input("Enter your CGPA"))
STUDENT=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT)




# 4th question

print()
marks = [66,78,33,67,90,12]
print("Marks Before Sorting: ", marks)
marks.sort()
print("Marks After Sorting:", marks)



# 5th question

print()
color = ['red','green','white','black','pink','yellow']
print("color", color)
color.pop(3)
print("(a) color", color)
color = ['red','green','white','black','pink','yellow']
color[3:5] = ["purple"]
print("(b) color", color)
