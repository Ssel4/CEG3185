import sys
import socket


def calculateCheckSum(header):
    hexadecimal_sum = lambda a,b : hex(int(a, 16) + int(b, 16))
    hexadecimal_sub = lambda a,b : hex(int(a, 16) - int(b, 16))
    checksum="0"
    tmp=""
    for i in header:
        tmp=tmp+i
        if len(tmp)==4:
                checksum = hexadecimal_sum(checksum,tmp)[2:]
                tmp=""
        
    if len(checksum)>4:
        tmp=checksum[0]
        checksum=checksum[1:]
        checksum = hexadecimal_sum(checksum,tmp)[2:]
    
    checksum= hexadecimal_sub("ffff",checksum)[2:]
    return checksum

stringPayload = "COLOMBIA 2 - MESSI 0"
hexPayload=stringPayload.encode("utf-8").hex()
print("Payload in hex: "+ hexPayload)

stringHeader = "4500 0028 1c46 4000 4006 0000 C0A8 0003 C0A8 0001" 
stringHeader=stringHeader.replace(" ","")
print ("header in string without spaces "+ stringHeader)

checkSum=calculateCheckSum(stringHeader)
print("checksum: "+calculateCheckSum(stringHeader))

stringHeader = stringHeader.replace("0000",checkSum)

print("header with new checksum: "+ stringHeader)

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

msg =s.recv(1024)
print (msg.decode("UTF-8"))

s.sendall(b"hello world")




#correctDataStream ="4500 0028 1c46 4000 4006 9D35 C0A8 0003 C0A8 0001 434f 4c4f 4d42 4941 2023 202d 204d 4553 5349 2030"
#print(correctDataStream)
#print(sys.argv)