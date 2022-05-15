print("Program 1")
input_string = "Python is a case sensitive language"
leng = 0  # variable to store length of string
index_1 = 0  # variable to store index of "a case sensitive language"
index_2 = 0  # variable to store index of "a"

leng = len(input_string)  # find length of string
print("Length of entered string is : " + str(leng) + "\n")  # print length of string

print("String after being reversed is : " + input_string[::-1] + "\n")  # reverse the string and print it

index_1 = input_string.find("a case sensitive language")  # find index of "a case sensitive language"
new_string = input_string[index_1:]  #  assign "a case sensitive language" to a new variable
print(new_string + " has been assigned to \"new_string\" \n")  # print the new variable

input_string = input_string[0:(index_1 + 1)] + " Object Orient Language"  # replace "case sensitive language" with "Object orient language"
print("String has been changed to : " + input_string + "\n")  # print it

index_2 = input_string.find("a")  # find index of "a"
print("Index of \"a\" is " + str(index_2) + "\n")  #print it

print("Here is the string after removing white spaces : " + input_string.strip())  # remove the white spaces and print them


print("Program 2")
name = input("Enter your name ")  # take name as input from user
sid = int((input("Enter your SID ")))  # take SID as input from user
depar = input("Enter your department ")  # take Department as input from user
cgpa = float(input("Enter your CGPA "))  # take CGPA as input from user

print("Hey, " + name + " Here!")  # print the name
print("My SID is " + str(sid))  # print the SID
print("I am from " + depar + " and my CGPA is " + str(cgpa))  # print the Department and CGPA

print("Program 3")
a = 56  # Declare value of a from question
b = 10  # Declare value of b from question

print("a is " + str(a))  # print value of a
print("b is " + str(b) + "\n")  # print value of b

print("a & b = " + str(a & b))  # Calculate bitwise and, and print it
print("a | b = " + str(a | b))  # Calculate bitwise or, and print it
print("a ^ b = " + str(a ^ b))  # Calculate bitwise xor, and print it
print("a left shift by 2 bit is " + str(a << 2))  # left shift a by 2 bit and print it
print("b left shift by 2 bit is " + str(b << 2))  # left shift b by 2 bit and print it
print("a left shift by 2 bit is " + str(a >> 2))  # right shift a by 2 bit and print it
print("b left shift by 2 bit is " + str(b >> 2))  # right shift b by 2 bit and print it

print("Program 4")
   
string = input("Enter a String ")  # take a string input form user

if "name" in string:  # check if name is present in the string
    print("Yes")      # if yes print "Yes"
else:
    print("No")       # else print "No"

print("Program 5")

side_1 = 0  # Variable to store first side of triangle
side_2 = 0  # Variable to store second side of triangle
side_3 = 0  # Variable to store third side of triangle

# Variables to store sum of two sides
sum_1 = 0
sum_2 = 0
sum_3 = 0

side_1 = int(input("Enter First side of the Triangle "))  # Take first side as input form user
side_2 = int(input("Enter Second side of the Triangle "))  # Take second side as input form user
side_3 = int(input("Enter Third side of the Triangle "))  # Take third side as input form user

# Calculate sum of sides taken 2 at a time
sum_1 = side_2 + side_3
sum_2 = side_1 + side_3
sum_3 = side_1 + side_2

if (sum_1 > side_1) & (sum_2 > side_2) & (sum_3 > side_3):  # Check if sum of sides is greater than third side
    print("Yes")                                            # if so print "Yes"
else:
    print("No")                                             # print "No"

print("Program 6")
# Get the value of a and b
a = int (input("Enter the Value of a: "))
b = int(input("Enter the Value of b: "))
# Calculating xor of a and b
num = a ^ b
Count_flipped_bit = 0
# Counting Number of set bit present
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)



