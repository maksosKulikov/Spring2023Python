small_letter_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
big_letter_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
small_letter_en = "abcdefghijklmnopqrstuvwxyz"
big_letter_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_array = list(keyword.lower())
    shift_array = []
    for key in keyword_array:
        shift_array.append(ord(key) - 97)
    index_shift = 0
    for letter in list(plaintext):
        if not letter.isalpha():
            ciphertext += letter
        if letter in small_letter_rus:
            ciphertext += small_letter_rus[
                (small_letter_rus.find(letter) + shift_array[index_shift % len(shift_array)]) % 33]
        if letter in big_letter_rus:
            ciphertext += big_letter_rus[
                (big_letter_rus.find(letter) + shift_array[index_shift % len(shift_array)]) % 33]
        if letter in small_letter_en:
            ciphertext += small_letter_en[
                (small_letter_en.find(letter) + shift_array[index_shift % len(shift_array)]) % 26]
        if letter in big_letter_en:
            ciphertext += big_letter_en[(big_letter_en.find(letter) + shift_array[index_shift % len(shift_array)]) % 26]
        index_shift += 1
    return ciphertext


def decrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    ciphertext = ""
    keyword_array = list(keyword.lower())
    shift_array = []
    for key in keyword_array:
        shift_array.append(ord(key) - 97)
    index_shift = 0
    for letter in list(plaintext):
        if not letter.isalpha():
            ciphertext += letter
        if letter in small_letter_rus:
            ciphertext += small_letter_rus[
                (small_letter_rus.find(letter) - shift_array[index_shift % len(shift_array)]) % 33]
        if letter in big_letter_rus:
            ciphertext += big_letter_rus[
                (big_letter_rus.find(letter) - shift_array[index_shift % len(shift_array)]) % 33]
        if letter in small_letter_en:
            ciphertext += small_letter_en[
                (small_letter_en.find(letter) - shift_array[index_shift % len(shift_array)]) % 26]
        if letter in big_letter_en:
            ciphertext += big_letter_en[(big_letter_en.find(letter) - shift_array[index_shift % len(shift_array)]) % 26]
        index_shift += 1
    return ciphertext
