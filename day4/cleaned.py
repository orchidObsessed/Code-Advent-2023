"""A post-completion cleaned-up version for day 4, with some explanations!"""
# ===== < PART 0 > =====
"""
Reading the problem input.
"""
with open("INPUT.txt", 'r') as fo:
    values = [x.strip() for x in fo.readlines()]

# ===== < PART 1 > =====
"""
In Python, this part of the question turned out to be super easy!

All we need to do, is split each card into our numbers vs the
winning ones, and then convert those two halves into cleaned-up
lists of integers. From there, we can iterate through our side
of each card, and compare it to the other side with an `in`
statement, tally up our score according to the prompt, and win!
"""

# Setting up a running sum
sum_1 = 0

for card in values:
    # This nasty double split also takes care of the first chunk
    # of the card, containing its number - we don't need that for
    # part 1.
    guesses, winning = card.split(": ")[1].split(" | ")

    # Now, we clean up each side to a list of ints
    guesses = [int(n) for n in guesses.split(" ") if n != ""]
    winning = [int(n) for n in winning.split(" ") if n != ""]

    # Then we loop through our guesses, checking if they win
    score = 0
    for guess in guesses:
        if guess in winning:
            # Set the current score to 1 if it's 0
            if score == 0: score = 1
            # Otherwise, double it
            else: score *= 2
    
    # Lastly, add the score to the sum
    sum_1 += score

print(sum_1)

# ===== < PART 2 > =====
"""
Aside from having a really hard time understanding the prompt, this part
wasn't too bad with the above code already completed.

The changes we'll need to make are twofold: first, we can drop the score,
as we'll just be counting cards (not the blackjack kind!). Second, we will
need the card number. For the sake of speed and code reuse, I just added
another variable to the `for` loop. We could enumerate, or we could pull
out the card number from the first bit of the string.
"""

# Set up our card counting operat- I mean, dictionary...
n_cards = {i: 1 for i in range(len(values))}

# Loop through, much the same as before, but with the iterator c
for card, c in zip(values, range(len(values))):
    # Again - we coulda used the first split to get the card number
    guesses, winning = card.split(": ")[1].split(" | ")

    # Now, we clean up each side to a list of ints
    guesses = [int(n) for n in guesses.split(" ") if n != ""]
    winning = [int(n) for n in winning.split(" ") if n != ""]

    # Not quite deja vu! We just need to keep track of the
    # total number of wins, not any doubling.
    wins = 0
    for guess in guesses:
        if guess in winning: wins += 1
    
    # Here's the magic part! We will increase the count of
    # `n` cards ahead of this one by `c`, where:
    #  `n` = the number of wins on this card
    #  `c` = the quantity of cards of this number we have
    for n in range(wins):
        n_cards[n+c+1] += 1*n_cards[c]

# No need for a running sum, we can get it at the end like this
sum_2 = sum(list(n_cards.values()))
print(sum_2)
    