def proverb(*input_data, qualifier=None):
    if not input_data:
        return []
    proverb = []
    for i in range(1,len(input_data)):
        string = f"For want of a {input_data[i-1]} the {input_data[i]} was lost."
        proverb.append(string)
    last_word = qualifier + " " + input_data[0] if qualifier else input_data[0]
    last_string = f"And all for the want of a {last_word}."
    proverb.append(last_string)
    return proverb
