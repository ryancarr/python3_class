BASE02 = {0: '0', 1: '1'}
BASE08 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}
BASE16 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
          9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
# BASE64 is in place but isn't correctly implemented
BASE64 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
          9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
          17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
          25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g',
          33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o',
          41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w',
          49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4',
          57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'}

BASE = {2: BASE02, 8: BASE08, 16: BASE16, 64: BASE64}

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


inp = input("Enter a string to convert to another base: ")
base = int(input("What base would you like to convert to? (2, 8, 16): "))

print(stringToDigits(inp, base))

input("Press any key to continue...")
