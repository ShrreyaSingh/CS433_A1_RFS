CS433_A1_RFS
-----------------

In this assignment, we developed a simple remote file system service (RFS) to understand the principles of layered network architecture. This RFS supports execution of the following commands:

* ``cwd``: Retrieve the path of the current working directory for the user
* ``ls``: List the files/folders present in the current working directory
* ``cd <dir_path>``: Change the directory to ``<dir_path>`` as specified by the client
* ``dwd <file_path>``: Download the ``<file_path>`` specified by the user on server to client
* ``upd<file_path>``: Upload the file present in ``<file_path>`` on client to the remote server in ``CWD``

The layered architecture is based on OSI model:

