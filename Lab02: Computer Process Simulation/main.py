"""Author: Shero Baig
KUID: 3093709
Date: Feb 10, 2023
Last Modified: Feb 10, 2023
"""
from process import Process

def main():
    #hand control over to process file
    name_file = input("Enter file name: ")
    control_process = Process(name_file)
    control_process.run()

if __name__ == "__main__":
    main()
