n = int(input('Введите число\t'))
matrix = [[0 for i in range(n)] for j in range(n)]
n_current = 1
ic, jc = 0, 0
str = 0
while n_current <= n ** 2:
    if matrix[ic][jc + 1 - n] == 0 and matrix[ic][str - 1] == 0 and 0 <= jc < n - 1:
        matrix[ic][jc] = n_current
        jc += 1
        n_current += 1
    elif matrix[ic + 1 - n][jc] == 0 and 0 <= ic < n - 1:
        matrix[ic][jc] = n_current
        ic += 1
        n_current += 1
    elif matrix[ic][jc - 1] == 0:
        matrix[ic][jc] = n_current
        jc -= 1
        n_current += 1
    elif matrix[ic - 1][jc] == 0:
        matrix[ic][jc] = n_current
        ic -= 1
        n_current += 1
    elif n % 2 == 1 and ic == jc:
        matrix[ic][ic] = n_current
        break
    elif n % 2 == 0 and n / 2 == jc + 1:
        matrix[ic][jc] = n_current
        break
    else:
        str -= 1
for i in matrix:
    print(*i)
