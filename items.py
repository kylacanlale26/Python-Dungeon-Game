# ITEM SYSTEM

# This dictionary stores all weapon items in the game.
# Weapons increase player attack damage
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

# Armors increase player HP / defense
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

# Consumable items restore HP
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

# PICKUP ITEM FUNCTION
#This function handles item pickup.

def pickup_item(player, item_name):

    # Add item to inventory 
    player.inventory.append(item_name)

    print(f"\nYou picked up {item_name}!")

    # EQUIP WEAPON
    if item_name in weapons:

        weapon = weapons[item_name]

        player.atk += weapon["attack_bonus"]

        # player["weapon"] = item_name

        print(f"\n{item_name} equipped!")
        print(f"\nAttack increased by {weapon['attack_bonus']}")

    # EQUIP ARMOR
    elif item_name in armors:

        armor = armors[item_name]

        player.hp += armor["hp_bonus"]
        player.max_hp += armor["hp_bonus"]

        player.armor = item_name

        print(f"{item_name} equipped!")
        print(f"\nHP increased by {armor['hp_bonus']}")


# USE CONSUMABLE FUNCTION

def use_item(player):

    # Check if inventory is empty
    if not player.inventory:
        print("\nInventory is empty.")
        return

    print("\n======= INVENTORY ======")

    for index, item in enumerate(player.inventory, start=1):
        print(f"{index}. {item}")

    try:
        choice = int(input("\nChoose item number to use (0 to exit): "))

        print("\n" + "=" * 24) #boarder

        selected_item = player.inventory[choice - 1]

        if selected_item == "0":
            return

        # CHECK IF ITEM IS CONSUMABLE
        elif selected_item in consumables:

            potion = consumables[selected_item]

            heal_amount = potion["heal"]

            player.hp += heal_amount

            # Prevent HP overflow
            if player.hp > player.max_hp:
                player.hp = player.max_hp

            print(f"\nYou used {selected_item}!")
            print(f"\nYou restored {heal_amount} HP!")

            # Remove item after use
            player.inventory.remove(selected_item)

        else:
            print("\nThis item cannot be used.")

    except:
        print("\nInvalid choice.")


# DISCARD ITEM FUNCTION
# Allows the player to throw away unwanted items.

def discard_item(player):

    # Check if inventory is empty
    if not player.inventory:
        print("\nInventory is empty.")
        return

    print("\n====== INVENTORY ======")

    for index, item in enumerate(player.inventory, start=1):
        print(f"{index}. {item}")

    try:
        choice = int(input("\nChoose item number to discard (0 to exit): "))

        print("\n" + "=" * 24) #boarder

        removed_item = player.inventory.pop(choice - 1)

        print(f"\n{removed_item} discarded.")

        if removed_item == "0":
            return

    except:
        print("\nInvalid choice.")
