import random

width = int(input("Enter width: "))
height = int(input("Enter height: "))

x = random.randint(0, width - 1)
y = random.randint(0, height - 1)

carrot_count = int(input("Enter the number of carrots: "))
hole_count = int(input("Enter the number of holes: "))

grid = [['- ' for _ in range(width)] for _ in range(height)]

rabbit_has_jumped = False
carrot_collected = False
carrot_dropped = False

if carrot_collected:
    grid[y][x] = 'R '
else:
    grid[y][x] = 'r '
    
carrots_placed = 0
while carrots_placed < carrot_count:
    carrot_x = random.randint(0, width - 1)
    carrot_y = random.randint(0, height - 1)

    if grid[carrot_y][carrot_x] == '- ':
        neighbor_cells = [
            grid[carrot_y][carrot_x - 1] if carrot_x > 0 else '',
            grid[carrot_y][carrot_x + 1] if carrot_x < width - 1 else '',
            grid[carrot_y - 1][carrot_x] if carrot_y > 0 else '',
            grid[carrot_y + 1][carrot_x] if carrot_y < height - 1 else '',
        ]

        if 'c ' not in neighbor_cells and 'O ' not in neighbor_cells:
            grid[carrot_y][carrot_x] = 'c '
            carrots_placed += 1

holes_placed = 0
while holes_placed < hole_count:
    hole_x = random.randint(0, width - 1)
    hole_y = random.randint(0, height - 1)

    if grid[hole_y][hole_x] == '- ':
        neighbor_cells = [
            grid[hole_y][hole_x - 1] if hole_x > 0 else '',
            grid[hole_y][hole_x + 1] if hole_x < width - 1 else '',
            grid[hole_y - 1][hole_x] if hole_y > 0 else '',
            grid[hole_y + 1][hole_x] if hole_y < height - 1 else '',
        ]

        if 'c ' not in neighbor_cells and 'O ' not in neighbor_cells:
            grid[hole_y][hole_x] = 'O '
            holes_placed += 1

def print_grid():
    for row in grid:
        print(''.join(row))
        
def is_valid_move(new_x, new_y):
    return 0 <= new_x < width and 0 <= new_y < height
def instruction():
    print("Instructions:")
    print("  - Move the rabbit 'r' using 'a' (left), 'd' (right), 'w' (up), 's' (down).")
    print("  - Collect carrots 'c' using 'p'.")
    print("  - Jump over holes 'O' using 'j' and specify the jump direction.")
    print("  - Type 'h' for help.")
    print("  - Type 'q' to quit the game.")
    
print("Welcome to Rabbit's Adventure Game!")
instruction()
print_grid()


