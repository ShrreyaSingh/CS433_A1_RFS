## Client Application Layer

import c_trans
import crypto

## Keep a variable check for bad requests
error = 0

full_cmd = input('''
Enter any one of the below commands:
CWD
LS
CD dir_path 
DWD server_file_path
UPD client_file_path 

------------------------------------------ 
''' )

# print('''
# Enter the number for the command to execute:
# 1 CWD
# 2 LS
# 3 CD 
# 4 DWD
# 5 UPD
# ''')

cmd_code = -1
# cmd_code = int(input())

full_cmd = full_cmd.split(' ')
# print(full_cmd[0].lower(),cmd_code)

if(full_cmd[0].lower().__eq__('cwd')):
    cmd_code = 1
elif(full_cmd[0].lower().__eq__('ls')):
    cmd_code = 2
elif(full_cmd[0].lower().__eq__('cd')):
    cmd_code = 3
elif(full_cmd[0].lower().__eq__('dwd')):
    cmd_code = 4
elif(full_cmd[0].lower().__eq__('upd')):
    cmd_code = 5
else:
    error = 1

# print(full_cmd[0],cmd_code)
cmd = ""
sep = '@@@'

# print("Error checkpoint 1: {}".format(error))
if(cmd_code==1):
    if(len(full_cmd)>1):
        error = 1
    cmd = '1' + sep + 'cwd' 

elif(cmd_code==2):
    if(len(full_cmd)>1):
        error = 1
    cmd = '2' + sep + 'ls'

elif(cmd_code==3):
    try:
        dir = full_cmd[1]
        cmd = '3' + sep + 'cd' + sep + dir
    except:
        error = 1       

elif(cmd_code == 4):
    try:
        filepath = full_cmd[1]
        cmd = '4' + sep + 'dwd' + sep + filepath 
    except:
        error = 1

elif(cmd_code == 5):
    try:
        filename = full_cmd[1]
        client_file = open(filename, "r")
        filedata = client_file.read()
        filename = filename.split('/')
        client_file.close()
        cmd = '5' + sep + 'upd' + sep + filename[-1] + sep + filedata
    except:
        error = 1

if(error):
    print("Invalid command!!!")
else:
    ## Encrypt cmd
    encrypt_code = input('''
Enter an integer to select the encryption type:
1 Plain 
2 Substitute
3 Transpose

---------------------------------------------------
''')
    sep2 = '^@^'

    if(int(encrypt_code) not in [1,2,3]):
        error = 1
    
    if(error):
        print("Invalid Command")
    else:
        ## Encrypt and establish connection
        encrypt_cmd = crypto.encrypt(cmd.encode(),encrypt_code.encode(),"encrypt".encode()) ## Returned in bytes
        request = encrypt_code + sep2 + encrypt_cmd.decode()

        print("\nSetting up connection ...")
        data, flag = c_trans.client_conn(request.encode())
        data = data.decode()
        flag = flag.decode()

        if(cmd_code==4):

            try:
                data_list = data.split(sep)
                filename = data_list[0]
                filedata = data_list[1]
                client_path = "client_files/"+filename
                client_file = open(client_path,"w+")
                client_file.write(filedata)

                client_file.close()
                data = filedata
            except:
                error = 1

        print("-------------------------------")
        print(f"Received: {data!r}")
        if(cmd_code in [3,4,5]):
            status = -1
            if(int(flag)==0):
                status = "NOK"
            elif(int(flag)):
                status = "OK"
            print("------------------------------- \nSTATUS: {}".format(status))


