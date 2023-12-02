"""A post-completion cleaned-up version for day 2, with some explanations!"""
# ===== < PART 0 > =====
"""
Reading the problem input.
"""
with open("INPUT.txt", 'r') as fo:
    values = [x.strip() for x in fo.readlines()]

# ===== < PART 1 > =====
"""
For whatever reason, I struggled with this a bit! I think it was largely due
to nerves, and I didn't fully read the question, so I missed the part where
the cubes go back into the bag. Once I caught that, though, it was pretty easy.

All we need to do is reduce each game down to the individual draws made; the
semicolon / comma separation seems like a red herring. If any single draw is
made that is over the 'budget', the whole game is invalidated. 

So, we first loop through each game, then each 'round' within each game,
then each 'draw' within each round! If at any point a draw is made that is
over the maximum cube limit for that color, we flag it. If we get through an
entire game without raising the flag, it must be valid, and we add it to the total.
"""

# Setting up max values and a running sum
max_red, max_green, max_blue = 12, 13, 14
sum_1 = 0

for game, i in zip(
    [l.split(": ")[1] for l in values],  # Leave out the leading "Game n: "
    range(len(values))                   # Also keep an iterator going
):
    
    overdraw = False                     # This is the flag mentioned above!

    for round in game.split("; "):       # Each round is delimeted by a colon followed by a space
        for draw in round.split(", "):   # Each draw is delimited by a comma followed by a space
            n, colour = draw.split(" ")  # This gives us the number drawn and the colour
            n = int(n)

            # A quick conditional chunk here to check if we overdrew on each colour
            # if only python had switch cases...
            if colour == "red" and n > max_red: overdraw = True
            if colour == "green" and n > max_green: overdraw = True
            if colour == "blue" and n > max_blue: overdraw = True
    
    # At the end of the game, if we haven't overdrawn, we're good to add the game to the sum!
    if not overdraw:
        sum_1 += (i+1)

print(f"Part 1: {sum_1}")

# ===== < PART 2 > =====
"""
This part was actually slightly easier than part 1, in my opinion!

Instead of checking if we've overdrawn, we now simply just need to keep track
of the largest seen value for each colour. We will again do the triply-nested
loop of game <- round <- draw, but will just keep track of the maximum values
for each, then multiply them together to get the power and sum them up!
"""

# Setting up sum
sum_2 = 0

for game in [l.split(": ")[1] for l in values]:      # Again, drop the "Game n: "; we don't even need the ID this time!
    
    count = {"red": 0, "green": 0, "blue": 0}        # We'll use this to keep track of the values we've seen

    for round in game.split("; "):                   # Split on semicolon to get rounds within the game,
        for draw in round.split(", "):               # and split on comma to get each draw,
            n, colour = draw.split(" ")              # and, finally, split on space to get the important bits.

            if int(n) > count[colour]:               # Update the value if we have a new maximum for that colour
                count[colour] = int(n)

    # Update the sum with the power
    sum_2 += (count["red"]*count["green"]*count["blue"])

print(f"Part 2: {sum_2}")
