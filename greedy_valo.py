from calculation import dmg_calculation, make_loadout


def greedy(goal, criteria, armor_type, money):
    final_loadout = make_loadout(goal, money, criteria, armor_type)
    for i in final_loadout:
        i["Density"] = i["Value"] / i["Weight"]
    final_loadout = sorted(final_loadout, key=lambda d: d["Density"])

    j = 0
    new_load = []
    cred = money
    cred = cred - final_loadout[j]["Weight"]
    if cred >= 0:
        new_load.append(final_loadout[j])
    j += 1
    while cred > 0:
        cred = cred - final_loadout[j]["Weight"]
        if cred >= 0:
            new_load.append(final_loadout[j])
        j += 1

    return new_load
