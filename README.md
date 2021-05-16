# Implementing Near Real-time or Scheduled Data Replication Framework using Parmiko

# Reference Architecture
![Alt text](/images/Screenshot_4_lat.jpg?raw=true "") 

The current scenario discusses real-time replication between two computes which can be in same network or in different networks, however this can be customized to work with multiple machines. The solution is tested on RHEL8 machine on IBM Cloud's VPC based network.

The private network can be either cloud-based network or on-prem data center network. Data can come from public Internet or generated by internal processes and stored on local disks or SAN volumes. This data can be replicated in real-time or scheduled for later replication depending on Individual requirements. The solution makes use of paramiko framework available in Python, the details of which are mentioned in below sections.  

The python replication service runs as systemd service on RHEL and starts automatically when OS is restarted. Any time data is loaded into landing zone, this service replicates it to other computes it is configured for. This service needs to be installed and confirmed on all participating peer machines for cross replication. This service will not replicate data which is currently downloading, in RHEL it has a **.filepart** extension and wait for it to completely download before action on it. The additional extensions (if any) can be added in the service code. 

This also talks about performance measurement for data transfer between two machines.

# Parmiko
Paramiko primarily supports POSIX platforms with standard OpenSSH implementations, and is most frequently tested on Linux and OS X. Windows is supported as well, though it may not be as straightforward. Details can be found in below git-hub link:

https://github.com/paramiko/paramiko

--------------------
# Meeting the Pre-requisites
Python Version : 3.6.8 <br/>
dnf install python3 <br/>
pip3 install schedule  <br/> 
pip3 install setuptools-rust <br/>
pip3 install wheel <br/>
pip3 install PyNaCl <br/>
pip3 install bcrypt <br/>
dnf install redhat-rpm-config gcc libffi-devel python3-devel openssl-devel cargo <br/>
pip3 install paramiko <br>
pip install loguru <br/>
## Make Pre-requisite directories
mkdir /upload <br/>
chmod 777 /upload <br/>
mkdir /archive <br/>
chmod 777 /archive <br/>

where upload directory is a landing zone and archive folder is where file is copied locally for further action. Similar directory structure should be created on remote machine(s) as well. 

## Service Setup
a) Copy schedule_test_every_two_min.py in /opt or directory of your choice (make sure to modify service file in this case). <br/>
b) Copy python-scheduler.service in /etc/systemd/system directory. <br/>
c) Run systemctl daemon-reload
d) Run systemd-analyze verify python-scheduler.service to ensure that file is correct. If it is correct it should not return any output. <br/>
e) Run systemctl enable python-scheduler.service to enable service to start automatically on system restart. <br/>
f) Run systemctl start python-scheduler.service <br/>
g) Run systemctl status python-scheduler.service to check the status of service. <br/>

## SSH Session Timeout
The ClientAliveInterval parameter specifies the time in seconds that the server will wait before sending a null packet to the client system to keep the connection alive.

On the other hand, the ClientAliveCountMax parameter defines the number of client alive messages which are sent without getting any messages from the client. If this limit is reached while the messages are being sent, the sshd daemon will drop the session, effectively terminating the ssh session.

Timeout value = ClientAliveInterval * ClientAliveCountMax

Example: <br/>
ClientAliveInterval  1200 <br/>
ClientAliveCountMax 3 <br/>

The Timeout value will be 1200 seconds * 3 = 3600 seconds. 
This is an equivalent of 1 hour, which implies that your ssh session will remain alive for idle time of 1 hour without dropping.

Alternatively, you can achieve the same result by specifying the ClientAliveInterval parameter alone.

ClientAliveInterval  3600

Once done, reload the OpenSSH daemon for the changes to come into effect.

## Performance Measurement
dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm <br/>
dnf install nload <br/>
nload -m <br/>
![Alt text](/images/Screenshot_1.jpg?raw=true "")
# nload commands
![Alt text](/images/Screenshot_2.jpg?raw=true "") <br/>
### Where <br/>
![Alt text](/images/Screenshot_3.jpg?raw=true "")

# Example Scenario - File is externally uploaded to virtual server ftom WinSCP and this will is replicated to second virtual server through python code
# Step1 - Uploading File 

After file transfer is started one can verify download speed as below <br/>
![Alt text](/images/Screenshot_1_lat.jpg?raw=true "") <br/>

One the upload is complete to first virtual server, python scheduler will replicate the data to second virtual server as shown below, one can not both outbound transfer rate on first server and inbound rate on second server  - <br/>

![Alt text](/images/Screenshot_2_lat.jpg?raw=true "")

The schedule will not initiate transfer during downloading process <br/>

![Alt text](/images/Screenshot_3_lat.jpg?raw=true "") <br/>

# Running Scheduler as Systemd Service
Copy python-scheduler.service in /etc/systemd/system directory.
![Alt text](/images/Screenshot_5_lat.jpg?raw=true "") <br/>

### Note: Entry Environment=PYTHONUNBUFFERED=1 in systemd service file ensures that the logging is not buffered and is real time. The logging is generated in /var/log/messages file

## Reference:
https://cryptography.io/en/3.4.5/installation.html <br/>
http://www.paramiko.org/installing.html#cryptography <br/>
https://www.programcreek.com/python/example/4561/paramiko.SSHClient <br/>
https://www.cyberciti.biz/faq/how-to-test-the-network-speedthroughput-between-two-linux-servers/ <br/>
https://www.cyberciti.biz/faq/linux-unix-test-internet-connection-download-upload-speed/ <br/>
https://phoenixnap.com/kb/linux-network-speed-test <br/>
https://www.cyberciti.biz/faq/linux-unix-test-internet-connection-download-upload-speed/ 
