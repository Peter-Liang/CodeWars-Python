"""
ASCII85 Encoding & Decoding
http://www.codewars.com/kata/5277dc3ff4bfbd9a36000c1c/train/python
"""


def toAscii85(data):
    hexstr = ''
    result = ''
    for c in data:
        hexstr += format(ord(c), 'x')

        if len(hexstr) == 8:
            result += encode_to_ascii85(hexstr)
            hexstr = ''

    if len(hexstr) > 0:
        result += encode_to_ascii85(hexstr)
    return '<~' + result + '~>'


def encode_to_ascii85(hexstr):
    result = ''
    padding = (8 - len(hexstr)) / 2
    if padding > 0:
        hexstr += '00' * padding
    intresult = int(hexstr, 16)
    for _ in range(5):
        intresult, encoded_char = divmod(intresult, 85)
        if padding > 0:
            padding -= 1
        else:
            result = chr(encoded_char + 33) + result
    return result


def decode_from_ascii85(encoded_str):
    result = ''
    pass


def fromAscii85(data):
    # Decode data from ASCII85
    return
