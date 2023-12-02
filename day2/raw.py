from reader import read_list

real_input = read_list()

sample = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green","Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

# ===

r, g, b = 12, 13, 14

sum = 0

for game, i in zip([x.split(": ")[1] for x in real_input], range(len(real_input))):
    max_r, max_g, max_b = 0, 0, 0

    for draw in game.split("; "):

        for set in draw.split(", "):
            n, c = set.split(" ")
            n = int(n)

            if c == "red" and n > max_r: max_r = n
            if c == "green" and n > max_g: max_g = n
            if c == "blue" and n > max_b: max_b = n
    
    # print(f"r: {max_r} | g: {max_g} | b: {max_b}")
    # print(f"power: {max_r*max_g*max_b}")
    sum += (max_r*max_g*max_b)

print(sum)