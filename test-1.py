AllowedVehiclesLists = [{
        'make': 'Ford',
        'model': 'f-150'
    }, {
        'make': 'Chevrolet',
        'model': 'Silverado'
    }, {
        'make': 'Tesla',
        'model': 'CyberTruck'
    }, {
        'make': 'Toyota',
        'model': 'Tundra'
    }, {
        'make': 'Nissan',
        'model': 'Titan'
    }, {
        'make': 'Rivian',
        'model': 'R1T'
    }, {
        'make': 'Ram',
        'model': '1500'
    }]


AllowedVehiclesList = ['Ford f-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']

#safe the list
with open('testdb.txt', 'w') as db:
    for x in AllowedVehiclesList:
        db.write(x + '\n') 

addVehicle = input('no se: ')
with open('testdb.txt', 'r') as db:
    saved_vehicules = [line.strip() for line in db.readlines()]

if addVehicle not in saved_vehicules:
    saved_vehicules.append(addVehicle)

remove = input('lol: ')
if remove in saved_vehicules:
    saved_vehicules.remove(remove)

with open('testdb.txt', 'w') as db:
    for vehicle in saved_vehicules:
        db.write(vehicle + '\n')

for x in saved_vehicules:
    print(x)
    