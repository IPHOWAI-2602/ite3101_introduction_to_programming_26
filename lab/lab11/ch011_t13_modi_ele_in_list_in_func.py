n = [6, 10, 14]

def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))