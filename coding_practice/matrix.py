import os, random, time, sys

# Characters from your video
CHARS = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"
GREEN = "\033[32m"
BRIGHT = "\033[37m"
RESET = "\033[0m"

def run_rain():
    # Get terminal size
    try:
        cols, rows = os.get_terminal_size()
    except:
        cols, rows = 40, 20

    # Start drops at random heights so they fall individually
    drops = [random.randint(-rows, 0) for _ in range(cols)]

    while True:
        # 1. MOVE CURSOR TO TOP (Stops the scrolling)
        sys.stdout.write("\033[H")
        
        output = []
        for r in range(rows):
            line = ""
            for c in range(cols):
                head = drops[c]
                # 2. DRAW THE RAIN
                if r == head:
                    line += f"{BRIGHT}{random.choice(CHARS)}{RESET}" # Glowing head
                elif head - 10 < r < head:
                    line += f"{GREEN}{random.choice(CHARS)}{RESET}" # Fading tail
                else:
                    line += " " # Empty space
            output.append(line)
        
        # 3. PRINT ALL AT ONCE
        sys.stdout.write("\n".join(output) + "\n")
        sys.stdout.flush()

        # 4. UPDATE POSITIONS
        for i in range(cols):
            drops[i] += 1
            if drops[i] > rows + 10:
                drops[i] = random.randint(-5, 0)

        time.sleep(0.05) # Speed match for the video

if __name__ == "__main__":
    run_rain()