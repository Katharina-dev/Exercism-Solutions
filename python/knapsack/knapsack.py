def maximum_value(maximum_weight, items):
    
    if not items:
        return 0
    
    weights = list(range(maximum_weight+1))
    table = {weight: [{count: 0} for count in range(len(items))] for weight in weights}
    
    for weight in weights:
        table[weight][0][0] = items[0]['value'] if items[0]['weight'] <= weight else 0
        
    for count, item in enumerate(items[1:],1):
        current_value = item['value']
        
        for weight in weights:
            prev_max = table[weight][count-1][count-1]
            delta = weight - items[count]['weight']
            
            if  delta >= 0:
                max_value_free_w = table[delta][count-1][count-1] if delta in table else 0
                table[weight][count][count] = max(prev_max, current_value + max_value_free_w)
                
            else:
                table[weight][count][count] = prev_max
                
    return table[maximum_weight][-1][len(items)-1]
