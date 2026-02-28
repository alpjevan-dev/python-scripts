import json
import os
import sys
import time

# --- CORE GLOBALS ---
inventory = []
health = 100
deaths = 0
xp = 0
level = 1

def speak(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def save_game_json(location):
    """Architect Level: Structured Data Persistence"""
    player_state = {
        "location": location,
        "inventory": inventory,
        "health": health,
        "deaths": deaths,
        "xp": xp,
        "level": level
    }
    with open("state.json", "w") as f:
        json.dump(player_state, f, indent=4)
    print("\n>>> SYSTEM: PROGRESS SERIALIZED TO JSON.")

def load_game_json():
    """Architect Level: Schema Retrieval"""
    global inventory, health, deaths, xp, level
    if os.path.exists("state.json"):
        with open("state.json", "r") as f:
            data = json.load(f)
            inventory = data.get("inventory", [])
            health = data.get("health", 100)
            deaths = data.get("deaths", 0)
            xp = data.get("xp", 0)
            level = data.get("level", 1)
            return data.get("location")
    return None
def introduction():
    """Architect Entry Point: Boots the game and saves initial state."""
    speak("Welcome to Khan Quest.")
    speak("You wake up in a damp cell. Your architectural journey begins...")
    save_game_json("introduction")
    # Make sure this points to your next function, like cell_block()
    cell_block()
def the_yard(stealth):
    save_game_json("the_yard")
    speak(f"\n--- THE YARD (Stealth: {stealth}) ---")
    if stealth > 10:
        speak("\nYou spot a loose stone. [1] Take the Sharpened Bolt | [2] Ignore it")
        if input("Choice: ") == "1":
            inventory.append("Sharpened Bolt")
    else:
        speak("\nGuards are watching too closely. You find nothing.")
    cell_block()

def cell_block():
    save_game_json("cell_block")
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
    save_game_json("the_canteen")
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
    save_game_json("the_laundry")
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
    save_game_json("the_loading_dock")
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
    saved_loc = load_game_json()
    if saved_loc:
        choice = input("Found a save! Resume? (y/n): ")
        if choice.lower() == 'y' and saved_loc in globals():
            globals()[saved_loc]()
        else:
            introduction()
    else:
        introduction()