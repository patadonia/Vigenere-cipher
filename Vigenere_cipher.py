#функция для создания таблицы Виженера
def create_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere_table = {}
    for i in range(len(alphabet)):
        row = alphabet[i:] + alphabet[:i]
        vigenere_table[alphabet[i]] = row
    return vigenere_table
    
#функция для шифровки    
def encrypt(unencrypted_text, key):
    unencrypted_text = unencrypted_text.upper()
    key = key.upper()
    vigenere_table = create_vigenere_table()
    encrypted_text = ''
    key_index = 0

    for i in range(len(unencrypted_text)):
        if unencrypted_text[i].isalpha():
            encrypted_text += vigenere_table[key[key_index % len(key)]][ord(unencrypted_text[i]) - 65]
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += unencrypted_text[i]

    return encrypted_text

#функция для дешифровки
def decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    vigenere_table = create_vigenere_table()
    decrypted_text = ''
    key_index = 0

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            decrypted_text += chr((vigenere_table[key[key_index % len(key)]].index(cipher_text[i]) + 65) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += cipher_text[i]

    return decrypted_text

#консольный ввод и вывод
def main():
    choice = input("Для шифровки слова введите '1', для расшифровки введите '2' : ").upper()

    if choice == '1':
        message = input("Введите слово на английском: ")
        key = input("Введите ключ на английском: ")
        resalt_en = encrypt(message, key)
        print("Результат:", resalt_en)

    elif choice == '2':
        resalt_en = input("Введите слово на английском: ")
        key = input("введите ключ на английском: ")
        resalt_dec = decrypt(resalt_en, key)
        print("результат:", resalt_dec)


if __name__ == "__main__":
    main()
    
    