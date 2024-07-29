from collections import Counter

'''

Coding challenge, basically had to even out a series of account balances.
Some balances were negative and some positive and had to generate a list of transfers that would make the balances equal to 100.

'''
class Solution2:

    def minTransfers(self, transactions) -> int:
        balance = Counter()
        # Calculates the net balance amt each person should receive or give
        for from_, to, amt in transactions:
            balance[to] += amt
            balance[from_] -= amt
        balance = list(balance.values())
        return self.backtrack_tran(balance, 0)


    # - Any unsettled balances between n people can be resolved in at most n-1 transactions.
    # - The number of transations possible between n people is ~ n^2.
    # - So we try out all the possible ways to pick at most n-1 transations from the n^2 available
    # - Note that this sounds like the total possibilities are ~ O(n^2 CHOOSE n)
    #   but as noted below, once we pick a transaction, we remove all other transactions that
    #   include the originating node of the transaction since we don't want to any loops (Creating a loop with n-1 transations will lead to unsettled debts).
    # - Essentially this means that the first level of recursion has n - 1 choices, second level has n - 2 and so on

    # - Each transaction we pick settles the balance of at most 2 people
    # - We prune the search by not picking transactions that don't settle the balance of anyone
    #   eg transation between someone who is settled and and an unsettled person
    # - Another way to prune is not to settle between person of same sign since at best it will not improve
    #   on optimal solution and at worst will be sub optimal

    def backtrack_tran(self, arr, index):
        # At each level we settle the debt of person at index
        # If it is already settled, pick next non settled person
        if index == len(arr):
            return 0
        if not arr[index]:
            return self.backtrack_tran(arr, index + 1)

        from math import inf
        min_txns = inf
        # Try all possible transactions originating at index and ending between index...len(arr)
        for j in range(index + 1, len(arr)):
            # Pruning. arr[j] must be non zero and of different sign
            if (arr[j] * arr[index]) < 0:
                arr[j] += arr[index]
                print(arr)
                min_txns = min(1 + self.backtrack_tran(arr, index + 1), min_txns)
                print(arr)
                arr[j] -= arr[index]
        return min_txns

import itertools, collections
from functools import lru_cache
def minTransfers(transactions) -> int:

    tuplify = lambda balance: tuple(sorted((k, v) for k, v in balance.items()))

    def dfs(balances):
        if not balances:
            return 0
        import math
        res = math.inf
        balances = {k: v for k, v in balances}
        for size in range(2, len(balances) + 1):
            for group in itertools.combinations(balances.keys(), size):
                if sum(balances[k] for k in group) == 0:
                    remaining_balances = {k: v for k, v in balances.items() if k not in group}
                    res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
        return res

    balances = collections.defaultdict(int)
    for u, v, z in transactions:
        balances[u] += z
        balances[v] -= z
    return dfs(tuplify({k: v for k, v in balances.items() if v}))


if __name__ == '__main__':
    print(minTransfers([[0,2,4],[1,2,4],[3,4,5]]))