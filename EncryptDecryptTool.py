from flask import Flask, request, render_template

app = Flask(__name__)


def tool(text, shift, mode='encrypt'):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    cipher = ''

    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            if mode == 'encrypt':
                cipher += shifted_alphabet[index]
            elif mode == 'decrypt':
                cipher += alphabet[shifted_alphabet.index(char)]
        else:
            cipher += char  # Non-alphabet characters are added as is

    return cipher

def main():
    choice = input("Do you want to encrypt or decrypt a message? (encrypt/decrypt): ").strip().lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-25): "))

    if choice == 'encrypt':
        encrypted_message = tool(message, shift, 'encrypt')
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = tool(message, shift, 'decrypt')
        print(f"Decrypted Message: {decrypted_message}")

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form['mode']

        if mode == 'encrypt':
            message = tool(text, shift, 'encrypt')
        elif mode == 'decrypt':
            message = tool(text, shift, 'decrypt')

    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)


