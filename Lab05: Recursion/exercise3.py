"""Author: Shero Baig
Lab: 5
KUID: 3093709
Date: March 3, 2023
Last Modified: March 3, 2023
"""


def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)

def is_fibonacci(num):
    v = 0
    while fibonacci(v) <= num:
        if fibonacci(v) == num:
            return True
        v += 1
    return False

def main():
    while True:
        try:
            user_input = input("Enter mode and value: ").split()
            if len(user_input) != 2:
                print("Invalid input. Please enter mode and value separated by a space.")
                continue
            mode, value_str = user_input
            value = int(value_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the value.")
    
    if mode == "-i":
        print(fibonacci(value))
    elif mode == "-v":
        if is_fibonacci(value):
            print(f"{value} is in the sequence")
        else:
            print(f"{value} is not in the sequence")
    else:
        print("Invalid mode")

if __name__ == '__main__':
    main()
