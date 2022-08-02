
import  socket
import  base64
import  threading
import time

client_list=[]

s1=socket.socket()
s1.bind(("127.0.0.1",996))
s1.listen(5)


def print_list():
    while True:
        time.sleep(3)
        print(client_list)

        if(len(client_list)>=1):
            client_list[0].send("这是服务器主动发送数据".encode())

thread1=threading.Thread(name="t1",target=print_list)
thread1.start()


while 1:
    conn,adress=s1.accept()
    if(conn not in client_list):
        client_list.append(conn)
    print("{}建立链接".format(adress))

