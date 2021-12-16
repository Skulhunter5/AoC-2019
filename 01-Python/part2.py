moduleWeights = None
with open("../res/01-input.txt", 'r') as file:
    moduleWeights = list(map(int, [line.replace('\n', '') for line in file.readlines()]))

fuelNeeded = 0
for weight in moduleWeights:
    last = weight
    while(last > 0):
        last = int(last / 3) - 2
        if(last > 0):
            fuelNeeded += last

print(fuelNeeded)
