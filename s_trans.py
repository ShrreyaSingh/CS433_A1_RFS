# Server Transport Layer

import socket
import s_app
import s_crypto


def server_conn():

    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 2500  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen()

        sep2 = '^@^'

        # Server is always kept on and accepts client requests whenever some client makes any request
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                cmd = conn.recv(2048)

                cmd = cmd.decode()
                if not cmd:
                    break

                # Decrypt
                cmd = cmd.split(sep2)
                encrypt_code = cmd[0]
                encrypt_cmd = sep2.join(cmd[1:])
                cmd = s_crypto.encrypt(encrypt_cmd.encode(
                ), encrypt_code.encode(), "decrypt".encode())
                # print("Server received request: {}".format(cmd.decode()))

                # Provide service
                data, flag = s_app.serve_client(cmd)
                response = flag.decode() + sep2 + data.decode()

                encrypt_response = s_crypto.encrypt(
                    response.encode(), encrypt_code.encode(), "encrypt".encode())
                encrypt_response = encrypt_code + sep2 + encrypt_response.decode()
                # print("Server sends response {}".format(encrypt_response))
                conn.sendall(encrypt_response.encode())


server_conn()
