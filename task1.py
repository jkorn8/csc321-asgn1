from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main(filename):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)


if __name__ == "__main__":
    main("text.txt")