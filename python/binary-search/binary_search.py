def find(search_list, value):
    
    start = 0
    end = len(search_list) - 1
    
    while end - start > 0:
        partition = (end-start)//2 + start
        if search_list[partition] == value:
            return partition
        elif value < search_list[partition]:
            end = partition - 1
        elif value > search_list[partition]:
            start = partition + 1
            
    if search_list and search_list[start] == value:
        return start 
    else:
        raise ValueError("value not in array")

