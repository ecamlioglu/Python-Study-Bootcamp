"""
-------------------------------------------
This question is second week exercise in
Python Study Bootcamp in Kocaeli University
-------------------------------------------
QUESTION
Albert is studying in high school,
he wants to pass the Geometry Exam. 
create an eligible formulas for him 
Formulas contains regular shapes
Only necessary items appear
-------------------------------------------
prepared by Mert Mahanoğlu and Boran Akova
"""
#test different numbers for a,b,c.
import math
def main():
    a = 3
    b = 4
    c = 5
    total = (a + b + c) / 2
    pi = 3
    R = 5

    if a == b:
        SquareRec(a, b)
    else:
        SquareRec(a, b)
    if c - b < a and b + c > a:

        TriangleEqangle(a, b, c, total)

        Circle(R, pi)
def SquareRec(a, b):
    if a == b:
        print("Square Area = ", a * b)
    else:
        print("Rectangle Area = ", a * b)

def TriangleEqangle(a, b, c, total):
    if a == b or a == c:
        root = math.sqrt(3)
        print("Equilatreal Triangle Area = ", (a * a * root) / 4)
    elif a != b or b != c:
        print("Unequal Triangle Area = ", math.sqrt(total * (total - a) * (total - b) * (total - c)))
    else:
        print("Perpendicular Triangle Area = ")
        print("Area = ", (a * b / 2))

        
def Circle(R, pi):
    print("Circle Area  = ", (pi * pi * R))


main()

