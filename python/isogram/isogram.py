def is_isogram(string):
    
    string_upd = string.replace('-', '').replace(' ', '').lower()
    return len(string_upd) == len(set(string_upd))
    
