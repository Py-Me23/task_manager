# ask user to input the  the 3 sides of a triangle
x= float(input("Enter the first side:\n"))
y= float(input("Enter the second side:\n"))
z= float(input("Enter the third side:\n"))
#if all sides are equal print Equilateral
if x==y and y==z:
    print(f"The triangle is an equilateral")
#if 2 sides are equal print Isosceles
elif x==y or x==z or y==z:
    print(f"The triangle is an isosceles")
#if no sides are equal print scalene
else:
    print(f"The triangle is a scalene")