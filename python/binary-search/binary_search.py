def find(search_list, value):
    start = 0
    end = len(search_list)
    while end - start > 1:
        partition = (end-start)//2 + start
        if value in search_list[start:partition]:
            end = partition
        else:
            start = partition
    if not search_list or search_list[start] != value:
        raise ValueError("value not in array")
    return start

