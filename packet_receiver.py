import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connecton with {address} has been established")
    clientsocket.send(bytes("Welcome!","UTF-8"))

    msg =clientsocket.recv(1024)
    print (msg.decode("UTF-8"))

    clientsocket.close()



address=""
msg=""

print("THe data received from "+address+ " is: " +msg)
print ("The data received has "+dataBits+" bits or "+dataBytes+" bytes. Total length of the packet is "+ totalBytes+" bytes.")

print ("The verification of the checksum demonstrates that the packet received is correct.")
print ("The verification of the checksum demonstrates that the packet received is corrupted. Packet discarded")