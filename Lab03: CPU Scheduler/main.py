"""Author: Shero Baig
Lab: 3
KUID: 3093709
Date: Feb 17, 2023
Last Modified: Feb 17, 2023
"""



from scheduler import Scheduler

def main():
    #hand control over to process file
    name_file = input("Enter file name: ")
    my_exec = Scheduler(name_file)
    my_exec.run()

if __name__ == "__main__":
    main()
