#File for handling wifi connections
import network
import socket
import time
ap = 3
def con(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    return wlan.isconnected()

def write(ssid,password):
    file = open("secrets.txt", "w")
    file.write(f"{ssid}\n")
    file.write(f"{password}\n")
    file.close()

def connect():
    file = open("secrets.txt", "r")
    content = (file.read()).split("\n")
    file.close()
    return con(content[0].strip(),content[1].strip())
    
def AP_connect():
    ssid = 'Lumi'
    password = '123456789'

    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)
    status = ap.ifconfig()
    print( 'ip = ' + status[0] )
    
def AP_disconnect():
    ap.disconnect()
        


