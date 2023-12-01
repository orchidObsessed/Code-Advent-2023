"""A post-completion cleaned-up version, with some explanations!"""
# ===== < PART 0 > =====
"""
Reading the problem input.
"""
with open("INPUT.txt", 'r') as fo:
    values = [x.strip() for x in fo.readlines()]

# ===== < PART 1 > =====
"""
This one was relatively straightforward.

All we need to do, is get every numeric character in a line,
then reduce that to the first and last element, concatenate them
as strings, then cast the resulting string to an int and sum up
those values!

Python makes this easy with two builtin features:
 * `str.isnumeric()` for finding numeric characters (the equivalent regex pattern would be \d or [0-9])
 * Negative array indexing, for finding the first and last values in the array
"""

# Setting up a running sum
sum_1 = 0

# Loop through each line in the input
for line in values:
    # Extract just the digits (regex equivalent is r'\d') from each into a list
    nums = [n for n in list(line) if n.isnumeric()]
    
    # Fetch the first and last, concatenate as a string, then cast to int and add to sum!
    sum_1 += int(f"{nums[0]}{nums[-1]}")

print(sum_1)

# ===== < PART 2 > =====
"""
The above code did not translate very cleanly into my implementation of part 2, unfortunately.

The first new thing we need is a list of spelled-out digits, which we will use to find occurences
of them in each line.

While this is entirely possible to do without regexes (by using `str.find()` with the optional
`start` parameter to limit the search space), I chose to fall back to regex, and implement a
`findall` anonymous function to fetch the indexes of all occurrences of a substring within a string.

Using these two new features, we can find the indices -- if any -- for each digit, then place that
into a dictionary where the keys are the indices and the values are the... well, values of the digit
at that index! We can use the builtin `min`/`max` and `keys` function to to find what we need,
then repeat the string concatenation and summation steps from before.
"""

# Setting up running sum and list of spellings of numbers
sum_2 = 0
alphanums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Anonymous function for finding all occurences of a substring in a string using regex
from re import finditer
findall = lambda string, n: [m.start() for m in finditer(str(n), string)]

# Loop through each line in input
for line in values:
    # Find alphanumeric values for this line
    alphanum_dict = []
    for a in alphanums:
        indices = findall(line, a)

        for index in indices:
            # A bit of weirdness going on here; this is just looking up
            # the value of the spelling of the word. Basically, we're
            # converting 'one' to 1, 'eight' to 8, etc.
            alphanum_dict.append((index, int(alphanums.index(a)+1)))

    # Find digits for this line - largely the same as above, just
    # without the trickery of looking up values for words!
    digits_dict = []
    for i in range(1, 10):
        indices = findall(line, i)

        for index in indices:
            digits_dict.append((index, i))

    # Convert to dict and join the two - this is why we appended
    # (index, value) tuples to the list!
    nums = dict(alphanum_dict) | dict(digits_dict)

    # Fetch first and last
    first_num = nums[min(nums.keys())]
    last_num = nums[max(nums.keys())]

    # Concatenate and add to sum
    sum_2 += int(f"{first_num}{last_num}")

print(sum_2)