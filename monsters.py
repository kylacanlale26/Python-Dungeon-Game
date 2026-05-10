class Monster: # blueprint for monster
    def __init__(self, name, hp, atk, description):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.description = description

#goblin, beast, undead, giant_beast, goblin_king
goblin = Monster(
    name="Goblin",
    hp=40,
    atk=8,
    description="A sneaky green creature hiding in the shadows.",
)

beast = Monster(
    name="Beast",
    hp=70,
    atk=12,
    description="A wild beast with razor sharp claws.",
)

undead = Monster(
    name="Undead",
    hp=50,
    atk=10,
    description="A cursed warrior revived from the dead.",
)

giant_beast = Monster(
    name="Giant Beast",
    hp=120,
    atk=18,
    description="A massive monster that shakes the dungeon floor.",
)

goblin_king = Monster(
    name="Goblin King",
    hp=200,
    atk=25,
    description="The ruler of the goblins and master of the dungeon.",
)

# groups of enemy that can randomly spawn in each room
enemies_room1 = [goblin, beast]
enemies_room2 = [undead, giant_beast]
boss_enemy = goblin_king