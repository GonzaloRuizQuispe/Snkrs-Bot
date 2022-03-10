from ipaddress import ip_address
import socket

#Nombre PC
hostname = socket.gethostname()
print(hostname)

#IP Addres
ip_address1 = socket.gethostbyname(hostname)
print(ip_address1)