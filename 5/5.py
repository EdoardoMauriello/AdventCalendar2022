from re import findall

def p1():
    with open('5/5.txt') as f:
        data = f.read().splitlines()
        stacks = []
        i = 0
        for i in range(len(data[0].replace(' ', ''))):
            stacks.append([])
        while data[i] != '':
            i += 1
        mat = []
        for k in range(i-2, -1, -1):
            mat.append(data[k].replace('[', '').replace(']', '').replace('    ', ' ').split(' '))
        for m in range(len(mat)):
            for j in range(len(mat[m])):
                if mat[m][j] != '':
                    stacks[j].append(mat[m][j])
        move = []
        k = 0
        for k in range(i+1, len(data)):
            move = findall(r'\d+', data[k])
            for j in range(int(move[0])):
                stacks[int(move[2])-1].append(stacks[int(move[1])-1].pop())
        
        word = ''
        for stack in stacks:
            word += stack.pop()
        return word

def p2():
    with open('5/5.txt') as f:
        data = f.read().splitlines()
        stacks = []
        i = 0
        for i in range(len(data[0].replace(' ', ''))):
            stacks.append([])
        while data[i] != '':
            i += 1
        mat = []
        for k in range(i-2, -1, -1):
            mat.append(data[k].replace('[', '').replace(']', '').replace('    ', ' ').split(' '))
        for m in range(len(mat)):
            for j in range(len(mat[m])):
                if mat[m][j] != '':
                    stacks[j].append(mat[m][j])
        move = []
        k = 0
        for k in range(i+1, len(data)):
            move = findall(r'\d+', data[k])
            temp = []
            for j in range(int(move[0])):
                temp.append(stacks[int(move[1])-1].pop())
            temp.reverse()
            for e in temp:
                stacks[int(move[2])-1].append(e)
        
        word = ''
        for stack in stacks:
            word += stack.pop()
        return word
print(p2())