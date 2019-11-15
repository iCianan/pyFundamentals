# Question: You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# Input [1,2,5] 11
# Output 3 (2x5s 1x1)

def fewestCoinChange(coins, amount):
    numsOfCoins = [float("inf") for total in range(amount+1)]
    numsOfCoins[0] = 0
    for coin in coins:
        for total in range(len(numsOfCoins)):
            if coin <= total:
                numsOfCoins[total] = min(
                    numsOfCoins[total], numsOfCoins[total - coin] + 1
                )
    return numsOfCoins[amount] if numsOfCoins[amount] != float('inf') else -1



def main():
    coins = [1,2,5]
    amount = 11
    print(fewestCoinChange(coins,amount))

if __name__ == "__main__":
    main()