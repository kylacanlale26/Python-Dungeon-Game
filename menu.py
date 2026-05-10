# from hero import Player
from items import use_item, discard_item

def menu(player):

    options = ["Player Stats", "Open Inventory", "Discard Items", "Exit"] #list of menu options
    
    while True:
            print("\n========= MENU =========")

            #display format of the options | joins the list into one string
            formatted = " | ".join([f"[{i}] {item}" for i, item in enumerate(options, start=1)])
            
            menu = input(f"\n{formatted}\n: ")

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