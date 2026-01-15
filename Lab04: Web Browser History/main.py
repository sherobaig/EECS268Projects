"""Author: Shero Baig
Lab: 4
KUID: 3093709
Date: Feb 24, 2023
Last Modified: Feb 24, 2023
"""


from browser import Browser
def main():
    file_input = input("Enter the name of the input file: ")
    browser = Browser()
    with open(file_input, "r") as f:
        for i in f:
            i = i.strip()
            if i.startswith("NAVIGATE"):
                url = i.split(" ")[1]
                browser.navigate_to(url)
            elif i == "BACK":
                browser.back()
            elif i == "FORWARD":
                browser.forward()
            elif i == "HISTORY":
                print(browser.print_history())
            else:
                print(f"Invalid command: {i}")
if __name__ == '__main__':
    main()
