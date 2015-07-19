class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc
        self.start = ord(min(abc))

    def encode(self, text):
        result = []
        key = self.key + ''.join([t for t in text if t in self.abc])
        index = 0
        for c in text:
            if c in self.abc:
                offset = ord(key[index]) - self.start
                result.append(chr(((ord(c) - self.start + offset) % len(self.abc)) + self.start))
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
                offset = ord(key[index]) - self.start
                decoded = chr(((ord(c) - self.start - offset) % len(self.abc)) + self.start)
                result.append(decoded)
                key += decoded
                index += 1
            else:
                result.append(c)
        return ''.join(result)