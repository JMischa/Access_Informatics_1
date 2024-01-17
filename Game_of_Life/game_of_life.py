
#!/usr/bin/env python3

def evolve(world, steps):
    
    def world_validation(world, steps):
        if not isinstance(steps, int) or steps < 1:
            raise Warning("Invalid input for steps")
        if not isinstance(world, tuple):
            raise Warning("Invalid type for game world")
        if len(world) <= 2:
            raise Warning("Invalid lenght of game world")
        for line in world:
            lenght = len(world[0])
            for column in line:
                if column not in "-|# ":
                    raise Warning("Invalid characters in game world")
            if not isinstance(line, str):
                raise Warning("Invalid type for game world")
            if len(line) <= 2:
                raise Warning("Invalid height of game world")
            if len(line) != lenght:
                raise Warning("Dimensions of game world is invalid")
        for c in world[0]:
            if c != "-":
                raise Warning("Invalid frame")
        for c in world[-1]:
            if c != "-":
                raise Warning("Invalid frame")
        
        for i in range(1, len(world) -1):
            if world[i][0] != "|" or world[i][-1] != "|":
                raise Warning("Invalid frame")
        return (world, steps)
    game_world, evolve_steps = world_validation(world, steps)


    def cell_mutation(column, line):
        pass

    # implement this function
    return (game_world, evolve_steps)  # placeholder


if __name__ == "__main__":

    field = (
        "--------------",
        "|            |",
        "|   ###      |",
        "|   #        |",
        "|    #       |",
        "|            |",
        "--------------"
    )
    steps = 3

    result, alive_cells = evolve(field, steps)

    print(f"Game of Life after {steps} moves:")
    for row in result:
        print(row)
    print(f"{alive_cells} are alive.")