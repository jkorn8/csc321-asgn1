from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main(filename):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = b''
    with open(filename, 'rb') as file:
        while True:
            data = file.read(128)
            if not data:
                break
            print(len(data))
            ascii_text = data.decode('ascii')
            print(ascii_text)
            cipher_text += cipher.encrypt(data)
    print(cipher_text)



if __name__ == "__main__":
    main("text.txt")