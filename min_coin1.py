#1. Given a value, return the optimal number of coins [1,5,10,25] to make the value.
#1. Inital code:

def min_coin1(cents):
    if cents < 1:
        return 0
        
    coins = [25,10,5,1]
    i = 0
    num_coins = 0
    
    while cents >= 1:
        if cents < coins[i]:
                i = i + 1
        elif cents >= coins[i]:
            cents = cents - coins[i]
            num_coins = num_coins + 1
    return num_coins

print (min_coin1(10))
print (min_coin1(31))
