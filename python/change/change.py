from itertools import combinations_with_replacement
def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    max_coins = target // min(coins) + 1
    min_coins = target // max(coins)

    for i in range(min_coins, max_coins):
        for j in combinations_with_replacement(coins, i):
            if sum(j) == target:
                return list(j)
    raise ValueError("can't make target with given coins")
