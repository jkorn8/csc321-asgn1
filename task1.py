from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main(filename):
    with open(filename, 'rb') as file:
        data = file.read(128)
        print(len(data))
        ascii_text = data.decode('ascii')
        print(ascii_text)
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_ECB)
        cipher_text = cipher.encrypt(data)
        print(cipher_text)


if __name__ == "__main__":
    main("text.txt")