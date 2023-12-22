__author__ = "Mischa Jampen"


def compress(data):
    if len(data) == 0:
        return ((), [])
    
    keys = tuple(sorted(data[0].keys()))
    values = []

    for d in data:
        v = []
        for k in keys:
            v.append(d[k])
        values.append(tuple(v))

    return (keys, values)


data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 9, "c": 7, "b": 8}
]

print(compress(data))




















