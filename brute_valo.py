from main import dmg_calculation
import valorant_gun as gun

def make_loadout(goal_loadout, budget, criteria, armor):
    temp_loadout = []
    armor_load = 'None'
    armor_name = 'None'
    for i in goal_loadout:
        if(i == 'Anyweapon'):
            for j in gun.shop[i]:
                for k in j:
                    if(k['Price'] <= budget):
                        dmg_score = dmg_calculation(k, criteria)
                        temp_loadout.append({'Name' : k['Name'], 'Weight': k['Price'], 'Value': dmg_score, 'Type': i})
        elif(i == 'Armors'):
            if(armor == 'Light'):
                armor_load = {'Name' : gun.Armors[0]['Name'], 'Weight': gun.Armors[0]['Price'], 'Value': 1, 'Type': i}
            elif(armor == 'Heavy'):
                armor_load = {'Name' : gun.Armors[1]['Name'], 'Weight': gun.Armors[1]['Price'], 'Value': 2, 'Type': i}
        else:
            for j in gun.shop[i]:
                if(j['Price'] <= budget):
                    dmg_score = dmg_calculation(j, criteria)
                    temp_loadout.append({'Name' : j['Name'], 'Weight': j['Price'], 'Value': dmg_score, 'Type': i})
    
    final_loadout = []
    for g in temp_loadout:
        weight = 0
        value = 0
        if(armor_load != 'None'):
            weight = armor_load['Weight']
            value = armor_load['Value']
            armor_name = armor_load['Name']

        weight = weight + g['Weight']
        value = value + g['Value']
        final_loadout.append({'Name':g['Name'],'Armor': armor_name,'Weight': weight,'Value': value})
    return final_loadout

def brute_force(final_loadout, budget):
    i = len(final_loadout) - 1
    best = {'Value':0}
    while(i >= 0):
        if(final_loadout[i]['Weight'] <= float(budget)):
            if(final_loadout[i]['Value'] >= best['Value']):
                best = final_loadout[i]
        i -= 1
    return best
