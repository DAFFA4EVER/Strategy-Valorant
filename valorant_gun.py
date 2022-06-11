# Damage : [Range from, Range to, body, head, leg]
Sidearms = [
    {'Name': 'Classic', 'Price': 0, 'Penetration': 1, 'Damage': [[0, 30, 26, 78, 22], [30, 50, 22, 66, 18]], 'Mag': 12, 'Fire': 'SemiAuto', 'Type' : 'Sidearms'},
    {'Name': 'Shorty', 'Price': 200, 'Penetration': 1, 'Damage': [[0, 9, 12, 36, 10], [9, 15, 22, 66, 18], [15, 50, 3, 9, 2]], 'Mag': 2, 'Fire': 'SemiAutoSG', 'Type' : 'Sidearms'},
    {'Name': 'Frenzy', 'Price': 400, 'Penetration': 1, 'Damage': [[0, 20, 26, 78, 22], [20, 50, 21, 63, 17]], 'Mag': 13, 'Fire': 'Auto', 'Type' : 'Sidearms'},
    {'Name': 'Ghost', 'Price': 500, 'Penetration': 2, 'Damage': [[0, 30, 30, 105, 25], [30, 50, 25, 87, 21]], 'Mag': 15, 'Fire': 'SemiAuto', 'Type' : 'Sidearms'},
    {'Name': 'Sheriff', 'Price': 800, 'Penetration': 3, 'Damage': [[0, 30, 55, 159, 46], [30, 50, 50, 145, 42]], 'Mag': 6, 'Fire': 'SemiAuto', 'Type' : 'Sidearms'}
]
SMGs = [
    {'Name': 'Stinger', 'Price': 1000, 'Penetration': 1, 'Damage': [[0, 20, 27, 67, 23], [20, 50, 25, 62, 21]], 'Mag': 20, 'Fire': 'Auto', 'Type' : 'SMGs'},
    {'Name': 'Spectre', 'Price': 1600, 'Penetration': 2, 'Damage': [[0, 20, 26, 78, 22], [20, 50, 22, 66, 18]], 'Mag': 12, 'Fire': 'SemiAuto', 'Type' : 'SMGs'}
]

Shotguns = [
    {'Name': 'Bucky', 'Price': 900, 'Penetration': 1, 'Damage': [[0, 8, 22, 44, 19], [8, 12, 17, 34, 14], [12, 50, 9, 18, 8]], 'Mag': 5, 'Fire': 'SemiAutoSG', 'Type' : 'Shotguns'}, # for 1 pellet, total is 15
    {'Name': 'Spectre', 'Price': 1600, 'Penetration': 2, 'Damage': [[0, 10, 17, 34, 14], [10, 15, 13, 26, 11], [15, 50, 10, 20, 9]], 'Mag': 7, 'Fire': 'AutoSG', 'Type' : 'Shotguns'} # for 1 pellet, total is 12
]

Rifles = [
    {'Name': 'Bulldog', 'Price': 2100, 'Penetration': 2, 'Damage': [[0, 50, 35, 116,30]], 'Mag': 24, 'Fire': 'Auto', 'Type' : 'Rifles'}, 
    {'Name': 'Guardian', 'Price': 2700, 'Penetration': 2, 'Damage': [[0, 50, 65, 195, 49]], 'Mag': 12, 'Fire': 'SemiAuto', 'Type' : 'Rifles'},
    {'Name': 'Vandal', 'Price': 2900, 'Penetration': 2, 'Damage': [[0, 50, 39, 156, 33]], 'Mag': 25, 'Fire': 'Auto', 'Type' : 'Rifles'},
    {'Name': 'Phantom', 'Price': 2900, 'Penetration': 2, 'Damage': [[0, 15, 39, 156, 33], [15, 30, 35, 140, 30], [30, 50, 31, 124, 26]], 'Mag': 25, 'Fire': 'Auto', 'Type' : 'Rifles'}
]

Snipers = [
    {'Name': 'Marshal', 'Price': 1100, 'Penetration': 2, 'Damage': [[0, 50, 101, 202,85]], 'Mag': 5, 'Fire': 'Bolt', 'Type' : 'Snipers'}, 
    {'Name': 'Guardian', 'Price': 4500, 'Penetration': 3, 'Damage': [[0, 50, 150, 255, 127]], 'Mag': 5, 'Fire': 'Bolt', 'Type' : 'Snipers'}
]

Heavies = [
    {'Name': 'Ares', 'Price': 1600, 'Penetration': 3, 'Damage': [[0, 30, 30, 72, 25], [30, 50, 28, 67, 23]], 'Mag': 50, 'Fire': 'Auto' , 'Type' : 'Heavies'}, 
    {'Name': 'Odin', 'Price': 3200, 'Penetration': 3, 'Damage': [[0, 30, 38, 95, 32], [30, 50, 31, 77, 26]], 'Mag': 100, 'Fire': 'Auto', 'Type' : 'Heavies'}
]

Armors = [
    {'Name': 'Light', 'Price': 400, 'Strength' : 25}, {'Name': 'Heavy', 'Price': 1000, 'Strength' : 50}
]
main = ['SMGs', 'Rifles', 'Shotguns', 'Snipers', 'Heavies']
shop = {'Sidearms': Sidearms, 'SMGs': SMGs, 'Shotguns' : Shotguns, 'Rifles' : Rifles, 'Snipers' : Snipers, 'Heavies' : Heavies, 'Armors' : Armors, 'Anyweapon' : [Sidearms, SMGs, Shotguns, Rifles, Snipers, Heavies]}
