#!/usr/bin/env python3
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):
    
    def validation(game):
        player = 0
        if len(game) <= 0:
            raise Warning("Invalid world size: x-dim")
        for line in game:
            if len(line) <= 0:
                raise Warning("Invalid world size: y-dim")
            elif len(line) != len(game[0]):
                raise Warning("not same lenght")
            for char in line:
                if not char == " " and not char == "#" and not char == "o":
                    raise Warning("Invalid characters")
                elif char == "o":
                    player += 1
                    y = game.index(line)
                    x = line.index(char)
                    player_position = y,x
        if player != 1:
            raise Warning("Not one player in world")
        return player_position

    def move_right(vert, horiz, world):
        new_right = list(world)
        if new_right[vert][horiz] == new_right[vert][-1]:
            raise Warning("Invalid move")
        elif new_right[vert][horiz + 1] == "#":
            raise Warning("Invalid move")
        else:
            new_right[vert] = new_right[vert][:horiz] + " " + "o" + new_right[vert][horiz + 2:]
        return tuple(new_right)       
            
    def move_left(line, char, world):
        new_left = list(world)
        if new_left[line][char] == new_left[line][0]:
            raise Warning("Invalid move")
        elif new_left[line][char -1] == "#":
            raise Warning("Invalid move")
        else:
            new_left[line] = new_left[line][:char -1] + "o" + " " + new_left[line][char + 1:]
        return tuple(new_left)
    
    def move_up(line, char, world):
        new_up = list(world)
        if new_up[line][char] == new_up[0][char]:
            raise Warning("Invalid move")
        elif new_up[line -1 ][char] == "#":
            raise Warning("Invalid move")
        else:
            new_up[line -1] = new_up[line -1][:char] + "o" + new_up[line -1][char + 1:]
            new_up[line] = new_up[line][:char] + " " + new_up[line][char + 1:]
        return tuple(new_up)

    def move_down(line, char, world):
        new_down = list(world)
        if new_down[line][char] == new_down[-1][char]:
            raise Warning("Invalid move")
        elif new_down[line + 1][char] == "#":
            raise Warning("Invalid move")
        else:
            new_down[line + 1] = new_down[line + 1][:char] + "o" + new_down[line + 1][char + 1:]
            new_down[line] = new_down[line][:char] + " " + new_down[line][char + 1:]
        return tuple(new_down)
    
    y,x = validation(state)
    
    if direction == "right":
        new_state = move_right(y,x, state)
    
    elif direction == "left":
        new_state = move_left(y,x, state)
    
    elif direction == "up":
        new_state = move_up(y,x, state)

    elif direction == "down":
        new_state = move_down(y,x, state)

    else:
        raise Warning("provided move is invalid")
    
    def possible_directions():
        directions = []
        new_y, new_x = validation(new_state)
        try:
            move_right(new_y,new_x,new_state)
        except:
            pass
        else:
            directions.append("right")
        
        try:
            move_left(new_y,new_x,new_state)
        except:
            pass
        else:
            directions.append("left")
        try:
            move_down(new_y,new_x,new_state)
        except:
            pass
        else:
            directions.append("down")
        try:
            move_up(new_y,new_x, new_state)
        except:
            pass
        else:
            directions.append("up")
        
        if len(directions) >= 1:
            return sorted(directions)
        else:
            raise Warning("No more moves possible")
    

    return (new_state,tuple(possible_directions()))


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    " o#    #",
    "#     ##",
    "   #####"
)
s2 = move(s1, "left")

print("= New State =")
print("\n".join(s2[0]))
print(f"\nPossible Moves: {s2[1]}")