import string


def decrypt_text(cipher_text, key):
    decrypted_plaintext = ""
    for i in cipher_text:
        if i.isupper():
            abc = string.ascii_uppercase
        elif i.islower():
            abc = string.ascii_lowercase
        else:
            decrypted_plaintext += i
            continue
        position = abc.find(i)
        shifted_position = (position - int(key)) % 26
        plaintext_letter = abc[shifted_position]
        decrypted_plaintext += plaintext_letter

    return decrypted_plaintext


def run():
    cipher_text = input("Enter the Caeser cipher text: ")
    key = input("Enter the key: ")
    plaintext = decrypt_text(cipher_text, key)
    print("The decrypted message is " + plaintext)


if __name__ == '__main__':
    run()
