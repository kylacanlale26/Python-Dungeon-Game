# item system

# this dictionary stores all weapon items in the game.
# weapons increase player attack damage
weapons = {
    "Longsword": {
        "type": "Weapon",
        "attack_bonus": 5,
        "description": "A sharp steel sword used by warriors."
    },

    "Magic Staff": {
        "type": "Weapon",
        "attack_bonus": 8,
        "description": "A staff infused with magical power."
    },

    "Dagger": {
        "type": "Weapon",
        "attack_bonus": 4,
        "description": "A small blade perfect for quick attacks."
    }
}

# armors increase player hp / defense
armors = {
    "Leather Armor": {
        "type": "Armor",
        "hp_bonus": 15,
        "description": "Light armor made from hardened leather."
    },

    "Knight Armor": {
        "type": "Armor",
        "hp_bonus": 25,
        "description": "Heavy armor worn by elite knights."
    },

    "Mystic Robe": {
        "type": "Armor",
        "hp_bonus": 20,
        "description": "A magical robe used by ancient mages."
    }
}

# consumable items restore hp
consumables = {
    "Healing Potion": {
        "type": "Consumable",
        "heal": 30,
        "description": "Restores 30 HP."
    },

    "Mega Potion": {
        "type": "Consumable",
        "heal": 60,
        "description": "Restores 60 HP."
    }
}

# pickup item system
# this function handles item pickup
def pickup_item(player, item_name):
            
        while True: # keep asking until valid input
            pick_up = input("\nPick up loot (yes/no)\n: ").lower() # converts input to lowercase

            print("\n" + "=" * 24) # boarder
   
            if pick_up == "yes":
                player.inventory.append(item_name) # add item to inventory
                print(f"\nYou picked up {item_name}!")

                # equip weapon
                if item_name in weapons: # checks if the picked item is a weapon
                    weapon = weapons[item_name] # gets the weapon stats
                    player.atk += weapon["attack_bonus"] # increase players attack as bonus
                    player.weapon = item_name # saves the equipped weapon
                    print(f"\n{item_name} equipped!")
                    print(f"\nAttack increased by {weapon['attack_bonus']}")

                # equip armor
                elif item_name in armors: # checks if the picked item is an armor
                    armor = armors[item_name] # gets the armor stats
                    player.hp += armor["hp_bonus"] # increase current hp
                    player.max_hp += armor["hp_bonus"] # also increase max hp
                    player.armor = item_name # saves the equipped armor
                    print(f"{item_name} equipped!")
                    print(f"\nHP increased by {armor['hp_bonus']}")
                break

            elif pick_up == "no":
                print(f"\nYou left {item_name} behind.")
                break

            else:
                print("\nInvalid choice. Please type 'yes or 'no'.")
                

# use consumable function
def use_item(player):

    # check if inventory is empty
    if not player.inventory:
        print("\n" + "=" * 24) # boarder
        print("\nInventory is empty.")
        return

    print("\n======= INVENTORY ======")

    for index, item in enumerate(player.inventory, start=1):
        print(f"{index}. {item}")

    try:
        choice = int(input("\nChoose item (potion) number to use (0 to exit): "))
        print("\n" + "=" * 24) # boarder

        selected_item = player.inventory[choice - 1]

        if selected_item == "0":
            return

        # check if item is consumable
        elif selected_item in consumables:
            potion = consumables[selected_item]
            heal_amount = potion["heal"]
            player.hp += heal_amount

            # prevent hp overflow
            if player.hp > player.max_hp:
                player.hp = player.max_hp

            print(f"\nYou used {selected_item}!")
            print(f"\nYou restored {heal_amount} HP!")

            # remove item after use
            player.inventory.remove(selected_item)

        else:
            print("\nThis item cannot be used.")

    except:
        print("\nInvalid choice.")


# discard item function
# allows the player to throw away unwanted items.
def discard_item(player):

    # check if inventory is empty
    if not player.inventory:
        print("\nInventory is empty.")
        return

    print("\n======= INVENTORY ======")

    for index, item in enumerate(player.inventory, start=1):
        print(f"{index}. {item}")

    try:
        choice = int(input("\nChoose item number to discard (0 to exit): "))
        print("\n" + "=" * 24) # boarder
        removed_item = player.inventory.pop(choice - 1) # removes discarded item in inventory
        print(f"\n{removed_item} discarded.")

        if removed_item == "0":
            return

    except:
        print("\nInvalid choice.")
