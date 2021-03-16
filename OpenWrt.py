#!/usr/bin/env python3
import paramiko

url = "192.168.1.1"
username = "root"
password = "password"

def restart():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=url, username=username, password=password)
    s = ssh.get_transport().open_session()
    paramiko.agent.AgentRequestHandler(s)
    
    try:
        ssh.exec_command("sudo /sbin/reboot", get_pty=True)
        print("Restart success")
    except:
        print("Error restarting router")
    
try:
    restart()
except Exception as e:
    print(str(e))