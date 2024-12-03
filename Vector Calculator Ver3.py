import time
import math

#Equations:
def polar_to_rectangular(magnitude, angle_deg):
    #Convert polar coordinates to rectangular.
    angle_rad = math.radians(angle_deg)
    x = magnitude*math.cos(angle_rad)
    y = magnitude*math.sin(angle_rad)
    return (x, y)

def rectangular_to_polar(x, y):
    #Convert rectangular coordinates to polar.
    magnitude = math.sqrt(x**2+y**2)
    angle_deg = math.degrees(math.atan2(y, x))
    return (magnitude, angle_deg)

def vector_addition(v1, v2):
    #Add two vectors in rectangular form.
    return (v1[0]+v2[0],v1[1]+v2[1])

def dot_product(v1, v2):
    #Calculate the dot product of two vectors.
    return v1[0]*v2[0]+v1[1]*v2[1]

def cross_product(v1, v2):
    #Calculate the cross product (z-component for 2D vectors).
    return v1[0]*v2[1]-v1[1]*v2[0]

def get_vector(prompt):
    #Prompt the user to input a vector in polar or rectangular form.
    print(prompt)
    time.sleep(1)
    form = input("Enter [P] for polar or [R] for rectangular: ").strip().upper()
    while form not in ['P', 'R']:
        form = input("Invalid input. Please enter [P] for polar or [R] for rectangular: ").strip().upper()


    if form == 'P':
        magnitude = float(input("Enter the magnitude: "))
        angle = float(input("Enter the angle (in degrees): "))
        return polar_to_rectangular(magnitude, angle), 'rectangular'
    else:
        x = float(input("Enter the x component: "))
        y = float(input("Enter the y component: "))
        return (x, y), 'rectangular'



#User Interactions
print("Welcome to the Vector Calculator")
time.sleep(1)
print("Will this operation be addition or multiplication?")
time.sleep(1)

calc = input("Enter [A] for addition or [M] for multiplication: ").strip().upper()
while calc != "A" and calc != "M":
    calc = input("Please enter a valid command, either [A] for addition or [M] for multiplication:").strip().upper()

if calc == "A":
    print("You have chosen Addition")
    time.sleep(1)

    v1, _ = get_vector("First vector.")
    v2, _ = get_vector("Second vector.")

    result = vector_addition(v1, v2)
    print(f"The result of vector addition is: {result}")

elif calc == "M":
    print("You have chosen Multiplication")
    time.sleep(1)

    operation = input("Enter [D] for dot product or [C] for cross product: ").strip().upper()
    while operation not in ['D', 'C']:
        operation = input("Invalid input. Please enter [D] for dot product or [C] for cross product: ").strip().upper()

    v1, _ = get_vector("Enter the first vector.")
    v2, _ = get_vector("Enter the second vector.")


    if operation == 'D':
        result = dot_product(v1, v2)
        print(f"The result of the dot product is: {result}")
    elif operation == 'C':
        result = cross_product(v1, v2)
        print(f"The result of the cross product is: {result}")
        