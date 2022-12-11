def p1():
    with open('4/4.txt') as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            data[i] = data[i].split(',')
            data[i] = (data[i][0].split('-'), data[i][1].split('-'))
        unefficient = 0
        for d in data:
            if (int(d[0][0]) >= int(d[1][0]) and int(d[0][1]) <= int(d[1][1])) or (int(d[0][0]) <= int(d[1][0]) and int(d[0][1]) >= int(d[1][1])):
                unefficient += 1
        return unefficient
        
def p2():
    with open('4/4.txt') as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            data[i] = data[i].split(',')
            data[i] = (data[i][0].split('-'), data[i][1].split('-'))
        unefficient = 0
        for d in data:
            if (int(d[0][0]) >= int(d[1][0]) and int(d[0][1]) <= int(d[1][1])) or (int(d[0][0]) <= int(d[1][0]) and int(d[0][1]) >= int(d[1][1])):
                unefficient += 1
            elif int(d[0][1]) >= int(d[1][0]) and int(d[0][1]) <= int(d[1][1]) or int(d[0][0]) >= int(d[1][0]) and int(d[0][0]) <= int(d[1][1]):
                print(d)
                unefficient += 1
        return unefficient
