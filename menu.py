# from hero import Player
from items import use_item, discard_item

def menu(player):

    options = ["Player Stats", "Open Inventory", "Discard Items", "Exit"] #list of menu options
    
    while True:
            print("\n========= MENU =========")

            print() # space

            #display format of the options
            for i, item in enumerate(options, start=1):
                print(f"({i}) {item}")
            
            menu = input(f": ")

            #validate choice - checks if input is a digit or not included in the choices
            while menu not in ["1", "2", "3", "4"]:
                menu = input("\nInvalid choice! Choose again (1-4 only): ")

            if menu == "1":
                player.display_stats()

            elif menu == "2":
                use_item(player)

            elif menu == "3": 
                discard_item(player)

            elif menu == "4":
                print("\n" + "=" * 24) #boarder
                return