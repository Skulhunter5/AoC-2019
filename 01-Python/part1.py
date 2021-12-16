moduleWeights = None
with open("../res/01-input.txt", 'r') as file:
    moduleWeights = list(map(int, [line.replace('\n', '') for line in file.readlines()]))

fuelNeeded = 0
for weight in moduleWeights:
    fuelNeeded += int(weight / 3) - 2

print(fuelNeeded)
