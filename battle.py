def adventure(player):

    print("\n====== DUNGEON EXPEDITION ======")

    # dungeon selection - JUSTIN
    print("\nChoose dungeon:")
    print("[1] Forest Dungeon")
    print("[2] Ice Cave")
    print("[3] Dragon Castle")

    level_choice = input("\nEnter level (1-3): ")

    while level_choice not in ["1", "2", "3"]:
        level_choice = input("\nInvalid choice! Choose again (1-3): ")

    print("\n" + "=" * 32)

    if level_choice == "1":
        print("\nYou entered the Forest Dungeon.")
        print("\nDark trees surround the area.")

    elif level_choice == "2":
        print("\nYou entered the Ice Cave.")
        print("The cave is freezing cold.")

    elif level_choice == "3":
        print("\nYou entered the Dragon Castle.")
        print("The castle is full of fire.")

    print("\n" + "=" * 32)

    # enemy appears after selecting level
    enemy = enemy_picker()
    
    print(f"\nA wild {enemy['name']} appeared!")

    print("\n" + "=" * 32)
