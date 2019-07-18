##################################################################################################
## credit to http://muharremdemiray.blogspot.com/2018/03/star-wars-asciimation-with-python.html ##
##################################################################################################
import socket

def start_movie():
    addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
    addr = addr_info[0][-1]
    s = socket.socket()
    s.connect(addr)
    while True:
        data = s.recv(500)
        print(str(data, 'utf8'), end='')