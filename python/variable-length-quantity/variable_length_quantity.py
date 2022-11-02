def encode(numbers):
    result = []
    for number in numbers:
        bin_number = bin(number)[2:]
        len_number = (len(bin_number)//7+1)*7 if len(bin_number)%7 else len(bin_number)
        bin_number = bin_number.zfill(len_number)
        vlq = []
        for i in range(0,len(bin_number),7):
            vlq.append('1'+bin_number[i:i+7])
        vlq[-1] = '0' + vlq[-1][1:]
        result.extend(vlq)
    return [int(num, 2) for num in result]


def decode(bytes_):
    if bin(bytes_[-1])[2:].zfill(8)[0] == '1':
        raise ValueError("incomplete sequence")
    numbers = []
    number = []
    for byte in bytes_:
        msb = bin(byte)[2:].zfill(8)[0]
        number.append(bin(byte)[2:].zfill(8)[1:])
        if msb == '0':
            numbers.append(''.join(number))
            number = []
    return [int(number,2) for number in numbers]
