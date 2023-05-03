import json

fileName = '005_Hin_und_her_gelaufen-2023-05-02_15-28-27.json'

with open(fileName) as data:
    d = json.load(data)

# Get all different sensor types
sensorTypes = []
for i in d:
    if (i.get('sensor') not in sensorTypes):
        sensorTypes.append(i.get('sensor'))

# Create a list for every sensor type
sortedBySensors = {}
for s in sensorTypes:
    listOfSensorType = []
    for i in d:
        if(s == i.get('sensor')):
            listOfSensorType.append(i)
    sortedBySensors[s] = listOfSensorType

# Create a JSON File for each Sensor Type
modifiedFileName = fileName.replace('.json', '-')
for i in range(len(sensorTypes)):
    with open(modifiedFileName + sensorTypes[i] + '.json', 'w') as f:
        json.dump(sortedBySensors.setdefault(sensorTypes[i]), f)

