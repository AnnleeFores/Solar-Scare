       
# Import Module
import ftplib

# Fill Required Information
HOSTNAME = "192.168.225.62"
USERNAME = "ftpuser"
PASSWORD = "pi"

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

#add zipping function here

# Enter File Name with Extension
filename = "filename"

# Read file in binary mode
with open(filename, "rb") as file:
        # Command for Uploading the file "STOR filename"
        ftp_server.storbinary(f"STOR {filename}", file)

ftp_server.dir()
# Close the Connection
ftp_server.quit()

