from calculation import dmg_calculation, make_loadout


def brute_force(goal, criteria, armor_type, money):
    final_loadout = make_loadout(goal, money, criteria, armor_type)
    i = len(final_loadout) - 1
    best = {'Value': 0}
    while(i >= 0):
        if(final_loadout[i]['Weight'] <= float(money)):
            if(final_loadout[i]['Value'] >= best['Value']):
                best = final_loadout[i]
        i -= 1
    return best
