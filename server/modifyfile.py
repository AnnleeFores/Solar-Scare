
import shutil
from datetime import date
from datetime import timedelta
import subprocess


today = date.today()
yesterday = today - timedelta(days = 1)
filename = yesterday.strftime("%d-%m-%Y")
print(filename)

    
def unzip():

    source = "/run/user/1000/gvfs/ftp:host=127.0.0.1/"+filename+".tar.xz"
    destination = "/home/annlee/solar-scare/server/dest"
    dest = shutil.move(source, destination)

    arcfilename ='~/solar-scare/server/dest/'+filename+'.tar.xz'
    extfolder = '~/solar-scare/server/unzipped'

    command = 'tar -xvzf '  + str(arcfilename)+ ' -C ' + str(extfolder)

    subprocess.call(command, shell=True)

def movefile():
    command = 'mv ~/solar-scare/server/unzipped/'+filename+'/*.wav ~/solar-scare/server/wingbeats_pi/test'
    subprocess.call(command, shell=True)
