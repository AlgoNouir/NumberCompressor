

from pprint import pprint
from numpy import number


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
                x = dict(r)
                r = {}
                r[n] = x
            d[numbers[num]] = r
            break
    if x:
        data = {**data, **d}

pprint(data)