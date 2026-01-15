"""Author: Shero Baig
Lab: 5
KUID: 3093709
Date: March 3, 2023
Last Modified: March 3, 2023
"""


def outbreak(day):
    if day == 1:
        return 6
    elif day == 2:
        return 20
    elif day == 3:
        return 75
    else:
        return outbreak(day-1) + outbreak(day-2) + outbreak(day-3)

while True:
    try:
        day = int(input("OUTBREAK!\nWhat day do you want a sick count for?: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if day <= 0:
    print("Invalid day")
else:
    sum = outbreak(day)
    print("Total people with flu:", sum)
