BASE02 = {0: '0', 1: '1'}
BASE08 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}
BASE16 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
          9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

BASE = {2: BASE02, 8: BASE08, 16: BASE16}

def stringToDigits(inp, base):
    result = ''
    for letter in inp:
        letter = ord(letter)
        lst = []
        while letter > 0:
            lst.insert(0, BASE[base][letter % base])
            letter = letter // base
        result += "".join(lst)

    return result
