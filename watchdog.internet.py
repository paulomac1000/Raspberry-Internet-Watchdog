#!/usr/bin/env python3
import http.client as httplib
import requests
import os
import time

RESTART_FILE_NAME = 'restarts.csv'
RESTART_DATE_FORMAT = '%d/%m/%Y %H:%M:%S'

def getLastRestart():
    try:
        f = open(RESTART_FILE_NAME)
        lines = f.read().splitlines()
        last_line = lines[-1]
        return datetime.strptime(last_line, RESTART_DATE_FORMAT)
    except Exception:
        return datetime.min
    finally:
        try:
            f.close()
        except: 
            pass
        
def putRestartTimespan():
    with open(RESTART_FILE_NAME, 'a') as f:
        f.write("\n" + datetime.now().strftime(RESTART_DATE_FORMAT))
        f.close()

def haveInternet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
        
def doWork():
    print("Starting watchdog.internet.py script")
    if haveInternet():
        print("Internet working")
    else:
        # Uncomment line for Your router and update access data in selected file
        #os.system('python3 Cisco_EPC3925.py')
        #os.system('python3 Nokia_G-240W-C.py')
        #os.system('python3 OpenWrt.py')
        
        print("restarted succesfully, waiting 120s")
        time.sleep(120)

        if haveInternet():
            print("Internet working")
        else:
            lastRestart = getLastRestart()
            lastRestartFromNow = (datetime.now() - lastRestart)
            
            if lastRestartFromNow.total_seconds() < 60*60:
                print("Device has already been restarted within the last hour, skipping")
            else:
                print("Internet still not working, restarting device")
                putRestartTimespan()
                os.system("sudo reboot")

try:
    doWork()
except Exception as e:
    print(str(e))
    pass