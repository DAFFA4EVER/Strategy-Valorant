def brute_force(final_loadout, budget):
    i = len(final_loadout) - 1
    best = {'Value':0}
    while(i >= 0):
        if(final_loadout[i]['Weight'] <= float(budget)):
            if(final_loadout[i]['Value'] >= best['Value']):
                best = final_loadout[i]
        i -= 1
    return best
