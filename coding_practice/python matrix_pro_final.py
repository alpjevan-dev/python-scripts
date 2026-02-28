import pygame
import random

pygame.init()

# Fullscreen setup for your ThinkPad
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

# 3D Depth Fonts
chars = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"
font_sizes = [14, 20, 28] 
fonts = [pygame.font.SysFont('ms gothic', s) for s in font_sizes]

# Aesthetic Colors
WHITE = (230, 255, 230)
BRIGHT_GREEN = (0, 255, 70)
DEEP_GREEN = (0, 100, 30)
BLACK = (0, 0, 0)

# Saturated Column Setup
column_spacing = 10 
column_count = width // column_spacing
drops = []

for i in range(column_count):
    layer = random.choices([0, 1, 2], weights=[0.4, 0.4, 0.2])[0]
    drops.append({
        'x': i * column_spacing,
        'y': random.randint(-height, 0),
        'speed': random.uniform(2, 4) if layer == 0 else random.uniform(5, 8),
        'layer': layer
    })

clock = pygame.time.Clock()
run = True

while run:
    # This Alpha (15) creates the "Wall of Green" look from your video
    s = pygame.Surface((width, height))
    s.set_alpha(15) 
    s.fill(BLACK)
    screen.blit(s, (0, 0))

    for drop in drops:
        font = fonts[drop['layer']]
        char = random.choice(chars)
        main_color = BRIGHT_GREEN if drop['layer'] > 0 else DEEP_GREEN
        
        # Draw glowing head and thick trail
        screen.blit(font.render(char, True, WHITE), (drop['x'], drop['y']))
        screen.blit(font.render(random.choice(chars), True, main_color), (drop['x'], drop['y'] - font_sizes[drop['layer']]))

        drop['y'] += drop['speed']
        if drop['y'] > height:
            drop['y'] = random.randint(-200, 0)

    pygame.display.flip()
    clock.tick(25) # Optimized to prevent ThinkPad lag

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            run = False
pygame.quit()