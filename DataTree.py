
data = {}

inp = [
    "123",
    "125",
    "725",
    "136"
]


for numbers in inp:
    d = dict(data)
    x = True
    for num in range(len(numbers)):
        if numbers[num] in list(d.keys()):
            d = d[numbers[num]]
            x = False
        else:
            r = {}
            for n in numbers[num+1:][::-1]:
                c = dict(r)
                r = {}
                r[n] = c
            d[numbers[num]] = r
            break
    if x: data = {**data, **d}

print(data)