import sys
import time
import os
import random

inventory = []
health = 100
deaths = 0
xp = 0      # This tracks Khyan's growth
level = 1   # This shows Khan is getting stronger
def speak(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def save_game(location):
    with open("savegame.txt", "w") as f:
        f.write(f"{location}\n")
        f.write(",".join(inventory) + "\n")
        f.write(f"{health}\n")
        f.write(f"{deaths}\n")
        f.write(f"{xp}\n")
        f.write(f"{level}\n")
    speak("\n>>> PROGRESS SAVED.")

def load_game():
    global inventory, health, deaths, xp, level     
    if os.path.exists("savegame.txt"):
        with open("savegame.txt", "r") as f:
            lines = f.readlines()
            if len(lines) < 3: return None
            loc = lines[0].strip()
            inv = lines[1].strip().split(",") if lines[1].strip() else []
            inventory = [i for i in inv if i]
            health = int(lines[2])
            return loc
    return None
def skill_tree():
    global xp, health, level
    speak(f"\n--- SKILL MENU (XP: {xp} | Level: {level}) ---")
    speak("1. Increase Max Health (+20 HP) - Costs 50 XP")
    speak("2. Combat Training (Level Up) - Costs 100 XP")
    speak("3. Exit Menu")
    
    choice = input("\nSelect an upgrade: ")
    if choice == "1" and xp >= 50:
        health += 20
        xp -= 50
        speak(f"Vitality increased! Health is now {health}.")
    elif choice == "2" and xp >= 100:
        level += 1
        xp -= 100
        speak(f"Rank Up! You are now Level {level}.")
    elif choice == "3":
        return
    else:
        speak("Not enough XP or invalid choice.")
def combat(enemy_name, enemy_health):
    global health
    speak(f"\n!!! BOSS FIGHT: {enemy_name} !!!")
    while enemy_health > 0 and health > 0:
        speak(f"\n[ KHAN HP: {health} | {enemy_name} HP: {enemy_health} ]")
        action = input("Action: [1] Strike | [2] Dodge | [3] Power Move | [4] Analyze: ")
        if action == "1":
            dmg = random.randint(10, 20) if "Sharpened Bolt" in inventory else random.randint(5, 12)
            enemy_health -= dmg
            speak(f"You dealt {dmg} damage!")
        elif action == "3":
            if random.random() > 0.4:
                dmg = random.randint(25, 40)
                enemy_health -= dmg
                speak(f"POWER MOVE! You dealt {dmg} damage!")
            else:
                speak("You missed!")
                health -= 10
        elif action == "4":
            health = min(100, health + 15)
            speak("You recovered 15 HP.")
        
        if enemy_health > 0:
            e_dmg = random.randint(10, 18)
            if action == "2": e_dmg //= 3
            health -= e_dmg
            speak(f"{enemy_name} hits for {e_dmg}!")
    if health <= 0:
        speak("\nGAME OVER."); sys.exit()

def introduction():
    save_game("introduction")
    speak("--- KHAN QUEST: THE REBIRTH ---")
    speak("\nKhan steps off the bus. The high-vis vest feels like a neon target.")
    choice = input("\nDo you [1] Keep the vest | [2] Ditch it? ")
    if choice == "2":
        the_yard(stealth=15)
    else:
        the_yard(stealth=5)

def the_yard(stealth):
    save_game("the_yard")
    speak(f"\n--- THE YARD (Stealth: {stealth}) ---")
    if stealth > 10:
        speak("\nYou spot a loose stone. [1] Take the Sharpened Bolt | [2] Ignore it")
        if input("Choice: ") == "1":
            inventory.append("Sharpened Bolt")
    else:
        speak("\nGuards are watching too closely. You find nothing.")
    cell_block()

def cell_block():
    save_game("cell_block")
    speak("\n--- CELL BLOCK C ---")
    speak("Brick blocks your path. 'Welcome home, Khan. You got a gift for me?'")
    if "Sharpened Bolt" in inventory:
        speak("\nYou show the bolt. Brick grins. 'You still got that edge. Move along.'")
    else:
        speak("\nBrick shoves you against the bars. 'New fish got nothing.' Health -10.")
        global health
        health -= 10
    the_canteen()

def the_canteen():
    save_game("the_canteen")
    speak("\n--- THE CANTEEN ---")
    speak("The room is loud. A group of lifers is whispering in the corner.")
    choice = input("\nDo you [1] Sit with them | [2] Eat alone? ")
    if choice == "1":
        if "Sharpened Bolt" in inventory:
            speak("\n'We saw how you handled Brick.' They slide a SCRAP OF PAPER to you.")
            inventory.append("Scrap of Paper")
        else:
            speak("\n'Keep walking, kid.' They don't trust you.")
    the_laundry()

def the_laundry():
    save_game("the_laundry")
    speak("\n--- THE LAUNDRY ROOM ---")
    if "Scrap of Paper" in inventory:
        speak("\nThe paper leads to Machine 42. You find the GHOST RADIO.")
        inventory.append("Ghost Radio")
        speak("VOICE: 'Khan? We're getting you out. But someone is coming!'")
        combat("Senior Sergeant", 50)
        inventory.append("Sergeant's Badge")
        the_loading_dock()
    else:
        speak("\nYou have no lead. The guards catch you. GAME OVER.")
        sys.exit()

def the_loading_dock():
    save_game("the_loading_dock")
    speak("\n--- THE LOADING DOCK ---")
    speak("A truck is idling. Guards are nearby.")
    if "Sergeant's Badge" in inventory:
        speak("You use the badge to walk right past them into the truck.")
    else:
        speak("You sneak in while they aren't looking.")
    chapter_2_forest()

def chapter_2_forest():
    speak("\n--- THE FOREST ---")
    speak("You escape into the wilderness. Freedom tastes like pine and suspicion.")
    if "Sergeant's Badge" in inventory:
        speak("\nYou remember better times. The badge feels heavier now.")
    else:
        speak("\nYou find a safe shack hidden in the brush. It's a moment of peace.")
        inventory.append("First Aid Kit")
        # This calls the "Brain" you built on Line 40
        choice = input("Do you want to [1] Rest and Upgrade | [2] Keep moving? ")
        if choice == "1":
            skill_tree()
    speak("\nTo be continued...")
if __name__ == "__main__":
    saved_loc = load_game()
    if saved_loc:
        choice = input(f"Found a save at {saved_loc}. Load it? (y/n): ")
        if choice.lower() == 'y':
            # This looks up the function name from the save file
            globals()[saved_loc]()
        else:
            introduction()
    else:
        introduction()