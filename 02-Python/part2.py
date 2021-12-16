initial = None
with open("../res/02-input.txt", 'r') as file:
    initial = list(map(int, [line.replace('\n', '') for line in file.readlines()][0].split(',')))

def intcodeComputer(mem):
    i = 0
    while(True):
        if(i >= len(mem)):
            print("\x1b[31m[ERROR]: trying to access int outside of the memory\x1b[0m")
            exit(1)
        opcode = mem[i]
        if(opcode == 99):
            break
        elif(opcode == 1):
            mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
            i += 4
        elif(opcode == 2):
            mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
            i += 4
    return mem

for noun in range(100):
    for verb in range(100):
        mem = initial.copy()
        mem[1] = noun
        mem[2] = verb
        if(intcodeComputer(mem)[0] == 19690720):
            print(100 * noun + verb)
            exit(0)
