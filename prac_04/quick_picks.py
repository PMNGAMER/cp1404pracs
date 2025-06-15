import random

MINI_NUM = 1
MAX_NUM = 45
NUM_PER_PICKS = 6

quick_pick_count = int(input("How many quick picks?: "))
for i in range(quick_pick_count):
    quick_picks = []
    while len(quick_picks) < NUM_PER_PICKS:
        number = random.randint(MINI_NUM, MAX_NUM)
        if number not in quick_picks:
            quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))