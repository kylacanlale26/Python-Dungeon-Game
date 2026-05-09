import random
def adventure(player):

    print("\n====== DUNGEON EXPEDITION ======")

    # dungeon selection - 
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
    if level_choice == "1":
        enemy = ["Goblin", 20]

    elif level_choice == "2":
        enemy = ["Ice Monster", 25]

    elif level_choice == "3":
        enemy = ["Dragon", 35]

    print(f"\nA wild {enemy[0]} appeared!")
    
    actions = ("Attack", "Defend")

    # while loop to check if the player and the monster are still alive
    while player[1] > 0 and enemy[1] > 0:

        # print choices
        print(f"\n1. {actions[0]}")
        print(f"2. {actions[1]}")

        # ask player for input
        choice = input("Choose: ")

        # check if the player chooses to attack
        if choice == "1":

            # generate random damage from 5 to 10
            damage = random.randint(5, 10)

            # minus damage from monster hp
            enemy[1] = enemy[1] - damage

            # print attack message
            print(f"\n{player[0]} attacked the {enemy[0]} for {damage} damage!")

            # check if the monster is still alive to attack back
            if enemy[1] > 0:

                # generate monster damage from 4 to 8
                monster_damage = random.randint(4, 8)

                # minus player HP
                player[1] = player[1] - monster_damage

                # print monster attack message
                print(f"{enemy[0]} attacked back for {monster_damage} damage!")

        # if the player chooses to defend
        elif choice == "2":

            # print defend message
            print(f"\n{player[0]} defended!")

            # lower damage because player chose to defend
            monster_damage = random.randint(1, 4)

            # minus player HP
            player[1] = player[1] - monster_damage

            # print lowered damage message
            print(f"{enemy[0]} attacked for only {monster_damage} damage!")

        # if the input is not in the choices
        else:
            print("\nInvalid choice!")

        # print current HP
        print(f"\n{player[0]} HP: {player[1]}")
        print(f"{enemy[0]} HP: {enemy[1]}")

    # print if the player won or lost depending on the players hp
    if player[1] > 0:
        print(f"\n{player[0]} won!")
        # chance to get a loot when u kill the enemy
        if random.random() < 0.5:  # 50% chance to find loot
            print(f"\n✨ {enemy[0]} dropped a loot bag! ✨")
            
            # Gold and XP
            gold_gain = random.randint(15, 40)
            xp_gain = random.randint(50, 100)
            print(f"💰 Found: {gold_gain} Gold")
            print(f"⭐ Gained: {xp_gain} XP")

        else:
            print(f"\nThe {enemy[0]} left behind nothing but dust.")
    else:
        print(f"\n{player[0]} lost!")
    
player = ["Hero", 30]

adventure(player)
