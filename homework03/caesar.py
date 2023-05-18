import typing as tp

small_letter_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
big_letter_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    letters = list(plaintext)
    for letter in letters:
        if not letter.isalpha():
            ciphertext += letter
            continue

        small_index_rus = small_letter_rus.find(letter)
        big_index_rus = big_letter_rus.find(letter)
        if small_index_rus != -1:
            small_index_rus += shift
            small_index_rus %= len(small_letter_rus)
            ciphertext += small_letter_rus[small_index_rus]
            continue
        if big_index_rus != -1:
            big_index_rus += shift
            big_index_rus %= len(big_letter_rus)
            ciphertext += big_letter_rus[big_index_rus]
            continue

        new_letter = ord(letter) + shift
        if letter.islower():
            while new_letter > 122:
                new_letter -= 26
            while new_letter < 97:
                new_letter += 26
        else:
            while new_letter > 90:
                new_letter -= 26
            while new_letter < 65:
                new_letter += 26
        ciphertext += chr(new_letter)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    return encrypt_caesar(ciphertext, -shift)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = -1
    flag = True
    while flag:
        best_shift += 1
        shift_word = decrypt_caesar(ciphertext, best_shift)
        for item in dictionary:
            if item == shift_word:
                flag = False
    return best_shift
