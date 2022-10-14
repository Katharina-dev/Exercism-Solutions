import re
def grep(pattern, flags, files):
    result = []
    for file in files:
        with open(file) as my_file:
            my_lines = my_file.readlines()
            count = 0
            for line in my_lines:
                count += 1
                if (re.findall(r'.*[ix].*[ix].*', flags) and re.findall(f'^{pattern}$', line, re.IGNORECASE)) or \
                (re.findall(r'.*[xv].*[xv].*', flags) and not re.findall(f'^{pattern}$', line)) \
                or (re.findall(r'^[^xv]*i[^xv]*$', flags) and re.findall(pattern, line, re.IGNORECASE)) or \
                (re.findall(r'^[^vi]*x[^vi]*$', flags) and re.findall(f'^{pattern}$', line)) or \
                (re.findall(r'^[^xi]*v[^xi]*$', flags) and not re.findall(pattern, line)) or \
                (not re.findall(r'[xvi]', flags) and re.findall(pattern, line)):
                    if re.findall(r'.*l.*', flags):
                        result.append(f'{file}\n')
                        break
                    elif len(files) == 1:
                        if not re.findall(r'n', flags):
                            result.append(line)
                        elif re.findall(r'n', flags):
                            result.append(f'{count}:{line}')
                    elif len(files) > 1:
                        if not re.findall(r'n', flags):
                            result.append(f'{file}:{line}')
                        elif re.findall(r'n', flags):
                            result.append(f'{file}:{count}:{line}')
    return ''.join(result)
