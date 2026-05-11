import random
from items import pickup_item, weapons, armors, consumables

# bonus chest room
def bonus_chest(player):

    print("\n" + "=" * 24) # border

    print("\nYou found a chest!")
    
    loot_pool = list(weapons.keys()) + list(armors.keys()) + list(consumables.keys())
    item = random.choice(loot_pool) # picks one of the loot

    print(f"Chest contains: {item}") # print what loot is inside the chest
    pickup_item(player, item) # asks if player will pick up the loot

    print("\n" + "=" * 24) # border

# battle
def combat(player, enemy):
    
    # copies enemy hp for battle, so original value won't change after battle
    enemy_hp = enemy.hp

    print("\n===== COMBAT START =====")

    print(f"\nA wild {enemy.name} appears!")
    print(f"\n{enemy.description}")

    actions = ("Attack", "Defend", player.skill) # action option

    # while loop to check if the player and the monster are still alive
    while player.hp > 0 and enemy_hp > 0:

        # print choices
        print(f"\n1. {actions[0]}")
        print(f"2. {actions[1]}")
        print(f"3. {actions[2]}")

        choice = input("\nChoose: ") # ask player for input

        print("\n" + "=" * 24) # boarder

        # if the player chooses to attack
        if choice == "1":
            damage = player.atk 
            enemy_hp = max(0, enemy_hp - damage) # minus damage from monster hp
            print(f"\n{player.name} attacked the {enemy.name} for {damage} damage!") # print attack message

            # check if the monster is still alive to attack back
            if enemy_hp > 0:
                monster_damage = enemy.atk 
                player.hp = max(0, player.hp - monster_damage) # minus player HP
                print(f"\n{enemy.name} attacked back for {monster_damage} damage!") # print monster attack message

            print("\n" + "=" * 24) # boarder

        # if the player chooses to defend
        elif choice == "2":            
            print(f"\n{player.name} defended!") # print defend message
            monster_damage = enemy.atk 
            player.hp = max(0, player.hp - monster_damage) # minus player HP
            print(f"\n{enemy.name} attacked for only {monster_damage} damage!") # print lowered damage message
            print("\n" + "=" * 24) # boarder

        # if the player chooses to skill attack
        elif choice == "3":
            skill_damage = player.atk * 2
            enemy_hp = max(0, enemy_hp - skill_damage) # minus enemy HP
            print(f"\n{player.name} used {player.skill}!") # print used skill
            print(f"\nIt dealt {skill_damage} damage!") # print skill damage

            # check if the monster is still alive to attack back
            if enemy_hp > 0:
                monster_damage = enemy.atk
                player.hp = max(0, player.hp - monster_damage) # minus player HP
                print(f"\n{enemy.name} attacked back for {monster_damage} damage!") # print enemy attack

            print("\n" + "=" * 24) # boarder

        # if the input is not in the choices
        else:
            print("\nInvalid choice!")
            print("\n" + "=" * 24) # boarder

        # print current HP
        print(f"\n{player.name} HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy_hp}")

    # checks if player loses
    if player.hp <= 0:
        print("\n" + "=" * 24) # boarder
        print(f"\n{player.name} lost!")
        print("\n" + "=" * 24) # boarder

        return False

    print("\n" + "=" * 24) # boarder
    print(f"\n{player.name} won!")
    print("\n" + "=" * 24) # boarder

    # loot system pu from items.py
    loot_pool = list(weapons.keys()) + list(armors.keys()) + list(consumables.keys())

    # chance to drop item
    if loot_pool:
        dropped_item = random.choice(loot_pool) # picks one out of the loots
        print(f"\n{enemy.name} dropped {dropped_item}!") # prints what loot was dropped by monster
        pickup_item(player, dropped_item) # asks if player will pick up the loot
        print("\n" + "=" * 24) # boarder

    return True