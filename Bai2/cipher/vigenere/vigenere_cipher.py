class VigenerCipher:
    def __init__(self):
        pass

    def vigener_encrypt(self, plain_text, key):
        encrypted_text = ''
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)]) - ord('A')
                key_index += 1
                if char.isupper():
                    char_shifted = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    char_shifted = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                encrypted_text += char_shifted
            else:
                encrypted_text += char
        return encrypted_text

    def vigener_decrypt(self, encrypted_text, key):
        decrypted_text = ''
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)]) - ord('A')
                key_index += 1
                if char.isupper():
                    char_shifted = chr((ord(char) - ord('A') - key_shift + 26) % 26 + ord('A'))
                else:
                    char_shifted = chr((ord(char) - ord('a') - key_shift + 26) % 26 + ord('a'))
                decrypted_text += char_shifted
            else:
                decrypted_text += char
        return decrypted_text