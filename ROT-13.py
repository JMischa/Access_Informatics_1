
#!/usr/bin/env python3

# perform a ROTn encoding
def rot_n(plain_text, shift_by):
    # Make sure to return the correct result!
    result = ""
    for c in plain_text:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) + shift_by - 65) % 26 + 65)
            else:
                result += chr((ord(c)+ shift_by - 97) % 26 + 97)
        else:
            result += c

    return result

print(rot_n("abc", 2))

