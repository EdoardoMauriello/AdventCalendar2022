def p1():
    with open('elves.txt') as f:
        data = f.read().splitlines()
        sum = 0
        index = 0
        elf = []
        for i in data:
            if i != '':
                sum += int(i)
            else:
                elf.append((index, sum))
                index += 1
                sum = 0
        
        max = 0
        for i in elf:
            if i[1] > max:
                max = i[1]
                index = i[0]

        return max

def p2():
    with open('elves.txt') as f:
        data = f.read().splitlines()

        sum = 0
        index = 0
        elf = []
        for i in data:
            if i != '':
                sum += int(i)
            else:
                elf.append((index, sum))
                index += 1
                sum = 0
        
        sum = 0
        elf.sort(key=lambda x: x[1], reverse=True)
        for i in range(0,3):
            sum += elf[i][1]

        return sum
