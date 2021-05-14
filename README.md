## python_scheduler
## Python Scheduler
--------------------
# Meeting the Pre-requisites
dnf install python3 <br/>
pip3 install schedule --user <br/> 
pip3 install setuptools-rust <br/>
pip3 install wheel <br/>
pip3 install PyNaCl <br/>
pip3 install bcrypt <br/>
dnf install redhat-rpm-config gcc libffi-devel python3-devel openssl-devel cargo <br/>
pip3 install paramiko <br>

## Make Pre-requisite directories
mkdir /upload <br/>
chmod 777 /upload <br/>
mkdir /archive <br/>
chmod 777 /archive <br/>

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
## Reference:
https://cryptography.io/en/3.4.5/installation.html <br/>
http://www.paramiko.org/installing.html#cryptography <br/>
https://www.programcreek.com/python/example/4561/paramiko.SSHClient
