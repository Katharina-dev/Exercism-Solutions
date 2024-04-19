from itertools import permutations

def can_chain(dominoes):
    
    if not dominoes:
        return []
    
    for lst in permutations(dominoes):
        
        chain = [lst[0]]
        
        for first, second in lst[1:]:
            
            head = chain[-1][-1]
            
            if first == head:
                chain.append((first, second))
            elif second == head:
                chain.append((second, first))
            else:
                break
            
        if len(chain) == len(lst) and chain[0][0] == chain[-1][-1]:
            
            return chain
        
