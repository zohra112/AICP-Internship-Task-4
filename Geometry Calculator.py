#A Python program which shows a simple geometry calculator that calculates and displays the
# properties of a hexagon and a square based on user input
import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length * self.side_length

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        print("Hexagon Properties:")
        print(f"  Area: {self.calcArea()}")
        print(f"  Perimeter: {self.calcPeri()}")
        print(f"  Sum of Angles: {self.calcAngleSum()}")

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length * self.side_length

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print("Square Properties:")
        print(f"  Area: {self.calcAreaSquare()}")
        print(f"  Perimeter: {self.calcPeriSquare()}")

# this chunk Input the last digit of your CNIC as the length of one side of hexagon
cnic_last_digit = int(input("Enter the last digit of your CNIC: "))
hexagon = Hexagon(cnic_last_digit)

# Display program heading
print("Geometry Calculator")

# Giving hoices as Input 1 to calculate and display hexagon properties, 2 for square properties,
# and any other input to exit
while True:
    # Displaying menu options
    print("\nChoose an option:")
    print("  1. Hexagon Properties")
    print("  2. Square Properties")
    print("  3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        hexagon.display()
    elif choice == '2':
        # Calculate length of one side of square
        square_side_length = cnic_last_digit + 1
        square = Square(square_side_length)
        square.display()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
