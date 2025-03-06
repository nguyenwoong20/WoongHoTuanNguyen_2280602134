from Cipher.Caeser.alphabet import ALPHABET

class CaeserCipher:
    def __init__(seft):
        seft.alphabet = ALPHABET
        
    def encrpyt_text(self, text: str, key: int) -> str:
        ALPHABET_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % ALPHABET_len
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)
                
        return "".join(encrypted_text)
        
    def decrypt_text(self, text: str, key: int) -> str:
        ALPHABET_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []        
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % ALPHABET_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
                
        return "".join(decrypted_text)
        
        