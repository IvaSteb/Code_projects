import math 

print("=================")
print("Area Calculator")  
print("=================")

for i in range(1, 6):

    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Circle")
    print("5. Quit")

    shape = int(input("Which shape:  "))  # Choose the shape

    if shape == 1:
        base = float(input("Base of the triangle: "))  # calculating area of triangle 
        height = float(input("Height of the triangle: "))
        area = 0.5 * (base * height)
        print(f"The area of triangle is: {area}")
        
    elif shape == 2:
        lenght = float(input("Length of the rectangle: ")) # calculating area of rectangle
        width = float(input("Width of the rectangle: "))
        area = lenght * width
        print(f"The area of rectangle is {area}")
    
    elif shape == 3:
        side = float(input("Side of the square: ")) # calculating area of square
        area = side ** 2
        print(f"The area of square is {area}")
        
    elif shape == 4:
        radius = float(input("Radius of the circle: ")) # calculating area of circle
        area = math.pi * radius
        print(f"The area of circle is {area}")
        
    elif shape == 5:
        print("Exit from the area calculator!") # Exit fro, programme
        break
    else: # If you select a number that is not in the list, you will be asked to enter another value.
        print("Choose the other shape!")