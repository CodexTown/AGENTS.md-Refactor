def process_data(d):
    # This function processes data
    r = []
    for i in d:
        if i > 10:
            r.append(i * 2)
        else:
            r.append(i + 5)
    return r

def calc_stats(l):
    s = 0
    for x in l:
        s += x
    return s / len(l)

data = [5, 12, 8, 20, 3]
res = process_data(data)
print(res)
print(calc_stats(res))
