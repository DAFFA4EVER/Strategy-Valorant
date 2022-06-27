from calculation import dmg_calculation, make_loadout


def greedy(goal, criteria, armor_type, money):
    final_loadout = make_loadout(goal, money, criteria, armor_type)
    print(final_loadout)
    new_load = []
    if len(final_loadout) != 0:
        for i in final_loadout:
            i["Weight"] += 1
            i["Density"] = i["Value"] / i["Weight"]
        final_loadout = sorted(
            final_loadout, key=lambda d: d["Density"], reverse=True)
        print(len(final_loadout))

        j = 0
        cred = money
        if cred - final_loadout[j]["Weight"] >= 0:
            new_load.append(final_loadout[j])
            cred = cred - final_loadout[j]["Weight"]
        j += 1
        while cred >= 0 and j < len(final_loadout):
            if cred - final_loadout[j]["Weight"] >= 0:
                new_load.append(final_loadout[j])
                cred = cred - final_loadout[j]["Weight"]
            j += 1

    return new_load
