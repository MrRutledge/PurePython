import socket

msock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
msock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
msock.send(cmd)


while True:
    data = msock.recv(512)
    if (len(data)<1):  break
    print(data.decode())
msock.close()