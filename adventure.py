import random
from rooms import combat, bonus_chest
from monsters import enemies_room1, enemies_room2, boss_enemy
from menu import menu

# room events
def room(player, enemies):

    event = random.choice(["combat", "chest", "empty"]) # pick random room event

    if event == "combat":
        return combat(player, random.choice(enemies)) # this clears the room that will allow player to be able to move to next room

    elif event == "chest":
        bonus_chest(player) # bonus chest event
        return False   # will not clear the room, only a bonus event

# adventure | navigate between rooms
def adventure(player):

    # tracks game progress
    current_room = 1
    room1_cleared = False
    room2_cleared = False

    # adventure loop
    while True:

        # checks if game over
        if player.hp <= 0:
            print("\nGame Over!")
            break

        # room system
        if current_room == 1: # starting room
            print("\n[Room 1: Overgrown Entrance]") # room name
            print("\nVines crawl the walls. Path leads South.") # room description

            act = input("\n(1) Explore | (2) Go South | (3) Menu\n: ") # action option

            if act == "1": # room event
                if room(player, enemies_room1): # picks room event
                    room1_cleared = True # marks room 1 as cleared

            elif act == "2": # move to next room
                print("\n" + "=" * 24) # boarder

                if room1_cleared: # block skipping
                    current_room = 2

                else:
                    print("\nYou must defeat a monster in Room 1 first!")
                    print("\n" + "=" * 24) # boarder

            elif act == "3": # display menu
                menu(player)

        elif current_room == 2:
            print("\n[Room 2: Sunken Armory]") # room name
            print("\nRust and shadows. Paths: North, East.") # room description

            act = input("\n(1) Explore | (2) Go North | (3) Go East | (4) Menu\n: ") # action option

            if act == "1": # room event
                if room(player, enemies_room2): # pick random room event
                    room2_cleared = True # marks room 2 cleared

            elif act == "2": # go back to room 1
                current_room = 1

            elif act == "3": # move to next room
                print("\n" + "=" * 24) # boarder

                if room2_cleared: # block skipping
                    current_room = 3

                else:
                    print("\nYou must defeat a monster in Room 2 first!")
                    print("\n" + "=" * 24) # boarder

            elif act == "4": # display menu
                menu(player)

        elif current_room == 3:
            print("\n[Room 3: Boss Sanctum] The air is heavy. Path: West.") # room name
            print("\nThe air is heavy. Final battle awaits. Path: West.") # room description

            act = input("\n(1) FIGHT BOSS | (2) Go West | (3) Menu\n: ") # action option

            if act == "1": #room event - boss fight

                # win
                if combat(player, boss_enemy):
                    print("\nGAME COMPLETED: You have defeated the bosses and cleared the dungeon!")
                    break

                else: # lose
                    print("\nGame Over!")
                    break

            elif act == "2": # go back room 2
                current_room = 2

            elif act == "3": # display menu
                menu(player)