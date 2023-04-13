from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main(filename):
    with open(filename, 'rb') as file:
        data = file.read(128)
        value = int.from_bytes(data, byteorder='big', signed=False)
        print(hex(value))
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_ECB)


if __name__ == "__main__":
    main("text.txt")