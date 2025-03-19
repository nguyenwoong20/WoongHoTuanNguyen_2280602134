from flask import Flask, render_template, request, json
from Cipher.Caeser import CaeserCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router routes for caesar cipher
@app.route("/caesar")
def caeser():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caeser_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caeser = CaeserCipher()
    
    encrypted_text = Caeser.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caeser_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caeser = CaeserCipher()
    
    decrypted_text = Caeser.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
