def pprint(A):
    if A.ndim == 1:
        print(A)
    else:
        w = max([len(str(s)) for s in A])
        print(u'\u250c' + u'\u2500' * w + u'\u2510')
        for AA in A:
            print(' ', end='')
            print('[', end='')
            for i, AAA in enumerate(AA[:-1]):
                w1 = max([len(str(s)) for s in A[:, i]])
                print(str(AAA) + ' ' * (w1 - len(str(AAA)) + 1), end='')
            w1 = max([len(str(s)) for s in A[:, -1]])
            print(str(AA[-1]) + ' ' * (w1 - len(str(AA[-1]))), end='')
            print(']')
        print(u'\u2514' + u'\u2500' * w + u'\u2518')


def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")
