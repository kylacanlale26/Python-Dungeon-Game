import random

class Player:
    def __init__(self, name, player_class, hp, atk, skill):
        self.name = name
        self.player_class = player_class
        self.hp = hp
        self.atk = atk
        self.skill = skill
        self.inventory = []
        
         # Assign starting weapon based on class
        if self.player_class == "Warrior":
            self.inventory = ["Long Sword"]
        elif self.player_class == "Mage":
            self.inventory = ["Wand"]
        elif self.player_class == "Rogue":
            self.inventory = ["Dagger"]
        else:
            self.inventory = []

    # Display player information
    def display_stats(self):
        print("\n===== PLAYER STATS =====")
        print(f"Name      : {self.name}")
        print(f"Class     : {self.player_class}")
        print(f"HP        : {self.hp}")
        print(f"ATK       : {self.atk}")
        print(f"Skill     : {self.skill}")
        print(f"Inventory : {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("========================")


class Monster:
    def __init__(self, name, hp, atk, description, loot):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.description = description
        self.loot = loot


# classes and stats
classes = {
    "1": {
        "name": "Warrior",
        "hp": 120,
        "atk": 15,
        "skill": "Shield Bash (Stuns enemy)"
    },
    "2": {
        "name": "Mage",
        "hp": 80,
        "atk": 25,
        "skill": "Fireball (High AOE damage)"
    },
    "3": {
        "name": "Rogue",
        "hp": 90,
        "atk": 20,
        "skill": "Backstab (Critical hit chance)"
    }
}

#goblin, beast, undead, giant_beast, goblin_king
goblin = ["Goblin", 40]
beast = ["Beast", 70]
undead = ["Undead", 50]
giant_beast = ["Giant Beast", 200]
goblin_king = ["Goblin King", 200]

potion_loot = "Potion"
sword_loot = "Steel Sword"
armor_loot = "Knight Armor"

#welcome
print("HELLO HERO")

# input player name
name = input("What is your name?: ")

# class choices
print("\nChoose your class:")
print("1. Warrior - HP: 120 | ATK: 15 | Skill: Shield Bash")
print("2. Mage    - HP: 80  | ATK: 25 | Skill: Fireball")
print("3. Rogue   - HP: 90  | ATK: 20 | Skill: Backstab")

# choose class
while True:
    choice = input("Enter class number (1-3): ")

    if choice in classes:
        selected = classes[choice]
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Create player
player = Player(
    name=name,
    player_class=selected["name"],
    hp=selected["hp"],
    atk=selected["atk"],
    skill=selected["skill"]
)

# Display player information
player.display_stats()


def combat(player, enemy):
    
    enemy = enemy[:]  

    print("\n===== COMBAT START =====")
    print(f"A wild {enemy[0]} appears!")

    actions = ("Attack", "Defend", player.skill)

    # while loop to check if the player and the monster are still alive
    while player.hp > 0 and enemy[1] > 0:

        # print choices
        print(f"\n1. {actions[0]}")
        print(f"2. {actions[1]}")
        print(f"3. {actions[2]}")

        # ask player for input
        choice = input("Choose: ")

        # check if the player chooses to attack
        if choice == "1":

            # generate random damage from 5 to 10
            damage = random.randint(5, 10)

            # minus damage from monster hp
            enemy[1] = max(0, enemy[1] - damage)

            # print attack message
            print(f"\n{player.name} attacked the {enemy[0]} for {damage} damage!")

            # check if the monster is still alive to attack back
            if enemy[1] > 0:

                # generate monster damage from 4 to 8
                monster_damage = random.randint(4, 8)

                # minus player HP
                player.hp = max(0, player.hp - monster_damage)

                # print monster attack message
                print(f"{enemy[0]} attacked back for {monster_damage} damage!")

        # if the player chooses to defend
        elif choice == "2":

            # print defend message
            print(f"\n{player.name} defended!")

            # lower damage because player chose to defend
            monster_damage = random.randint(1, 4)

            # minus player HP
            player.hp = max(0, player.hp - monster_damage)

            # print lowered damage message
            print(f"{enemy[0]} attacked for only {monster_damage} damage!")

        # skill attack
        elif choice == "3":

            skill_damage = random.randint(8, 15)

            enemy[1] = max(0, enemy[1] - skill_damage)

            print(f"\n{player.name} used {player.skill}!")
            print(f"It dealt {skill_damage} damage!")

            if enemy[1] > 0:

                monster_damage = random.randint(10, 15)

                player.hp = max(0, player.hp - monster_damage)

                print(f"{enemy[0]} attacked back for {monster_damage} damage!")

        # if the input is not in the choices
        else:
            print("\nInvalid choice!")

        # print current HP
        print(f"\n{player.name} HP: {player.hp}")
        print(f"{enemy[0]} HP: {enemy[1]}")

    if player.hp <= 0:
        print(f"\n{player.name} lost!")
        print("Game Over!")
        return False

    print(f"\n{player.name} won!")

    return True


def adventure(player):

    current_room = 1
    room1_cleared = False
    room2_cleared = False

    while True:
        if player.hp <= 0:
            print("💀 Game Over!")
            break

        if current_room == 1:
            print("\n[Room 1: Overgrown Entrance] Vines crawl the walls. Path leads South.")
            act = input("(1) Explore (2) Go South (3) Stats: ")

            if act == "1":
                if combat(player, random.choice([goblin, beast])):
                    room1_cleared = True

            elif act == "2":
                # FIX: block skipping
                if room1_cleared:
                    current_room = 2
                else:
                    print("You must defeat Room 1 first!")

            elif act == "3":
                player.display_stats()

        elif current_room == 2:
            print("\n[Room 2: Sunken Armory] Rust and shadows. Paths: North, East.")
            act = input("(1) Explore (2) Go North (3) Go East (4) Stats: ")

            if act == "1":
                if combat(player, random.choice([undead, giant_beast])):
                    room2_cleared = True

            elif act == "2":
                current_room = 1

            elif act == "3":
                # FIX: block skipping boss room
                if room2_cleared:
                    current_room = 3
                else:
                    print("You must defeat Room 2 first!")

            elif act == "4":
                player.display_stats()

        elif current_room == 3:
            print("\n[Room 3: Boss Sanctum] The air is heavy. Path: West.")
            act = input("(1) FIGHT BOSS (2) Go West (3) Stats: ")

            if act == "1":
                if combat(player, goblin_king):
                    print("\nGAME COMPLETED: You have defeated the bosses and cleared the dungeon!")
                    break
                else:
                    break

            elif act == "2":
                current_room = 2

            elif act == "3":
                player.display_stats()


adventure(player)
