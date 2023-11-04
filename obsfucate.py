import random

def obsfucate(s):
    obsfucated = ""
    for c in s:
        obsfucated += c
        obsfucated += random.randint(len(s),len(s)+20) * '\x08'
    return obsfucated
try:
    while True:
        # Reads a line from STDIN
        line = input()
        print(obsfucate(line), end='')
except EOFError:
    exit(0)