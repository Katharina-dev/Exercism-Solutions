animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow"]
second_line = ["It wriggled and jiggled and tickled inside her.", "How absurd to swallow a bird!", "Imagine that, to swallow a cat!", "What a hog, to swallow a dog!", "Just opened her throat and swallowed a goat!", "I don't know how she swallowed a cow!"]

def recite(start_verse, end_verse):
    result = []
    for i in range(start_verse-1, end_verse):
        if i == 0:
            sub_result = ['I know an old lady who swallowed a fly.', "I don't know why she swallowed the fly. Perhaps she'll die."]
        elif i == 7:
            sub_result = ["I know an old lady who swallowed a horse.", "She's dead, of course!"]
        else:
            sub_result = []
            sub_result.append(f"I know an old lady who swallowed a {animals[i]}.")
            sub_result.append(second_line[i-1])
            for j in range(i):
                line = f'She swallowed the {animals[j+1]} to catch the {animals[j]}.'
                if j == 1:
                    line = line[:-1] + " that wriggled and jiggled and tickled inside her."
                sub_result.insert(2, line)
            sub_result.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        result.extend(sub_result+[""])
    return result[:-1]
