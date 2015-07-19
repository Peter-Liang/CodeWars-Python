# coding=utf-8
"""
Vigenère Autokey Cipher Helper
http://www.codewars.com/kata/52d2e2be94d26fc622000735/train/python
"""


class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc

    def encode(self, text):
        result = []
        key = self.key + ''.join([t for t in text if t in self.abc])
        index = 0
        for c in text:
            if c in self.abc:
                offset = self.abc.index(key[index])
                result.append(self.abc[(self.abc.index(c) + offset) % len(self.abc)])
                index += 1
            else:
                result.append(c)
        return ''.join(result)

    def decode(self, text):
        result = []
        key = self.key
        index = 0
        for c in text:
            if c in self.abc:
                offset = self.abc.index(key[index])
                decoded = self.abc[(self.abc.index(c) - offset) % len(self.abc)]
                result.append(decoded)
                key += decoded
                index += 1
            else:
                result.append(c)
        return ''.join(result)