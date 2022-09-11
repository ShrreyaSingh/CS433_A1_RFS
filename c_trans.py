## Client Transport Layer

import socket
import crypto

def client_conn(cmd):

    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 2500  # The port used by the server
    sep2 = '^@^'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))
        # print("Client Request: {}".format(cmd.decode()))
        s.sendall(cmd) ## Encoded and encrypted

        response = s.recv(2048)
        
        ## Decrypt response
        response = response.decode().split(sep2)
        encrypt_code = response[0]
        encrypt_response = sep2.join(response[1:])

        response = crypto.encrypt(encrypt_response.encode(),encrypt_code.encode(),"decrypt".encode())
        # print("Client received Response: {}".format(response.decode()))
        response = response.decode().split(sep2)
        flag = response[0]
        data = response[1]

        ## Decode date, decrypt it


    ## Send error flag, msg to app layer in encoded form
    print("\nConnection closed :)")
    return data.encode(),flag.encode()


# client_conn()