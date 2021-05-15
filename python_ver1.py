# Schedule Library imported 
import schedule 
import time 
import shutil, os, fnmatch
import subprocess
import paramiko
import re
from pathlib import Path

dirPath="/upload"
dstDirPath="/archive"


# Functions setup 
def sudo_placement(): 
	print("Write Some Implementation") 

def good_luck(): 
	print("Write Some Implementation") 

def work(): 
	print("Write Some Implementation") 

def bedtime(): 
	print("Write Some Implementation") 
	
def geeks(): 
      try:
        path, dirs, files = next(os.walk(dirPath))
        file_count=len(files)
        print("Number of files:: ", file_count)
        if (file_count > 0): 
           for filename in os.listdir(dirPath):
              f=os.path.join(dirPath,filename)
              match=re.search("\.filepart$",f)
              print("RegEx Match file name:: ",f)
              print("RegEx Match:: ",match)
              if os.path.isfile(f) and  not f.endswith(".filepart"):
                  try:  
                    print("filename:", filename)  
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect('10.240.0.5', username='root', password='hadoop@123')
                    sftp = ssh.open_sftp()
                    dstPath=dstDirPath+"/"+filename
                    print("filename", filename)
                    print("filepath", f)
                    print("dstPath",dstPath)
                    sftp.put(f,dstPath)
                    sftp.close()
                    print("Uploaded Successsfully")
                    shutil.move(f, '/archive/'+filename) 
                  except AuthenticationException:
                      print("authentication failed")
                  except SSHException as sshException:
                      print("Unable to establish SSH connection")
                  except BadHostKeyException as badHostKeyException:
                      print("Unable to verify server's host key: %s" % badHostKeyException)
                  finally:
                      ssh.close()
        else:        
         print("File Transfer Not yet Initiated") 
      except FileNotFoundError:
            print("Directory: {0} does not exist".format(path))
      except NotADirectoryError:
            print("{0} is not a directory".format(path))
      except PermissionError:
            print("You do not have permissions to change to {0}".format(path))
# Task scheduling 
# After every 10mins geeks() is called. 
schedule.every(1).minutes.do(geeks) 

# After every hour geeks() is called. 
#schedule.every().hour.do(geeks) 

# Every day at 12am or 00:00 time bedtime() is called. 
#schedule.every().day.at("00:00").do(bedtime) 

# After every 5 to 10mins in between run work() 
#schedule.every(5).to(10).minutes.do(work) 

# Every monday good_luck() is called 
#schedule.every().monday.do(good_luck) 

# Every tuesday at 18:00 sudo_placement() is called 
#schedule.every().tuesday.at("18:00").do(sudo_placement) 

# Loop so that the scheduling task 
# keeps on running all time. 
while True: 

	# Checks whether a scheduled task 
	# is pending to run or not 
	schedule.run_pending() 
	time.sleep(1) 

