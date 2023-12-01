from reader import read_list

# print(read_list())

test_input = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]

broken = ["8flntwomkktkpvsone78sixone"] # giving 86

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

real_input = read_list()

# ===
import re

findall = lambda string, n: [m.start() for m in re.finditer(str(n), string)]

alphanums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for word in real_input:
    # num_indices = [(word.find(n), n) for n in alphanums]
    # num_indices = [d for d in num_indices if d[0] != -1]
    # num_indices = [(d[0], alphanums.index(d[1])+1) for d in num_indices]

    num_indices = []
    for d in alphanums:
        indices = findall(word, d)
        # print(f"{i} appears at indices: {indices}")
        for index in indices:
            # print(f"{d} appears at index: {index}")
            num_indices.append((index, int(alphanums.index(d)+1)))

    digits = []
    for i in integers:
        indices = findall(word, i)
        # print(f"{i} appears at indices: {indices}")
        for index in indices:
            # print(f"{i} appears at index: {index}")
            digits.append((index, i))

    # print(f"digits: {digits}")
    # digits = [(int(n), word.find(n)) for n in list(word) if n.isnumeric()]
    # digits = [d for d in digits if d[1] != -1]

    # value: index
    num_indices, digits = dict(num_indices), dict(digits)

    # index: value
    # num_indices = dict((v,k) for k,v in num_indices.items())
    # digits = dict((v,k) for k,v in digits.items())

    nums = num_indices | digits

    first_num = nums[min(nums.keys())]
    last_num = nums[max(nums.keys())]

    print(f"{first_num}{last_num} | {nums} | {word}")
    sum += int(f"{first_num}{last_num}")

print(sum)