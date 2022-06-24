def dmg_calculation(weapon_info, criteria):
    w = weapon_info
    c = criteria[0]
    flag = True
    n = 0
    while(flag):
        i = w['Damage'][n]
        if(c <= i[1] and c > i[0]):
            dmg_score = (i[2]*0.45) + (i[3]*0.15) + (i[4]*0.40)
            dmg_score = dmg_score + (dmg_score*(w['Penetration']/10))
            flag = False
        n += 1
    dmg_score = (dmg_score * 0.7) + (w['FRate'] * 0.3)
    return dmg_score
