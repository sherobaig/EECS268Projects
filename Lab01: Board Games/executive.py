from boardgame import BoardGame


class Executive:
    def __init__(self, filename):
        self.filename = filename
        self.games_list = []
        with open(self.filename, "r") as file_open:
            for line in file_open:
                new_line = line.strip().split('\t')
                self.games_list.append(new_line)

    def user_menu(self):

        print("1) Print all games highest Gibbons range to lowest.")
        print("2) Print all games from a year")
        print("3) Time for a game?")
        print("4) The People VS Dr. Gibbons")
        print("5) Print based on ranking")
        print("6) Exit the program")

    def Gibbons_rating_sorted(self):

        gibbons_rating_list = []
        for i in self.games_list:
            gibbons_rating_list.append(i[0:2])
        list_sort = sorted(gibbons_rating_list, key=lambda item: float(item[1]), reverse=True)
        for i in list_sort:
            print(i[0])

    def games_from_year(self):

        games_year_list = []
        for i in self.games_list:
            games_year_list.append([i[0], i[3]])
        while True:
            try:
                obtain_year_user = int(input("Enter a year: "))
                break
            except:
                print("Invalid number. Try again.")
        for i in games_year_list:
            if int(i[1]) == obtain_year_user:
                print(i[0])

    def time_for_a_game(self):

        while True:
            try:
                time_played = int(input("How much time do you have to play in minutes?: "))
                break
            except:
                print("Invalid number. Try again.")
        list_games_time = []
        for i in self.games_list:
            list_games_time.append([i[0], i[5]])
        for i in list_games_time:
            if int(i[1]) <= time_played:
                print(i[0])

    def people_vs_gibbons(self):

        while True:
            try:
                different_rating = float(input("Enter a number between 0 and 10 to search by rating differences (decimals allowed): "))
                if different_rating < 0 or different_rating > 10:
                    raise ValueError
                break
            except:
                print("Invalid input. Try again")

        combination_list = []
        for i in self.games_list:
            combination_list.append(i[0:3])
        for i in combination_list:
            if abs(float(i[1]) - float(i[2])) >= different_rating:
                print(i[0])

    def ranking_order(self):

        while True:
            try:
                ranking = float(input("Enter a ranking: "))
                if ranking < 0 or ranking > 10:
                    raise ValueError
                break
            except:
                print("Invalid input. Try again")
        for i in self.games_list:
            if float(i[1]) >= ranking:
                print(i[0])

    def run(self):

        decision = ""
        while decision != "6":
            self.user_menu()
            decision = input("Enter a choice: ")
            if decision == "1":
                self.Gibbons_rating_sorted()
                print("")
            elif decision == "2":
                self.games_from_year()
                print("")
            elif decision == "3":
                self.time_for_a_game()
                print("")
            elif decision == "4":
                self.people_vs_gibbons()
                print("")
            elif decision == "5":
                self.ranking_order()
                print("")
            elif decision == "6":
                print("Exiting program...")
            else:
                print("Invalid choice. Please try again.")
                print("")
