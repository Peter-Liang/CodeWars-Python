"""
ASCII85 Encoding & Decoding
http://www.codewars.com/kata/5277dc3ff4bfbd9a36000c1c/train/python
"""


def toAscii85(data):
    hex_str = ''
    result = ''
    for c in data:
        hex_str += format(ord(c), '02x')
    index = 0
    while index < len(hex_str):
        padding = max(((index + 8) - len(hex_str)) / 2, 0)
        encode_block = hex_str[index:index + 8] if padding == 0 else hex_str[index:] + '00' * padding
        if encode_block == '0' * 8 and padding == 0:
            result += 'z'
        else:
            encode_block_int = int(encode_block, 16) / (85 ** padding)
            encode_block_result = ''
            for _ in range(5 - padding):
                encode_block_int, remainder = divmod(encode_block_int, 85)
                encode_block_result = chr(remainder + 33) + encode_block_result
            result += encode_block_result
        index += 8
    return '<~' + result + '~>'


def decode_from_ascii85(encoded_str):
    if encoded_str == 'z':
        return '\0' * 4
    padding = 5 - len(encoded_str)
    if padding > 0:
        encoded_str += 'u' * padding
    int_sum = 0
    for i, c in enumerate(encoded_str):
        int_sum += (ord(c) - 33) * (85 ** (4 - i))
    byte_result = format(int_sum, '08x')
    if padding > 0:
        byte_result = byte_result[:-(padding * 2)]
    return ''.join([chr(int(byte_result[i:i + 2], 16)) for i in range(0, len(byte_result), 2)])


def fromAscii85(data):
    result = ''
    illegal_character = ['\n', ' ', '\0', '\t']
    for c in illegal_character:
        data = data.replace(c, '')
    data = data[2:-2]

    index = 0
    while index < len(data):
        if data[index] != 'z':
            if index + 5 < len(data):
                result += decode_from_ascii85(data[index:index + 5])
            else:
                result += decode_from_ascii85(data[index:])
            index += 5
        else:
            result += decode_from_ascii85(data[index:index + 1])
            index += 1
    return result
