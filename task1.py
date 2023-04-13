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
            padded_data = add_padding(data)
            print(len(padded_data))
            print(padded_data)
            ascii_text = data.decode('ascii')
            print(ascii_text)
            cipher_text += cipher.encrypt(padded_data)
    print(cipher_text)


def add_padding(data):
    missing_len = 128 - len(data)
    data = data + bytes(missing_len * chr(missing_len), 'utf-8')
    return data


if __name__ == "__main__":
    main("text.txt")
