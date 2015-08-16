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


def fromAscii85(data):
    result = ''
    illegal_character = ['\n', ' ', '\0', '\t']
    for c in illegal_character:
        data = data.replace(c, '')
    data = data[2:-2]

    index = 0
    while index < len(data):
        if data[index] == 'z':
            result += '\0' * 4
            index += 1
        else:
            padding = max(index + 5 - len(data), 0)
            encoded_block = data[index:index + 5] if padding == 0 else data[index:] + 'u' * padding
            encoded_int = 0
            for i, c in enumerate(encoded_block[::-1]):
                encoded_int += (ord(c) - 33) * (85 ** i)
            encoded_byte = format(encoded_int, '08x')
            if padding > 0:
                encoded_byte = encoded_byte[:-padding * 2]
            index += 5
            result += ''.join([chr(int(encoded_byte[i:i + 2], 16)) for i in range(0, len(encoded_byte), 2)])
    return result
