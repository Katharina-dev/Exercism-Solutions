from itertools import permutations

def solve(puzzle):
    
    words = puzzle.replace('+', '').replace('=', '').split()
    first_letters = {ord(w[0]) for w in words}
    letters = "".join(set(''.join(words)))
    num_letters = len(letters)
    
    for perm in permutations(range(10), num_letters):
        trans = str.maketrans(letters, "".join(map(str, perm)))
        if any(trans[l] == 48 for l in first_letters):
            continue
        num = [word.translate(trans) for word in words]
        *adds, target = map(int, num)
        if sum(adds) == target:
            return dict(zip(letters, perm)) 
