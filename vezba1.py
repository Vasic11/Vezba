import socket

c = socket.socket()

c.connect(("localhost",80))

c.send(b"POST /dovla.php HTTP/1.1\r\nHost: localhost\r\nContent-type: aplication/x-www-form-urlencoded\r\nContetn-Lenght: 5\r\n\r\ndovla=ricma&a=10")

print(c.recv(1024))