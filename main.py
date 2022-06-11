import valorant_gun as gun
import brute_valo as brute
import greedy_valo as greedy

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
    return dmg_score

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

if __name__ == "__main__":
    print('Rules : 0/1 Sidearms, 0/1 Main Weapon (SMGs, Rifles, Snipers, Heavies), 1 Armor (At least you have a Sidearms or Main Weapon')
    print('Catalog : Sidearms, SMGs, Shotguns, Rifles, Snipers, Heavies, Armors, Anyweapon\n')
    s, m, a = 0,0,0
    goal = input("Input your loadout goal : ").split()
    error = False
    armor_type = None
    for i in goal:
        if(i == 'Sidearms'):
            s += 1
        elif(i == 'Armors'):
            a += 1
            armor_type = input('Light or Heavy armor? ')               
        elif(i == 'Anyweapon'):
            m += 1
            s += 1
        else:
            for j in gun.main:
                if(i == j):
                    m += 1
                    break
        if(s > 1 or m > 1 or a > 1):
            error = True
            print('This is Valorant, not Rambo bro')
            break
        elif(s == 0 and m == 0):
            print('You want to play Point Blank with a knife?')
            error = True
            break

    if(not error):
        final = 'There maybe some error :('
        money = int(input("Your creeds : "))
        print("Your weapon of choice range (Their max range)?",end=' ')
        criteria = list(map(int, input().split()))
        algorithm = input("Greedy/Brute? ")
        if(algorithm == 'Brute'):
            final = brute.brute_force(make_loadout(goal, money, criteria, armor_type), money)
        elif(algorithm == 'Greedy'):
            final = 'Blank'
        
        print(final)
    
    print("!!!!!!!ACE!!!!!!!")