from binascii import b2a_hex

"""
ASCII85 Encoding & Decoding
http://www.codewars.com/kata/5277dc3ff4bfbd9a36000c1c/train/python
"""


def toAscii85(data):
    hex_str = ''
    result = ''
    for c in data:
        # hex_str += '{:02x}'.format(ord(c))
        hex_str += format(ord(c), '02x')
        if len(hex_str) == 8:
            result += encode_to_ascii85(hex_str)
            hex_str = ''

    if len(hex_str) > 0:
        result += encode_to_ascii85(hex_str)
    return '<~' + result + '~>'


def encode_to_ascii85(hex_str):
    if hex_str == '0' * 8:
        return 'z'
    result = ''
    padding = (8 - len(hex_str)) / 2
    if padding > 0:
        hex_str += '00' * padding
    intresult = int(hex_str, 16)

    for _ in range(5):
        intresult, encoded_char = divmod(intresult, 85)
        if padding > 0:
            padding -= 1
        else:
            result = chr(encoded_char + 33) + result
    return result


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
    # print('byte_result: %s' % byte_result)
    if padding > 0:
        byte_result = byte_result[:-(padding * 2)]
    # print('byte_result: %s' % byte_result)
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
    # print('result: %s' % result)
    # print('len: %d' % len(result))
    if result == '\0':
        return '\x00'
    return result
