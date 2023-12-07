# FINAL SOLUTION
import math
from collections import Counter
import functools 

def get_hand_type(hand):
    counts = Counter(hand)
    hand_type = sorted(list(counts.values()))
    if hand_type == [5]:
        return 7
    if hand_type == [1,4]:
        if "J" in hand:
            return 7
        return 6
    if hand_type == [2, 3]:
        if "J" in hand:
            return 7
        return 5
    if hand_type == [1,1,3]:
        if counts["J"] == 1:
            return 6
        elif counts["J"] == 2:
            return 7
        elif counts["J"] == 3:
            return 6
        return 4
    if hand_type == [1, 2, 2]:
        if counts["J"] == 1:
            return 5
        elif counts["J"] == 2:    
            return 6
        return 3
    if hand_type == [1, 1, 1, 2]:
        if counts["J"] == 1:
            return 4
        elif counts["J"] == 2:    
            for i in counts:
                if counts[i]==2 and i != "J":
                    return 6
            return 4
        return 2
    if hand_type == [1, 1, 1, 1 ,1]:
        if counts["J"] == 1:
            return 2
        return 1
    print("not possible")
    return 1000

def get_char_strength(char):
    strengths = ["A", "K", "Q", "T", "9", '8', '7', '6', '5', '4', '3', '2', 'J']
    return len(strengths) - strengths.index(char)

def cmp_same_hand_strength(a, b):
    for i in range(len(a)):
        if get_char_strength(a[i]) > get_char_strength(b[i]):
            return 1
        elif get_char_strength(a[i]) < get_char_strength(b[i]):
            return -1
    return 0


f = open("input.txt", "r")

all_cards = []
bids = {}
for line in f:
    card, curr_bid = line.split(" ")
    bids[card] = int(curr_bid)
    all_cards += [card]

# sort by hands
hand_catorized = [[], [], [], [], [], [], []]
for hand in all_cards:
    hand_type = get_hand_type(hand)
    hand_catorized[hand_type - 1] += [hand]


# sort each hand by card strength 
final_sorted_cards = []
for hand_type_cards in hand_catorized:
    final_sorted_cards += (sorted(hand_type_cards, key=functools.cmp_to_key(cmp_same_hand_strength)))

total = 0
for rank, card in enumerate(final_sorted_cards):
    total += ((rank+1) * bids[card])

# print(final_sorted_cards)
print(total)



