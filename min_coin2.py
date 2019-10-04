#2. Given a value and a set of coins, return the optimal count of coins to achieve the value.
# Example: Can you rewrite this so that it will work when you're machine has run out of nickels?
# (and minimize the number of coins given [a reasonable amount])
def min_coin2(cents):
    try:
        cents == int(cents)
    except ValueError:
        return "Not an integer!"
    else:
        if cents < 1:
            return 0
        coins = [25, 10, 5, 1]
        q = True
        d = True
        n = False
        p = True
        supply = [q,d,n,p]
        i = 0
        num_coins = 0
        
        while cents >= 1:
            
            #This can be simplified
            '''
            if supply[i] == False:
                i += 1
            elif cents < coins[i]:
                i += 1
            '''
            if (supply[i] == False) or cents < coins[i] :
                i += 1
                
            elif (supply[i] == True) & (cents >= coins[i]):
                cents -= coins[i]
                num_coins += 1
            
        return num_coins

print (min_coin2(31))
print (min_coin2(70))
print (min_coin2('hi'))
