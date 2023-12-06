"""A post-completion cleaned up and annotated solution of day 6!"""
# ===== < PART 0 > =====
"""
Reading the input.

Since today's input was so short, you could also
just write out the list in this file.
"""
with open("INPUT.txt", 'r') as fo:
    values = [l.strip() for l in fo.readlines()]
    
# ===== < PART 1 > =====
"""
Today's problem and solution were thankfully pretty straightforward! It all
comes down to making sure you aren't doing anything funky when creating the
velocity and distance travelled, and comparing that to the record.

First, we'll clean up the input; we don't care about the field names, and
we want them as integers.

Then, we'll loop through each pair of times and distances. For each pair,
we will find the minimum and maximum duration of holding the button, which
we can do (somewhat inefficiently) by looping through each possibility and
checking it it beats the record.

Then, we just find the number of ways to win, and update the margin of error
accordingly!
"""

# This nasty bit is just doing the cleaning step. Since it can be
# gross to follow, what's happening (in order) is:
# 1. Split the whole thing by a colon, and discard the first element
# 2. Strip the resulting string of leading and trailing whitespace / invis
# 3. Split the resulting string by whitespaces
# 4. Discard any empty entries in the resulting list
# 5. Cast the reamining list entries to strings
times, distances = values[0], values[1]
times = [int(t) for t in times.split(":")[1].strip().split(" ") if t != ""]
distances = [int(t) for t in distances.split(":")[1].strip().split(" ") if t != ""]

# Create running margin of error
margin_of_error = 1 # set to 1 since we'll use *= for updating it

# Begin looping through each race
for time, distance in zip(times, distances):
    count = 0 # Number of ways we can win
    
    # Loop through each second of the race
    for t in range(time):
        # Get our projected distance if we hold the button for t seconds
        # t is our velocity, and (time-t) is our time spent moving
        d = t * (time-t)
        
        # If we will beat the record, update the count!
        if d > distance: count += 1
    
    # Finally, update the margin of error with our count
    margin_of_error *= count
    
print(f"Part 1: {margin_of_error}")

# ===== < PART 2 > =====
"""
This only requires two small changes over part 1!

The first is how we clean up our input. We'll need to combine the little integers
into one big one via concatenation, which is straightforward.

The second is that we can drop our outermost loop, since there will is now only
one race!
"""

# We will start largely the same as before, but we DO NOT cast to integer.
times, distances = values[0], values[1]
times = [t for t in times.split(":")[1].strip().split(" ") if t != ""]
distances = [t for t in distances.split(":")[1].strip().split(" ") if t != ""]

# Here, we will cast only after joining the strings together:
time = int("".join(times))
distance = int("".join(distances))

# Create our running count, but notably NOT a running MoE!
count = 0 # Number of ways we can win

# Loop through each second of the singular race
for t in range(time):
    # Get our projected distance, same as before
    d = t * (time-t)
    
    # If we will beat the record, update the count
    if d > distance: count += 1
    
print(f"Part 2: {count}")

# ===== < POSTSCRIPT > =====
"""
As can be seen by running this, this is not the most efficient way to
solve this puzzle. Part 2 runs in O(n), and part 1 runs in ~O(n^2)!
There is thankfully a much more elegant solution that can make these
much more algorithmically efficient. This "better way" can be summed
up as finding the solution to a system of equations.

Let's imagine a weird graph: a velocity (button hold duration) over
distance traveled graph. Under this graph, the race's record would
be a horizontal line. The line that we're considering would be an
inverted parabola, that intersects that line. We want to find the
solution to that system of equations, ie. the points of intersection.

This can be done easily enough in pure Python, and even easier with
libraries like NumPy, and our solutions can even be visualized through
things like MatPlotLib! If I have the time and remember to do it, I'll
come back and show off a NumPy solution, and a vizualization with MPL.
"""