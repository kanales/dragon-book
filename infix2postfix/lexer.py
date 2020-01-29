import re

DIGIT = re.compile(r'\d')
WHITESPACE = re.compile(r'\s')
OPERATOR = re.compile(r'[\+\-\*\/]')

class LexicalError(Exception):
    pass

def lex(s):
    tokens = []
    acc = []
    it = iter(s)
    
    try:
        while True:
            c = next(it)
            if re.match(DIGIT, c):
                acc.append(c)
                continue
            elif acc:
                tokens.append(''.join(acc))
                acc = []

            if re.match(OPERATOR, c):
                tokens.append(c)
            elif not re.match(WHITESPACE, c):
                raise LexicalError() # todo say error
    except StopIteration:
        if acc:
            tokens.append(''.join(acc))
        return tokens
