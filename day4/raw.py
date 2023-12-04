from reader import read_list

real_input = read_list()

sample = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53","Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19","Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1","Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83","Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36","Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

# ===

# ncards = 0
cards = {i: 1 for i in range(len(real_input))}

for card, c in zip(real_input, range(len(real_input))):
    x, y = card.split(": ")[1].split(" | ")
    x = [int(_) for _ in x.split(" ") if _ != ""]
    y = [int(_) for _ in y.split(" ") if _ != ""]

    n_wins = 0
    for i in x:
        if i in y:
            n_wins += 1
    
    print(f"{n_wins} wins for card(s) {c+1}")
    for n in range(n_wins):
        print(f"Card {c} earns an instance of card {n}")
        cards[c+n+1] += 1*cards[c]

for k, v in cards.items(): print(f"{k+1}: {v}")
print(sum(list(cards.values())))