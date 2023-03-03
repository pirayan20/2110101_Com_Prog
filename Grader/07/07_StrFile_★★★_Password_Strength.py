import string


def no_lowercase(t):
    for i in range(len(t)):
        if t[i] in string.ascii_lowercase:
            return False
            break
    return True


def no_uppercase(t):
    for i in range(len(t)):
        if t[i] in string.ascii_uppercase:
            return False
            break
    return True


def no_number(t):
    for i in range(len(t)):
        if t[i] in string.digits:
            return False
            break
    return True


def no_symbol(t):
    for i in range(len(t)):
        if t[i] in string.punctuation:
            return False
            break
    return True


def character_repetition(t):
    for i in range(len(t)-3):
        if t[i] == t[i+1]:
            if t[i+1] == t[i+2]:
                if t[i+2] == t[i+3]:
                    return True
                    break
    return False


def number_sequence(t):
    digits = string.digits + "0123"
    for i in range(len(t)-3):
        for j in range(len(digits)-3):
            if t[i:i+4] == digits[j:j+4]:
                return True
                break
    convert = digits[::-1]
    for i in range(len(t)-3):
        for j in range(len(convert)-3):
            if t[i:i+4] == convert[j:j+4]:
                return True
                break
    return False


def letter_sequence(t):
    y = t.lower()
    alphabet = string.ascii_lowercase + "abcd"
    for i in range(len(y)-3):
        for j in range(len(alphabet)-3):
            if y[i:i+4] == alphabet[j:j+4]:
                return True
                break
    convert = alphabet[::-1]
    for i in range(len(y)-3):
        for j in range(len(convert)-3):
            if y[i:i+4] == convert[j:j+4]:
                return True
                break
    return False


def keyboard_pattern(t):
    y = t.lower()
    s1 = "!@#$%^&*()_+"
    s2 = "qwertyuiop"
    s3 = "asdfghjkl"
    s4 = "zxcvbnm"
    for i in range(len(y)-3):
        for j in range(len(s1)-3):
            if y[i:i+4] == s1[j:j+4]:
                return True
                break
    cs1 = s1[::-1]
    for i in range(len(y)-3):
        for j in range(len(cs1)-3):
            if y[i:i+4] == cs1[j:j+4]:
                return True
                break

    for i in range(len(y)-3):
        for j in range(len(s2)-3):
            if y[i:i+4] == s2[j:j+4]:
                return True
                break
    cs2 = s2[::-1]
    for i in range(len(y)-3):
        for j in range(len(cs2)-3):
            if y[i:i+4] == cs2[j:j+4]:
                return True
                break

    for i in range(len(y)-3):
        for j in range(len(s3)-3):
            if y[i:i+4] == s3[j:j+4]:
                return True
                break
    cs3 = s3[::-1]
    for i in range(len(y)-3):
        for j in range(len(cs3)-3):
            if y[i:i+4] == cs3[j:j+4]:
                return True
                break

    for i in range(len(y)-3):
        for j in range(len(s4)-3):
            if y[i:i+4] == s4[j:j+4]:
                return True
                break
    cs4 = s4[::-1]
    for i in range(len(y)-3):
        for j in range(len(cs4)-3):
            if y[i:i+4] == cs4[j:j+4]:
                return True
                break
    return False


passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")

if no_lowercase(passw):
    errors.append("No lowercase letters")

if no_uppercase(passw):
    errors.append("No uppercase letters")

if no_number(passw):
    errors.append("No numbers")

if no_symbol(passw):
    errors.append("No symbols")

if character_repetition(passw):
    errors.append("Character repetition")

if number_sequence(passw):
    errors.append("Number sequence")

if letter_sequence(passw):
    errors.append("Letter sequence")

if keyboard_pattern(passw):
    errors.append("Keyboard pattern")

if len(errors) == 0:
    print("OK")
else:
    for i in errors:
        print(i)
