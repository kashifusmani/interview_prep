#Given a target amount n and a list (Array) of distinct coin values, what's the fewest coins needed to make the change amount?

#rec_coin(10, [1,5]) = 2 (2 coins of 5)

#assuming coins is sorted in increasing order
def rec_coin(target, coins, coins_comb=0):
    if target <= 0:
      return coins_comb
    if target >= coins[len(coins) - 1]:
        coin_val = coins[len(coins) - 1]
        return rec_coin(target - coin_val, coins, coins_comb = coins_comb + 1)
    else:
        return rec_coin(target, coins[:len(coins) - 1], coins_comb = coins_comb)

#find how many combinations of coins can be used
def rec_coin_combs(target, coins):
    result = []
    for i in range(len(coins)):
        result.append(rec_coin(target, coins[:len(coins)-i]))
    return result

#No that different from above, in fact tail recursion version is much faster
def rec_coin_dynamic(target, coins, known_results):
    min_coins = target
    if target in coins:
        known_results[target] = 1
        return 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c < target]:
            num_coins = 1 + rec_coin_dynamic(target - i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
    return min_coins

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def count(S, m, n ):

    # If n is 0 then there is 1
    # solution (do not include any coin)
    if n == 0:
        return 1

    # If n is less than 0 then no
    # solution exists
    if n < 0:
        return 0

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if m <=0 and n >= 1:
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1])


if __name__ == '__main__':
    '''
    from time import time
    target = 200
    start = time()
    print(rec_coin(target, [1, 5, 10, 25]))
    end = time()
    print(end - start)


    start = time()
    print(rec_coin_dynamic(target, [1, 5, 10, 25], [0]*(target+1)))
    end = time()
    print(end - start)
    '''
    arr = [1,5,10]
    m = len(arr)
    print(count(arr, m, 20))


    #print(rec_coin_combs(50, [1, 5, 10]))