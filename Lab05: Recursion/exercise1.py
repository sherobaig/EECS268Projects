"""Author: Shero Baig
Lab: 5
KUID: 3093709
Date: March 3, 2023
Last Modified: March 3, 2023
"""

def power_function(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        print("Sorry, your exponent must be zero or larger.")
        while True:
            try:
                new_exponent = int(input("Enter a power: "))
                return power_function(base, new_exponent)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

while True:
    try:
        base = int(input("Enter a base: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        exp = int(input("Enter a power: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

answer = power_function(base, exp)
print("Answer:", answer)
