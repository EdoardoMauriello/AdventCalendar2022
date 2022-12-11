def p1():
    # rock, paper, scissors
    opponent_list = ['A','B','C']
    # rock, paper, scissors
    player_list = ['X','Y','Z']
    with open('2/2.txt') as f:
        data = f.read().splitlines()
        for i in range(0, len(data)):
            data[i] = data[i].split(' ')
        points = 0
        for i in data:
            o = opponent_list.index(i[0])
            p = player_list.index(i[0])
            points += p + 1
            if o == p:
                print('tie ', i[1])
                points += 3
            elif o == (p + 1) % 3:
                print('lose', i[1])
                points += 0
            elif p == (o + 1) % 3:
                print('win', i[1])
                points += 6
        
        return points

def p2():
    # rock, paper, scissors
    opponent_list = ['A','B','C']
    # lose, draw, win
    outcome_list = ['X','Y','Z']

    with open('2/2.txt') as f:
        data = f.read().splitlines()
        for i in range(0, len(data)):
            data[i] = data[i].split(' ')
        points = 0
        for i in data:
            o = opponent_list.index(i[0])
            outcome = outcome_list.index(i[1])
            points += (outcome) * 3
            points += (o + outcome + 2) % 3 + 1
        
        return points

print(p2())
