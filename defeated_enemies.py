#displays defeated enemies - defeated_enemies.py

defeated_enemies = set() #set - store defeated enemies

def show_defeated():

    print("\n====== DEFEATED ENEMIES ======")
    if not defeated_enemies:
        print("\nNo enemies defeated yet.")
    else:
        for enemy in defeated_enemies:
            print("-", enemy)
