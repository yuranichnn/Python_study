string, stolb, mins = (int(i) for i in input().split())
pole = [[0 for i in range(stolb)] for j in range(string)]

for i in range(mins):
    row, col = (int(i) - 1 for i in input().split())
    pole[row][col] = '*'
for i in range(string):
    for j in range(stolb):
        if pole[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    smest_str = i + di
                    smest_stolb = j + dj
                    if 0 <= smest_stolb < stolb and 0 <= smest_str < string and pole[smest_str][smest_stolb] == '*':
                        pole[i][j] += 1
for i in range(string):
    for j in range(stolb):
        if pole[i][j] == 0:
            print('.', end='')
        else:
            print(pole[i][j], end='')
    print()
