def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for i in lists:
        result += i
    return result


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    count = 0
    for i in list:
        count += 1
    return count


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    for i in list:
        initial = function(initial,i)
    return initial


def foldr(function, list, initial):
    for i in list[::-1]:
        initial = function(initial,i)
    return initial if type(initial) == int else initial[::-1]


def reverse(list):
    return list[::-1]

