

def coinChange(coins, target):
    ways = [0] * (target + 1)
    ways[0] = 1
    for coin in coins:
        for amount in range(1, len(ways)):
            if coin <= amount:
                ways[amount] += ways[amount-coin]            
    return ways[target]

def main():
    print(coinChange([1,5,10,25], 25))

if __name__ == "__main__":
    main()
    
