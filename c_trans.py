# Client Transport Layer

import socket
import c_crypto


def client_conn(cmd):

    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 2500  # The port used by the server
    sep2 = '^@^'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))
        arr = bytes(cmd.decode(), 'utf-8')
        arr2 = bytes(cmd.decode(), 'ascii')
        # print("\nClient Request Encrypted String: {}".format(cmd.decode()))
        # print("\nHex string = {}".format(cmd.hex()))
        s.sendall(cmd)  # Encoded and encrypted

        response = s.recv(2048)
        # print("\nServer Response Encrypted String: {}".format(response.decode()))
        # print("\nHex string = {}".format(response.hex()))

        # Decrypt response
        response = response.decode().split(sep2)

        encrypt_code = response[0]
        encrypt_response = sep2.join(response[1:])

        response = c_crypto.encrypt(
            encrypt_response.encode(), encrypt_code.encode(), "decrypt".encode())
        response = response.decode().split(sep2)
        flag = response[0]
        data = response[1]

        # Decode date, decrypt it

    # Send error flag, msg to app layer in encoded form
    print("\nConnection closed :)")
    return data.encode(), flag.encode()


# client_conn()
