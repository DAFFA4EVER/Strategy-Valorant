import valorant_gun as gun
import brute_valo as brute
import greedy_valo as greedy
import time

if __name__ == "__main__":
    print('Rules : 0/1 Sidearms, 0/1 Main Weapon (SMGs, Rifles, Snipers, Heavies), 1 Armor (At least you have a Sidearms or Main Weapon')
    print('Catalog : Sidearms, SMGs, Shotguns, Rifles, Snipers, Heavies, Armors, Anyweapon\n')
    s, m, a = 0, 0, 0
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
        print("Your weapon of choice range (Their max range)?", end=' ')
        criteria = list(map(int, input().split()))
        algorithm = input("Greedy/Brute? ")
        start = time.time_ns()
        if(algorithm == 'Brute'):
            final = brute.brute_force(goal, criteria, armor_type, money)
            print("Brute Force time elapsed : ", end='')
        elif(algorithm == 'Greedy'):
            final = 'Blank'
            print("Greddy time elapsed : ", end='')

        end = time.time_ns()
        print(f'{end-start}ns')
        print(
            f"Weapon : {final['Name']} <> Armor : {final['Armor']} <> Price : {final['Weight']} <> Value : {final['Value']}")

    print("!!!!!!!ACE!!!!!!!")
