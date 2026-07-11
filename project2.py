def encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char

    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)

print("---------------------------------------------")
print("---------------------------------------------")
print(" 🔒TEXT ENCRYPTION AND DECRYPTION SYSTEM🔓 ")
print("---------------------------------------------")
print("---------------------------------------------")

while True:
    text = input("\nEnter the text to Encrypt: ")
    shift = int(input("Enter the shift key: "))

    encrypted = encrypt(text, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nThe Encrypted message is:", encrypted)
    print("The Decrypted message is:", decrypted)

    choice = input(
        "\nWant to continue Encryption / Decryption (Y/N): "
    ).upper()

    if choice != "Y":
        print("\nThank you.")
        break
