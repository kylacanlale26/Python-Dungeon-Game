def shop(player):

    shop_items = [
        ("Small Potion", 10, 20), #name, price, 
        ("Medium Potion", 20, 40),
        ("Large Potion", 35, 70)
    ]

    while True: #shop session
        print("\n====== SHOP ======")

        print(f"\nGold: {player['gold']}\n") #display gold count

        for index, item in enumerate(shop_items, start=1):
            print(f"[{index}] {item[0]} - {item[1]} Gold")
        print("[0] Exit Shop")

        choice = input("\nChoose item to buy (1-3 or 0): ")

        #validate input - checks if its a digit or included in the choices
        while choice not in ["1", "2", "3", "0"]: #loop to keep asking if invalid input
            choice = input("\nSelected option invalid. Choose again: ")

        if choice == "0":
            print("\n" + "=" * 18)
            print("\nLeaving shop...")
            return

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(shop_items):
                item = shop_items[choice - 1]

                if player["gold"] >= item[1]:
                    player["gold"] -= item[1]
                    player["hp"] = min(player["hp"] + item[2], player["max_hp"]) # Don't over-heal
                    player["inventory"].append(item[0])
                    print(f"\nYou bought {item[0]} and healed!")

                else:
                    print("\nNot enough gold!")

            # ask if player wants to continue shopping
            print("\n" + "=" * 18)

        again = input("\nBuy another potion? [yes/no]: ").lower()

        if again == "no":
            print("\n" + "=" * 18)
            print("\nLeaving shop...")
            return
