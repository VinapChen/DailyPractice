import socket, ssl, pprint,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# require a certificate from the server
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="./client.crt",
                           cert_reqs=ssl.CERT_REQUIRED)
ssl_sock.connect(('182.92.1.50', 8898))

pprint.pprint(ssl_sock.getpeercrert())