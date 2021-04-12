# Raspberry Internet Watchdog

... but also for any other Linux-based system. Contains a script that monitors whether the Internet connection is working on your device. If not, restarts the router. If the problem persists, the device will restart. In this way, you will ensure the stability of access to your network and device in the event of a network failure.

## Requirements

- `Linux` based device (like `Raspberry Pi`) with installed `Python 3`
- One of the supported routers: `Cisco EPC3925`, `Nokia G-240W-C` or other with `OpenWrt` installed
- The following python packages installed on device: `http.client`, `requests`, `paramiko` (only for `Cisco EPC3925`)
- Access data to your device: login and password
- If you are using a router with OpenWrt, make sure it has SSH access and password enabled.
- The script saves the last restart date to a file in its location to avoid restart loops, so make sure it will have permission to write to that location

## Installation

Install required Python packages:

```bash
pip3 install http.client requests paramiko
```

Clone the repository to any directory on your device, e.g. to the home directory.

```bash
cd
git clone https://github.com/paulomac1000/Raspberry-Internet-Watchdog
```

Change to the script's directory

```bash
cd Raspberry-Internet-Watchdog
```

Configure the master script

```bash
nano watchdog.internet.py
```

Go to line 44 (to the code below) and uncomment the call to your router restart script

```python
# Uncomment line for Your router and update access data in selected file
#os.system('python3 Cisco_EPC3925.py')
#os.system('python3 Nokia_G-240W-C.py')
#os.system('python3 OpenWrt.py')
```

Close the file with `ctrl+x` and save changes.

Then configure the script that will restart your router:

### If you are using a `Cisco EPC3925` router:

Open script `Cisco_EPC3925.py`

```bash
nano Cisco_EPC3925.py
```

And set proper access data like url, login and password. The given data in the script is the default for routers provided by the Inea operator.

```python
url = "192.168.0.1"
username = "homeu"
password = "homep"
```

### If you are using a `Nokia G-240W-C` router:

Here, the matter is a bit more complicated. You need to get the authorization tokens generated by the router after logging in. Don't be discouraged, it's easy to get to them. Unfortunately, I couldn't rewrite the logic that generated them because it was using a package that is not available for `Python`.

Of course, if you use the Inea operator router with the default password, you don't need to change anything in the script. Otherwise:
- go to the login page of the router,
- open developer tools (F12 in chrome) and select the "Network" tab,
- check the `Preserve logs` checkbox in developer tools,
- log in to the router,
- find the request named `login.cgi` to the address `http://192.168.1.1/login.cgi` and go to it,
- at the very bottom you will see values for "Form Data", copy the value of the parameter `ct` and `ck`.

Open script `Nokia_G-240W-C.py`

```bash
nano Nokia_G-240W-C.py
```

And set proper access data like url, ct and ck. The given data in the script is the default for routers provided by the Inea operator.

```python
url = "192.168.1.1"
ct = "2Awp6Rntn24AtFDkwCioWarQFk734lYGf0lIz6EoJdv1E741j-_mChCqgJzmSby4OvHDpyTcIs87PeKeKxkEpRS7vYEoLFX3_LhVuF4fWE9SP8pfhR8I-jsynfwfpGDWqX5mXBClQgnjudj0_evkf0UJZYCaiZgmEI3G8OwV5BqP5nDreYL1RmS_9xNgfjdMu6LTALtiCqrg_0yi-XF4Kr8HAsK0UvDXugmk8nNoi8eDWk_ELGVwDcuJtxsRgbzN8yJXvqJD_Iqnf_A1G7yq7T9vLRCYb5loHljS5GGC7dI"
ck = "mqdh47u9tZ4pMNyMkK5bSOvEdN8XgeRwplu24qLG7fwDPRcxNPQMy0HVbp0sXb7cSqe6EUoEMIHt1btDghNp16AogCS531fNeBqT4Vt1bVnONu6cIash2yvjOCZtInruarFsuerxsxv8K7-80cYTvQKgdsqSUH2CZ0BSGH_D7yQ."
```

### If you are using other with `OpenWrt` installed

Open script `OpenWrt.py`

```bash
nano OpenWrt.py
```

And set proper access data like url, login and password. Make sure it has SSH access and password enabled.

```python
url = "192.168.1.1"
username = "root"
password = "password"
```

## Usage

To run a script, run it from the command line.

```bash
python3 watchdog.internet.py
```

For the script to run automatically, add it to the `crontab`.

```bash
crontab -e
```

And call script. The following command will run the script every 15 minutes.

```bash
*/15 * * * * python3 /home/pi/Raspberry-Internet-Watchdog/watchdog.internet.py
```


## Contributing
Pull requests are welcome. I would be very pleased if you add a script that reboots your router. For major changes, please open an issue first to discuss what you would like to change.

## Show your support

Please star this repository if this project helped you!

## License
[MIT](https://choosealicense.com/licenses/mit/)

## See also
Blog post on [cleverblog.pl](https://cleverblog.pl/?p=206)