f = open("input.txt", "r")

length = 203 + 1
cards_wins_count = [0] * length
card_wins = [0] * length

total = 0
for line_no, line in enumerate(f):
    card_no = line_no + 1
    wins, games = line.split(":")[1].split("|")
    score = 0
    wins = set(wins.strip().split(" "))
    games = set(games.strip().split(" "))
    wins_count = 0
    for i in wins:
        if i in games and i.isnumeric():
            wins_count += 1
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score
    card_wins[card_no] = wins_count
    cards_wins_count[card_no] += 1
    for i in range(wins_count):
        if card_no + i + 1 < length:
            cards_wins_count[card_no + i + 1] += cards_wins_count[card_no]
        else: print(card_no, i, wins_count, card_no)

print(total)
# print((card_wins))
# print((cards_wins_count))
print(sum(cards_wins_count))