while carrot_count > 0:
    move = input("Enter a move (a: left, d: right, w: up, s: down, or q: quit the game, h: help): ").lower()
    
    if move == 'q':
        print("Let's try again!")
        break
    elif move == 'h':
        instruction()
        input("Press Enter to continue...")
        print_grid()
    
    else:
        new_x, new_y = x, y

        if move == 'a':
            new_x -= 1
        elif move == 'd':
            new_x += 1
        elif move == 'w':
            new_y -= 1
        elif move == 's':
            new_y += 1
        elif move == 'j':
            if rabbit_has_jumped:
                print("Rabbit cannot jump again in the same turn.")
                rabbit_has_jumped = False
                continue
            
            if grid[y][x] != 'r ':
                print("Rabbit is near a hole. Use 'p' to drop the carrot.")
                continue
            
            else:
                direction = input("Enter jump direction (a:left, d:right, w:up, s:down): ").lower()
                jump_x, jump_y = x, y
                
                if direction == 'a' and x > 1 and grid[y][x - 1] == 'O ':
                    jump_x -= 2
                elif direction == 'd' and x < width - 2 and grid[y][x + 1] == 'O ':
                    jump_x += 2
                elif direction == 'w' and y > 1 and grid[y - 1][x] == 'O ':
                    jump_y -= 2
                elif direction == 's' and y < height - 2 and grid[y + 1][x] == 'O ':
                    jump_y += 2
                else:
                    print("Invalid jump direction or no hole to jump over or it's the edge.")
                    continue
                
            rabbit_has_jumped = True
            grid[y][x] = '- '
            x, y = jump_x, jump_y
            grid[y][x] = 'r '
            carrot_dropped = False

        elif move == 'p':
            if carrot_collected:
                if move == 'p':
                    drop_x, drop_y = x, y
                    
                    if x > 0 and grid[y][x - 1] == 'O ':
                        drop_x -= 1
                        print("Carrot Dropped!!")
                        carrot_dropped = True
                        carrot_collected = False
                        carrot_count -= 1
                    elif x < width - 1 and grid[y][x + 1] == 'O ':
                        drop_x += 1
                        print("Carrot Dropped!!")
                        carrot_dropped = True
                        carrot_collected = False
                        carrot_count -= 1
                    elif y > 0 and grid[y - 1][x] == 'O ':
                        drop_y -= 1  
                        print("Carrot Dropped!!")
                        carrot_dropped = True
                        carrot_collected = False
                        carrot_count -= 1
                    elif y < height - 1 and grid[y + 1][x] == 'O ':
                        drop_y += 1
                        print("Carrot Dropped!!")
                        carrot_dropped = True
                        carrot_collected = False
                        carrot_count -= 1
                    else:
                        print("No carrot to drop.")
                        continue
                else:
                    print("Carrot already collected.")
            else:
                collect_x, collect_y = x, y
                
                if x > 0 and grid[y][x - 1] == 'c ':
                    collect_x -= 1
                    print("Carrot Collected!!")
                    carrot_collected = True
                elif x < width - 1 and grid[y][x + 1] == 'c ':
                    collect_x += 1
                    print("Carrot Collected!!")
                    carrot_collected = True
                elif y > 0 and grid[y - 1][x] == 'c ':
                    collect_y -= 1  
                    print("Carrot Collected!!")
                    carrot_collected = True
                elif y < height - 1 and grid[y + 1][x] == 'c ':
                    collect_y += 1
                    print("Carrot Collected!!")
                    carrot_collected = True
                else:
                    print("No carrot to pick.")
                    continue
                
                
            
            if carrot_collected:
                grid[y][x] = '- '
                x, y = collect_x, collect_y
                grid[y][x] = 'R '
            if carrot_dropped:
                grid[y][x] = 'r '
                
        
        elif move in ('w', 's', 'a', 'd'):
            if grid[y][x] == 'r ':
                if move == 'w':
                    if y > 0 and grid[y - 1][x] not in ('c ', 'O '):
                        grid[y][x] = '- '
                        y -= 1
                        grid[y][x] = 'r '
                    else:
                        print("Invalid move. Cannot move through carrots or other holes.")
                elif move == 's':
                    if y < height - 1 and grid[y + 1][x] not in ('c ', 'O '):
                        grid[y][x] = '- '
                        y += 1
                        grid[y][x] = 'r '
                    else:
                        print("Invalid move. Cannot move through carrots or other holes.")
                elif move == 'a':
                    if x > 0 and grid[y][x - 1] not in ('c ', 'O '):
                        grid[y][x] = '- '
                        x -= 1
                        grid[y][x] = 'r '
                    else:
                        print("Invalid move. Cannot move through carrots or other holes.")
                elif move == 'd':
                    if x < width - 1 and grid[y][x + 1] not in ('c ', 'O '):
                        grid[y][x] = '- '
                        x += 1
                        grid[y][x] = 'r '
                    else:
                        print("Invalid move. Cannot move through carrots or other holes.")
            else:
                print("Rabbit is near a hole. Use 'p' to drop the carrot.")
                
            
        if is_valid_move(new_x, new_y):
            if grid[new_y][new_x] == 'c ':
                if carrot_collected:
                    continue
            
            elif carrot_collected:
                if grid[new_y][new_x] == 'O ':
                    continue
                else:
                    grid[y][x] = '- '
                    x, y = new_x, new_y
                    grid[y][x] = 'R '
                
            elif carrot_dropped:
                if grid[new_y][new_x] == 'O ':
                    continue
                else:
                    grid[y][x] = '- '
                    x, y = new_x, new_y
                    grid[y][x] = 'r '
                
            elif rabbit_has_jumped == False and carrot_collected == False and carrot_dropped == False:
                if grid[new_y][new_x] == 'O ':
                    continue
                else:
                    grid[y][x] = '- '
                    x, y = new_x, new_y
                    grid[y][x] = 'r '
                    
            elif grid[new_y][new_x] == 'O ':
                if rabbit_has_jumped:
                    rabbit_has_jumped = False
                elif carrot_dropped:
                    grid[y][x] = 'r '
                    
                else:
                    print("Unable to jump, there is a hole!!")
            else:
                print("Invalid move. Cannot move through carrots or other holes. Or got stuck kindly press that button which will direct rabbit.")

        print_grid()
    
if carrot_count == 0:
    print("You won the game!")
    print_grid()

print("Game Over!")
