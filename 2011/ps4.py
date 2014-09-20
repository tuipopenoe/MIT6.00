#!python2
# Tui Popenoe
# ps4.py - Caesar ciphers

characters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.
    """
    cipher = {}
    if shift > 27:
        shift = 27
    if shift < 1:
        shift = 1
    for i in range(len(characters)):
        cipher[characters[i]] = characters[(i + shift) % 27]
        if characters[i] != ' ':
            cipher[characters[i].upper()] = characters[(i + shift) % 27].upper()
    print(cipher)
    return cipher

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. The cipher is
    defined by the shift value. Ignores non-letter characters like punctuation
    and numbers.
    """

def main():
    build_coder(3)

if __name__ == '__main__':
    main()