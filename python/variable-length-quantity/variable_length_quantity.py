vlq_num_mask = 0b1111111
vlq_continue_mask = 128

def encode(numbers):
    
    return [((number>>(7*i)) & vlq_num_mask) | (bool(i)<<7)
            for number in numbers
            for i in range(((number>>1).bit_length())//7, -1, -1)]


def decode(bytes_):
    
    result = []
    code = 0
    if bytes_[-1] & vlq_continue_mask:
        raise ValueError('incomplete sequence')
    for byte in bytes_:
        code = (code << 7)|(byte & vlq_num_mask)
        if not(byte & vlq_continue_mask):
            result.append(code)
            code = 0
            
    return result
