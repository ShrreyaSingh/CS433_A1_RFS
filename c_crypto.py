# Encryption - Decryption Layer

'''
Arguments:

data: Data to be encrypted or decrypted
crypt_mode: 1: plain, 2: substitute, 3: transpose
flag: decrypt: decrypt, encrypt: encrypt
'''


def encrypt(data, crypt_mode, flag, shift=2):

    data = data.decode()
    crypt_mode = int(crypt_mode.decode())
    flag = flag.decode()

    if (crypt_mode == 2):
        if (flag == "decrypt"):
            shift *= -1
        result = ""
        for i in range(len(data)):
            if (data[i].isupper()):
                result += chr((ord(data[i]) + shift - 65) % 26 + 65)
            elif (data[i].islower()):
                result += chr((ord(data[i]) + shift - 97) % 26 + 97)
            elif (data[i].isnumeric()):
                result += chr((ord(data[i]) + shift - 48) % 10 + 48)
            else:
                result += data[i]
        return result.encode()

    elif (crypt_mode == 3):
        result = "".join(reversed(data))
        return result.encode()

    else:
        return data.encode()
