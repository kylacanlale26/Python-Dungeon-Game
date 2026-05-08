# GAME OVERALL SYSTEM | MENU + LEVELS + END GAME - JD & KYLA - game_system.py
def game():
        
    #game loop
    while True:
    
        print("\n====== PYTHON DUNGEON QUEST ======")

        print("\nWelcome to Python Dungeon Quest!")

        player = player_info()

        print("\nGame Objectives:")
        print("Clear 12 dungeons to win.")
        print("You only have 3 chances to succeed.")
        print(f"\nGood luck, hero {player['name']}!")

        #menu loop - JD
        while True:
            print("\n====== MAIN MENU ======")
            print("[1] Explore Dungeon\n[2] Visit Shop\n[3] Show Status\n[4] Show Defeated Enemies\n[5] Exit Game")
            menu = input("\nChoose option (1-5): ")

            #validate choice - checks if input is a digit or not included in the choices
            while menu not in ["1", "2", "3", "4", "5"]:
                menu = input("\nInvalid choice! Choose again (1-5 only): ")

            if menu == "1":
                adventure(player)

            elif menu == "2":
                shop(player)

            elif menu == "3": 
                show_status(player)

            elif menu == "4":
                show_defeated()

            elif menu == "5":
                print("\n" + "=" * 23)
                print("\nThanks for playing, , Hero {player['name']}!")
                break
