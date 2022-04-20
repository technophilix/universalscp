import pysftp
import json
with open("credinfo.json", 'r') as infile:
          config = json.load(infile)

# print(config["user"][0]["ip"])          


Hostname = config["user"][0]["ip"]
Username = config["user"][0]["username"]
Password = config["user"][0]["password"]
with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
    print("Connection successfully established ... ")
# Switch to a remote directory
    sftp.cwd('/')
    sftp.cwd('/www')

# Obtain structure of the remote directory '/opt'
    directory_structure = sftp.listdir_attr()

# Print data
for attr in directory_structure:
    print(attr.filename, attr)