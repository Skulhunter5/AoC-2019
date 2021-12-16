with open("../res/05-input.txt", 'r') as file:
    initial = list(map(int, [line.replace('\n', '') for line in file.readlines()][0].split(',')))

def getInput():
    return 5

def doOutput(output):
    print(output)

def intcodeComputer(mem):
    i = 0
    while(True):
        if(i >= len(mem)):
            print("\x1b[31m[ERROR]: trying to access int outside of the memory\x1b[0m")
            exit(1)
        opcode = int(str(mem[i])[-2:])
        parameterTypes = str(mem[i])[:-2]
        i += 1
        if(opcode == 99):
            break
        elif(opcode in [1, 2]):
            parameterTypes = ("0" * (2 - len(parameterTypes))) + parameterTypes
            a = mem[mem[i]] if parameterTypes[1] == "0" else mem[i]
            b = mem[mem[i+1]] if parameterTypes[0] == "0" else mem[i+1]
            if(opcode == 1):
                mem[mem[i+2]] = a + b
            else:
                mem[mem[i+2]] = a * b
            i += 3
        elif(opcode == 3):
            mem[mem[i]] = getInput()
            i += 1
        elif(opcode == 4):
            output = mem[mem[i]] if (("0" * (1 - len(parameterTypes))) + parameterTypes)[0] == "0" else mem[i]
            doOutput(output)
            i += 1
        elif(opcode in [5, 6]):
            parameterTypes = ("0" * (2 - len(parameterTypes))) + parameterTypes
            condition = mem[mem[i]] if parameterTypes[1] == "0" else mem[i]
            addr = mem[mem[i+1]] if parameterTypes[0] == "0" else mem[i+1]
            if((opcode == 5 and condition != 0) or (opcode == 6 and condition == 0)):
                i = addr
            else:
                i += 2
        elif(opcode in [7, 8]):
            parameterTypes = ("0" * (2 - len(parameterTypes))) + parameterTypes
            a = mem[mem[i]] if parameterTypes[1] == "0" else mem[i]
            b = mem[mem[i+1]] if parameterTypes[0] == "0" else mem[i+1]
            if(opcode == 7):
                mem[mem[i+2]] = 1 if a < b else 0
            else:
                mem[mem[i+2]] = 1 if a == b else 0
            i += 3
        else:
            print("\x1b[31m[ERROR]: invalid opcode\x1b[0m")
            exit(1)
    return mem

intcodeComputer(initial)
