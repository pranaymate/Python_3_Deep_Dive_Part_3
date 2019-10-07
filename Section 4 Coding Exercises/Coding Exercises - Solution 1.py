composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}


def sort_dict_by_value(d):
    d = {k: v
        for k, v in sorted(d.items(), key=lambda el: el[1])}
    return d


print(sort_dict_by_value(composers))

print('#' * 52 + '  Here is a better approach - instead of using a dictionary comprehension, '
                 '  we can simply use the dict() function to create a dictionary from the sorted tuples!')


def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda el: el[1]))


print(sort_dict_by_value(composers))

