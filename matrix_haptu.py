import os
import random
import time
import colorama # This makes the colors work
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def matrix_rain():
    # List of characters to fall (Numbers, symbols, and HAPTU)
    chars = ["0", "1", "H", "A", "P", "T", "U", "!", "#", "$", "%", "&"]
    
    # Get the size of your terminal window
    columns = os.get_terminal_size().columns
    
    # Create a list to track the position of the "rain" in each column
    # If it's 0, it's not falling. If it's > 0, it's falling.
    drops = [0] * columns

    print(Fore.GREEN + "CONNECTING TO HAPTU_NET...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the screen

    try:
        while True:
            line = ""
            for i in range(columns):
                # Randomly start a new drop
                if drops[i] == 0 and random.random() > 0.975:
                    drops[i] = 1
                
                # If a drop is active, print a random character
                if drops[i] > 0:
                    char = random.choice(chars)
                    line += Fore.GREEN + char
                    drops[i] += 1
                    
                    # Randomly stop the drop so it doesn't fall forever
                    if drops[i] > random.randint(10, 30):
                        drops[i] = 0
                else:
                    line += " "
            
            print(line)
            time.sleep(0.05) # Adjust this to change the speed
            
    except KeyboardInterrupt:
        print(Style.RESET_ALL + "\nMatrix connection terminated.")

if __name__ == "__main__":
    # You might need to install colorama first! 
    # Run: pip install colorama
    matrix_rain()