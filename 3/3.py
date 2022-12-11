def p1():
    with open("3/3.txt") as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            data[i] = (data[i][0:int(data[i].__len__()/2)], data[i][int(data[i].__len__()/2):data[i].__len__()])
        duplicates = []
        for i in data:
            for j in i[0]:
                if j in i[1]:
                    duplicates.append(j)
                    break
        
        psum = 0
        for i in duplicates:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                psum += ord(i) - 96
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                psum += ord(i) - 38

        print(psum, duplicates[0], data[0])

def p2():
    with open("3/3.txt") as f:
        data_raw = f.read().splitlines()
        data = []
        for i in range(0, len(data_raw), 3):
            data.append((data_raw[i], data_raw[i+1], data_raw[i+2]))

        badges = []
        duplicates = dict()
        for i in data:
            duplicates.clear()
            for k in range(0, len(i)):
                for j in range(len(i[k])):
                    if i[k][j] in duplicates.keys():
                        duplicates[i[k][j]][k] += 1
                    else:
                        duplicates[i[k][j]] = [0,0,0]
                        duplicates[i[k][j]][k] = 1
            for d in duplicates:
                prod = 1
                for k in range(0, len(duplicates[d])):
                    prod *= duplicates[d][k-1]
                if prod > 0:
                    badges.append(d)
                    break
        
        psum = 0
        for i in badges:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                psum += ord(i) - 96
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                psum += ord(i) - 38
        
        print(psum)
p2()