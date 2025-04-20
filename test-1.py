AllowedVehiclesList = [{
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
with open('testdb.txt', 'w') as db:
    for x in AllowedVehiclesList:
        db.write(f'{x['make']},{x['model']}\n')