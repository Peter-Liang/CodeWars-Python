"""
3 kyu: Morse Encoding
https://www.codewars.com/kata/morse-encoding/train/python
"""
class Morse:

    @classmethod
    def encode(self, message):
        words = message.split(' ')
        code = ('0' * 7).join(['000'.join([Morse.alpha[c.upper()]
                                           for c in word]) for word in words])
        result = []
        for i in range(0, len(code), 32):
            num = code[i:i + 32].ljust(32, '0')
            result.append(int(num[1:], 2) -
                          (0 if num[0] == '0' else Morse.neg))
        return result

    @classmethod
    def decode(self, array):
        code = ''
        for num in array:
            if num < 0:
                num += Morse.neg
                code += '1' + bin(num)[2:].rjust(31, '0')
            else:
                code += bin(num)[2:].rjust(32, '0')
        code = code.rstrip('0')
        result = ' '.join([''.join([next(k for k, v in Morse.alpha.items() if v == char)
                                    for char in words.split('000')]) for words in code.split('0' * 7)])

        return result

    neg = 1 << 31

    alpha = {
        'A': '10111',
        'B': '111010101',
        'C': '11101011101',
        'D': '1110101',
        'E': '1',
        'F': '101011101',
        'G': '111011101',
        'H': '1010101',
        'I': '101',
        'J': '1011101110111',
        'K': '111010111',
        'L': '101110101',
        'M': '1110111',
        'N': '11101',
        'O': '11101110111',
        'P': '10111011101',
        'Q': '1110111010111',
        'R': '1011101',
        'S': '10101',
        'T': '111',
        'U': '1010111',
        'V': '101010111',
        'W': '101110111',
        'X': '11101010111',
        'Y': '1110101110111',
        'Z': '11101110101',
        '0': '1110111011101110111',
        '1': '10111011101110111',
        '2': '101011101110111',
        '3': '1010101110111',
        '4': '10101010111',
        '5': '101010101',
        '6': '11101010101',
        '7': '1110111010101',
        '8': '111011101110101',
        '9': '11101110111011101',
        '.': '10111010111010111',
        ',': '1110111010101110111',
        '?': '101011101110101',
        "'": '1011101110111011101',
        '!': '1110101110101110111',
        '/': '1110101011101',
        '(': '111010111011101',
        ')': '1110101110111010111',
        '&': '10111010101',
        ':': '11101110111010101',
        ';': '11101011101011101',
        '=': '1110101010111',
        '+': '1011101011101',
        '-': '111010101010111',
        '_': '10101110111010111',
        '"': '101110101011101',
        '$': '10101011101010111',
        '@': '10111011101011101',
        ' ': '0'}

if __name__ == '__main__':
    print(Morse.encode('hello world'))
    # print(Morse.encode('EEEEEEEIE'))
    # print(Morse.decode([-2004318070, 536870912]))
    print(Morse.decode([-1440552402, -1547992901, -1896993141, -1461059584]))
