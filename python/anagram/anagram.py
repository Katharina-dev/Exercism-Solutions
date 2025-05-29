def find_anagrams(word, candidates):
    
    word = word.lower()
    return [can for can in candidates if sorted(can.lower()) == sorted(word) and can.lower() != word]
