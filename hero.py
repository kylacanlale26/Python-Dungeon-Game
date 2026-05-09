class Player:
    def __init__(self, name, player_class, hp, atk, skill):
        self.name = name                  
        self.player_class = player_class 
        self.hp = hp                     
        self.atk = atk                    
        self.skill = skill                
        self.inventory = []             

    # Display player information
    def show_stats(self):
        print("\n===== PLAYER STATS =====")
        print(f"Name      : {self.name}")
        print(f"Class     : {self.player_class}")
        print(f"HP        : {self.hp}")
        print(f"ATK       : {self.atk}")
        print(f"Skill     : {self.skill}")
        print(f"Inventory : {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("========================")


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
player.show_stats()