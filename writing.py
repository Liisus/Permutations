def rewrite(st):
    s = set()
    t = tuple(map(int, st[1:-1:].split(', ')))
    cycles = []
    for i in range(len(t)):
        if i not in s:
            s.add(i)
            b = str(i + 1)
            k = t[i] - 1
            while t[k] != i + 1:
                s.add(k)
                b += str(k + 1)
                k = t[k] - 1
            s.add(k)
            if k != i:
                b += str(k + 1)
            cycles.append(b[0] + b[-1:0:-1])
    return '(' + ')('.join(cycles) + ')'

# у меня нет комментариев по поводу этого быдлокода
# оно работает, и на том спасибо


with open('S4.txt', 'r') as file:
    for line in file:
        h = line.strip()
        for i in h.split('; '):
            print(rewrite(i), end='; ')
        print()
