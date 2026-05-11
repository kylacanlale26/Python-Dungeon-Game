class Player: # blueprint for character
    def __init__(self, name, player_class, hp, atk, skill, skill_dmg):
        self.name = name
        self.player_class = player_class
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.skill = skill
        self.skill_dmg - skill_dmg
        self.inventory = []
        self.weapon = None
        self.armor = None
        
         # assign starting weapon based on class
        if self.player_class == "Warrior":
            self.inventory = ["Long Sword"]
        elif self.player_class == "Mage":
            self.inventory = ["Wand"]
        elif self.player_class == "Rogue":
            self.inventory = ["Dagger"]
        else:
            self.inventory = []

    # display player information
    def display_stats(self):
        print("\n===== PLAYER STATS =====")
        print(f"Name      : {self.name}")
        print(f"Class     : {self.player_class}")
        print(f"HP        : {self.hp}/{self.max_hp}")
        print(f"ATK       : {self.atk}")
        print(f"Skill     : {self.skill}")
        print(f"Inventory : {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("=" * 24) # boarder

# classes and stats
classes = {
    "1": {
        "name": "Warrior",
        "hp": 120,
        "atk": 15,
        "skill": "Shield Bash",
        "skill_dmg":25
    },
    "2": {
        "name": "Mage",
        "hp": 80,
        "atk": 25,
        "skill": "Fireball",
        "skill_dmg":40
    },
    "3": {
        "name": "Rogue",
        "hp": 90,
        "atk": 20,
        "skill": "Backstab",
        "skill_dmg":35
    }
}

def hero():

    # greetings
    print("\nHello, Hero!")

    # input player name
    name = input("\nWhat is your name?: ")

    # class choices
    print("\nChoose your class:")
    print("1. Warrior - HP: 120 | ATK: 15 | Skill: Shield Bash")
    print("2. Mage    - HP: 80  | ATK: 25 | Skill: Fireball")
    print("3. Rogue   - HP: 90  | ATK: 20 | Skill: Backstab")

    # choose class
    while True:
        choice = input("\nEnter class number (1-3): ")

        if choice in classes:
            selected = classes[choice]
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # create player
    player = Player(
        name=name,
        player_class=selected["name"],
        hp=selected["hp"],
        atk=selected["atk"],
        skill=selected["skill"],
        skill_dmg=selected["skill_dmg"]
    )

    # display player information
    player.display_stats()

    return player