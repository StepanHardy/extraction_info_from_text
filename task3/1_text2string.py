import re


WORD_RE = re.compile(r"[\w\,']+")
PATTERN_RE = re.compile(r"[=]+")

input = open("1_Facts.txt", "r+")
text = input.read()


if __name__ == '__main__':

    output = open("2_text2string.txt", "w+")

    middle = re.split(PATTERN_RE, text)
    for mid in middle:
        text2 = re.findall(WORD_RE, mid)
        lineBreak = False
        for word in text2:
            lineBreak = True
            output.write(word + ' ')
        if lineBreak:
            output.write('\n')





