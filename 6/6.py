def p1(window=4):
    with open('6/6.txt') as f:
        data = f.read()
        flag = False
        for i in range(len(data)-window):
            temp = [x for x in data[i:i+window]]
            while len(temp) != 0:
                if temp.pop() in temp:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                return i + window

def p2():
    return p1(14)

print(p2())


        