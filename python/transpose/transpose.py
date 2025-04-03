def transpose(lines):
    
    len_line = max(len(line) for line in lines.split("\n"))
    ljust = [string.ljust(len_line, "0") for string in lines.split("\n")]
    result = ["".join(list(i)).rstrip("0").replace("0", " ") for i in zip(*ljust)]
    
    return "\n".join(result)
    
    