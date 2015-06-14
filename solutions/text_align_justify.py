"""
Text align justify

http://www.codewars.com/kata/537e18b6147aa838f600001b/train/python
"""


def justify(text, width):
    words = text.split()
    current_len = 0
    line_words = []
    lines = [line_words]
    for word in words:
        if current_len + len(word) > width:
            line_words = [word]
            lines.append(line_words)
            current_len = len(word) + 1
        else:
            line_words.append(word)
            current_len += len(word) + 1
    for i in range(len(lines) - 1):
        line_words = lines[i]
        space_need = width - sum(len(word) for word in line_words)
        while space_need:
            for index in range(len(line_words) - 1):
                if space_need == 0:
                    break
                line_words[index] += ' '
                space_need -= 1
        lines[i] = ''.join(line_words) + '\n'
    lines[-1] = ' '.join(lines[-1])
    return ''.join(lines)
