#program to calculate the average of two numbers.
#take two numbers as input
#declare the average variable 
#declare average =(num1 + num2)/2
#display the average.


num1=int(input("enter number\n"))
num2=int(input("enter number\n"))
average= int(num1+num2)/2
print(f" The average is {average}")

# accept an age input from the user
#if the age is less than 18 and the average is equal to 20,
#print {name}, you are not allowed to vote
#if the age is greater than or equal to 18 and average is greater than or equal to 20
#print{name} you are allowed to vote
#if the age is greater than or equal to 18 or the average is 10
#print{name},you are allowed to vote


username= input("Enter your full name:\n")
age= int(input("Enter your age:\n"))
if age <18 and average==20:
    print(f"{username}, You are not allowed to vote")
    
elif age>= 18 and average>=20:
    print(f"{username}, You are allowed to vote")

elif age>= 18 or average==10:
    print(f"{username},You are allowed to vote")