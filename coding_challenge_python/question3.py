def minimize_coins(amount):
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]  
    result = []  

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    print("Coins used:")
    print(result)
    print("Total coins:", len(result))


amount = int(input("Enter the amount: "))
minimize_coins(amount)
