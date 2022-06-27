from calculation import dmg_calculation, make_loadout
import numpy as np

def brute_force(goal, criteria, armor_type, money):
    loadout = []
    final = []
    val = []
    wt = []
    n = 1
    for i in goal:
        load = [i]
        if(armor_type != None):
            load.append('Armors')
        if(i != 'Armors'):
            for j in (make_loadout(load, money, criteria, armor_type)):
                loadout.append(j)
                val.append(j['Value'])
                wt.append(j['Weight'])
    
    W = money
    n = len(val)
    for v in subsetSum(n, val, knapSack(W, wt, val, n)):
        for p in loadout:
            if(p['Value'] == v):
                final.append(p)
    return (final)
    
  
def subsetSum(n, arr, x):
    from itertools import combinations    
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    for i in range(n+1):
        for subset in combinations(arr, i):
            # printing the subset if its sum is x:
            if sum(subset) == x:
                return (list(subset))

def knapSack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
 