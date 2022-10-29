#Main File for executing commands

import network
import socket
import time
import ujson
import html
import WIFI
import website
import colorwave as light
import discord
import colors
import _thread
con = False
def blink():
    global con
    light.fade_out()
    light.fill((255,0,0))
    while con == False:
        if con == False:
            light.fade_in()
        if con == False:
            time.sleep(0.5)
        if con == False:
            light.fade_out()
        if con == False:
            time.sleep(0.5)

#_thread.start_new_thread(blink, ())

if WIFI.connect() == False:
    WIFI.AP_connect()
    website.sight()

current = (255, 150, 0)   
command = "YELLOW"
baton = _thread.allocate_lock()



def morse():
    global color
    
    baton.acquire()
    text = command.strip("MORSE")
    print(text)
    c = color
    text = text.split(" ")
    while color == c:
        
        for let in text:
            for part in let:
                wait = 0
                print(part)
                if part == '.':
                    wait = 1
                    print("in .")

                elif part == '-' or part == '_':
                    wait = 3
                    print("in -")
                else:
                    break

                light.fill(current)
                time.sleep(wait)
                light.fill((0,0,0))
                print("black")
                time.sleep(1)
            time.sleep(2)
    baton.release()
                
def rainbow():
    global color
    baton.acquire()

    while color =="RAINBOW":
        for j in range(255):
            if color == "RAINBOW":
                light.rainbow_cycle(0.05,j)
            else:
                break
    baton.release()
def err():
    for i in range(2):
        light.fill((255,0,0))
        time.sleep(0.5)
        light.fill((0,0,0))
        time.sleep(0.5)
    light.fill(current)
def parseCom():
    global color
    global current
    global command
    if color.find("GRADIENT") != -1:
        col = color.split(" ")
        light.gradient(col[1],col[2])
        command = "GRADIENT" +" " + colors.Tuple(colors.readColor(col[1])) +" " + colors.Tuple(colors.readColor(col[2]))
        current = colors.readColor(col[1])

    elif color.find("SEND") !=-1:
        discord.send(discord.URL_POST_G,command)
        
    elif color.find("SAVE") !=-1:
        color = color.split(" ")
        if len(color) == 3:
            colors.write(color[2],current)
        if len(color) == 2:
            colors.write(color[1],current)
        
    elif color == ("RAINBOW"):
        command = color
        while(baton.locked()):
             time.sleep(0.1)
        _thread.start_new_thread(rainbow, ())
    
    elif color.find("MORSE") != -1:
        command = color
        while(baton.locked()):
             time.sleep(0.1)
        _thread.start_new_thread(morse, ())
    
    elif color.find("OFF") != -1:
        light.fade_out()
    
    elif color.find("ON") != -1:
        light.fade_in()
    else:
        col = colors.readColor(color)
        if col == 1:
            err()
        else:
            light.fill(col)
            command = colors.Tuple(col)
            current = col

color = discord.getData(discord.URL_GET_G)
color = color.upper()
print(color)
con = True
#light.fade_in()
parseCom()
discord.start()
while True:
    m = discord.getData(discord.URL_GET_G)
    if m == 'none':
        m = discord.getDataS()
    if m!='none' and m!=color:
        color = m

        color = color.upper()
        print(color)
        parseCom()




