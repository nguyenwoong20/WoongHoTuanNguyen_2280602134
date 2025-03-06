from flask import Flask, request, jsonify
from Cipher.Caeser import CaeserCipher
app = Flask(__name__)

#CAESER CIPHER ALGORITHM
caeser_cipher = CaeserCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caeser_cipher.encrpyt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    encrypted_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caeser_cipher.decrypt_text(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#main function
if __name__ == "__main__":
    app.run(host ="0.0.0.0", port = 50000, debug=True)