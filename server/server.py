import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('Здесь происходить обработка перенаправленного url')
print('connected:', addr)
data = conn.recv(4096)
b = data.decode('utf-8').split(' ')[1]
url = f'http://localhost:9090' + b
conn.send(url)
conn.close()
print('connection close:')
print(url)
