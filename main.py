import pysftp

Hostname = "xxxxxxxxxxxx"
Username = "xxxxxxxx"
Password = "xxxxxxxxxx"
with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
    print("Connection successfully established ... ")
# Switch to a remote directory
    sftp.cwd('/')
    # sftp.cwd('/wwww')

# Obtain structure of the remote directory '/opt'
    directory_structure = sftp.listdir_attr()

# Print data
for attr in directory_structure:
    print(attr.filename, attr)