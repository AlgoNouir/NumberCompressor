

numberList = [
    "1230",
    "1251",
    "1282",
    "1293"
]


def toBit(l):
    number = ['0']*10
    for num in l:
        number[int(num)] = "1"
    number = "".join(number)
    return number


def func(inp, x):
    r = []
    if x > 1:
        for o in list(inp.values()):
            r += func(o, x-1)
        return r
    else:
        return [list(inp.keys())]



data = {}
for numbers in numberList:
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



r = ""
for o in range(len(numberList[0])):
    for t in func(data, o+1):
        r += toBit(t)

print(r)