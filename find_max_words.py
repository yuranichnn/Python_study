def read_file():
    with open('D:\Vashington Dzhordzh.txt', 'r') as text:
        list_input = []
        for line in text:
            list_input += line.lower().strip().split()
    return list_input


def create_dict(input):
    out = {}
    for i in input:
        out[i] = input.count(i)
    return out


def print_out(output):
    list_value = []
    list_key = []
    for value in output.values():
        list_value += [value]
    max_value = max(list_value)

    for key, value in output.items():
        if value == max_value:
            list_key += [key]
    list_key.sort()
    print(list_key[0], max_value, sep=' ')


print_out(create_dict(read_file()))
