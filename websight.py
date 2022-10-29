#File for running connection website
import network
import socket
import time
import ujson
import html
import WIFI
def sight():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)



    status = True
    while status:
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            request = cl.recv(1024)
            request = request.decode('utf-8' )
            thing = request.split('\n')
            print(request)
            if request[0] == 'P':
                params = thing[len(thing)-1].replace('&', '=')
                params = params.split('=')
                print(params)
            #JSON_data = ujson.loads(request)
    #         data = cl.recv(1024).decode('utf-8')  
    #         request = ujson.load(data)  

    #        request = (str(request))

            if request.find("/connect") != -1:
                stat = "Connecting"
                responce = html.con
                cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                cl.send(responce)
                WIFI.write(params[1],params[3])
                if WIFI.connect():
                    stat = "Connected"
                    responce = html.succ
                    cl.send(responce)
                    status = False
            else:
                responce = html.index
                cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                cl.send(responce)


            cl.close()

        except OSError as e:
            cl.close()
            print('connection closed')

