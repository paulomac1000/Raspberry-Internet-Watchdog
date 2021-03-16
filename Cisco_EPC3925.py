#!/usr/bin/env python3
import requests

# the following data are for the router from the operator inea - homeu:homep

url = "192.168.0.1"
username = "homeu"
password = "homep"

def restart():
    print("Trying to login to router")
    
    loginUrl = 'http://' + url + '/goform/Docsis_system';
    loginBody = {
        'username_login': username,
        'password_login': password,
        'LanguageSelect': 'en',
        'Language_Submit': '0',
        'login': 'Log In'
    }

    loginHeaders = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://' + url + '/Docsis_system.asp'
    }

    try:
        response = requests.post(loginUrl, data = loginBody, headers = loginHeaders)
        print("Login response code " + str(response.status_code))
    except:
        print("Error login to system")

    print("Trying to restart router")

    restartUrl = 'http://' + url + '/goform/Devicerestart';
    restartBody = {
        'mtenRestore': 'Device Restart',
        'devicerestart': '1'
    }
    restartHeaders = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://' + url + '/Devicerestart.asp'
    }

    try:
        response = requests.post(restartUrl, data = restartBody, headers = restartHeaders)
        print("Restart response code " + str(response.status_code))
    except:
        print("Error restarting router")   

try:
    restart()
except Exception as e:
    print(str(e))