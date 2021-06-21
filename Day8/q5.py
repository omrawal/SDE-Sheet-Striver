# Find Min Coins Greedy
# https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/


def coinChange(self, coins, amount) -> int:
    target = amount
    coin_count = 0
    n = len(coins)
    for i in range(n-1, -1, -1):
        while(target > coins[i]):
            target -= coins[i]
            coin_count += 1
        if(target == 0):
            break
    return coin_count
