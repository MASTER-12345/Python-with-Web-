import  socket

client=socket.socket()
client.connect(("127.0.0.1", 996))

while True:
    res=client.recv(1000000000)
    if(res!=None):
        print(res.decode())
