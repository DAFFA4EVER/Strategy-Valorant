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
        for j in loadout:
            if(j['Value'] == v):
                final.append(j)
    return (final)
    
  
def subsetSum(n, arr, x):
    from itertools import combinations    
    for i in range(n+1):
        for subset in combinations(arr, i):
            if sum(subset) == x:
                return (list(subset))

def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
 
