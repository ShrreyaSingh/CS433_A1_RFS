# Server Application Layer
import os


def serve_client(request):

    sep = '@@@'
    request = request.decode()
    request = request.split(sep)
    cmd_code = int(request[0])

    if (cmd_code == 1):
        # cwd
        try:
            return os.getcwd().encode(), "1".encode()
        except:
            return "Error in returning current directory".encode(), "0".encode()

    if (cmd_code == 2):
        ## ls or os.listdir
        try:
            return str(os.listdir()).encode(), "1".encode()
        except:
            return "Error in returning file list".encode(), "0".encode()

    if (cmd_code == 3):
        # Change dir
        try:
            path = request[2]
            os.chdir(path)
            return "Directory changed successfully".encode(), "1".encode()
        except:
            return "Error in changing directory".encode(), "0".encode()

    if (cmd_code == 4):
        # Download
        try:
            filename = request[2]
            server_file = open(filename, "r")
            server_data = server_file.read()
            filename = filename.split('/')
            server_data = filename[-1] + sep + server_data

            server_file.close()

            return server_data.encode(), "1".encode()
        except:
            return "Download Failed".encode(), "0".encode()

    if (cmd_code == 5):
        # Upload
        try:
            filename = request[2]
            filedata = request[3]

            server_path = filename
            server_file = open(server_path, "w+")
            server_file.write(filedata)

            server_file.close()

            return server_path.encode(), "1".encode()
        except:
            return "Upload Failed".encode(), "0".encode()
