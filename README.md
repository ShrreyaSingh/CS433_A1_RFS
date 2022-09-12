## CS433_A1_RFS
----

In this assignment, we developed a simple remote file system service (RFS) to understand the principles of layered network architecture. This RFS supports execution of the following commands:

* ``cwd``: Retrieve the path of the current working directory for the user
* ``ls``: List the files/folders present in the current working directory
* ``cd <dir_path>``: Change the directory to ``<dir_path>`` as specified by the client
* ``dwd <file_path>``: Download the ``<file_path>`` specified by the user on server to client
* ``upd<file_path>``: Upload the file present in ``<file_path>`` on client to the remote server in ``CWD``

The layered architecture is based on OSI model:

![alt text](images/OSI.png?raw=true)

* ``Layer N``: File Service Layer: On client side, it takes the user inputs for command execution, checks for bad requests and if the request is valid, propagates the data units to subsequent layers for encryption and servicing.

* ``Layer N-1``: Crypto Layer: Encrypts and decrypts the data using three functions before transmitting it further in the network:

  * Plain text → No change to the input; (No encryption or decryption)
  * Substitute → Only alphanumeric characters will be substituted with fixed offset, say Caesar cipher with offset 2. Example ARTZ will be substituted with CTVB
  * Transpose → Revere the contents in a word by word manner. Example ARTZ willbe substituted with ZTRA.

* ``Layer N-2``: Transport layer: Create and implement client and server sockets to establish a connection using TCP Protocol. The encrypted data is transmitted over the network wherein the client sends its request and server returns a response with appropriate status.

Code Execution
--------------------

* Fork and clone this repo into your local system. Change directory to the cloned repo directory ``CS433_A1_RFS``.
* In the command prompt, create a server socket by running ``s_trans.py`` using command ``python3 s_trans.py``, incase of python3. 
* Now, run ``c_app.py`` to get a list of valid commands. Enter any one of the commands in the terminal in the correct format.
* If the command is valid, a client socket will be created by ``c_trans.py``. 
* The data unit will be encrypted in the presentation layer according to the user defined encryption procedure (mentioned above). Kindly note that only valid integer numbers should be given as input to choose the encryption option.
* Encryption header (identifying the encryption type) is attached to the content and protocol data unit is sent over the network to the server side.
* On the server side, this service data unit is listened to by the socket of the server.
* It is decrypted and the service layer performs the necessary functions according to the commands entered by the user.
* The server's response is again encrypted and sent back to the client over the network, where it's decrypted and the message with the status flag is displayed in the terminal.
* Please note that, for ``dwd`` and ``upd``, the files to be downloaded should be present within ``server_files`` directory i.e. file_path should be like ``server_files/*`` and the ones to be uploaded should be present within ``client_files`` directory i.e. file_path should be like ``client_files/*``. The files will be downloaded to ``client_files`` folder and uploaded inside ``server_files`` folder.
