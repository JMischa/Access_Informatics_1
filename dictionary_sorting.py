
def dict_to_lists(d):
    sorted_values = sorted(d.values())
    keys = [key for key in d.keys()]
    values = [d[key] for key in keys]
    sorted_keys = [key for _, key in sorted(zip(values, keys))]
    return sorted_keys, sorted_values

def dict_to_lists(d):
    sorted_values = sorted(d.values(), reverse=True)
    keys = [key for key in d.keys()]
    values = [d[key] for key in keys]
    sorted_keys = [key for _, key in sorted(zip(values, keys), reverse=True)]
    return sorted_keys, sorted_values


def dict_to_lists(d):
    sorted_keys = sorted(d.keys(), reverse=True)
    values = [d[key] for key in sorted_keys]
    return sorted_keys, values


def dict_to_lists(d):
    sorted_keys = sorted(d.keys())
    values = [d[key] for key in sorted_keys]
    return sorted_keys, values

