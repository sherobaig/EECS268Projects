
"""Author: Shero Baig
Lab: 4
KUID: 3093709
Date: Feb 24, 2023
Last Modified: Feb 24, 2023
"""



from linkedlist import LinkedList
class Browser:
    
    def __init__(self):
        self.historylist =[]
        self.now = -1
    
    def navigate_to(self, url):
        self.historylist = self.historylist[:self.now +1]
        self.historylist.append(url)
        self.now = len(self.historylist) - 1
    
    def forward(self):
        if self.now < len(self.historylist) - 1:
            self.now += 1
    def back(self):
        if self.now > 0:
            self.now -= 1
    def print_history(self):
        output = "Oldest\n===========\n"
        for value, website in enumerate(self.historylist):
            if value == self.now:
                output += website + "<==current\n"
            else:
                output += website + "\n"
        output += "===========\nNewest\n"
        return output
