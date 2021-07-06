import ftplib
from datetime import date
from datetime import timedelta
import subprocess

HOSTNAME = "192.168.225.62"
USERNAME = "ftpuser"
PASSWORD = "pi"


ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

ftp_server.encoding = "utf-8"

today = date.today()
yesterday = today - timedelta(days = 1)
filename = yesterday.strftime("%d-%m-%Y")
print(filename)


file_to_archive = filename
output_filename = filename +'.tar.xz'

command = 'tar -czvf '  + str(output_filename)+ ' ' + str(file_to_archive)

subprocess.call(command, shell=True)


with open(output_filename, "rb") as file:
	ftp_server.storbinary(f"STOR {output_filename}", file)

ftp_server.dir()
ftp_server.quit()

