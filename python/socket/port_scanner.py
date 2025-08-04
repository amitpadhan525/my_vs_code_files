import socket
ip=input("Enter targeted IP :")
for port in range(1,65535):
    s=socket.socket()
    s.settimeout(0.1)
    result=s.connect_ex((ip,port))
    if result==0:
      print(f"port {port} open")
    s.close()