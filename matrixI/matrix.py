string_in = input()
matrix_in = []
while string_in != 'end':
    matrix_in.append([int(i) for i in string_in.split()])
    string_in = input()
if matrix_in != []:
    kol_string = len(matrix_in)
    kol_stolb = len(matrix_in[0])
matrix_out = []
for i in range(kol_string):
    matrix_out.append([0] * kol_stolb)
# if kol_string == 1:
for i in range(kol_string):
    for j in range(kol_stolb):
        matrix_out[i][j] = matrix_in[i][j - kol_stolb + 1] + \
                           matrix_in[i][j - 1] + \
                           matrix_in[i - kol_string + 1][j] + \
                           matrix_in[i - 1][j]
for i in matrix_out:
    print(*i)
