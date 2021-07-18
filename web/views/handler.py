import socket
from threading import Thread
import socketserver
import json
import pickle
import time

server = None
conn_pool = []
port = 2077
host = '127.0.0.1'
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# channel 内部会自动把 . 转化成 _
# async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message", "message": "hello ajdskakffjsdfjkadskdg"})

conn_poll = []


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        group_name = 'camera_client'
        print('... connected from {}'.format(self.client_address))
        conn_poll.append(self.client_address)
        while True:
            try:
                # channel_layer = get_channel_layer()

                print('waiting')
                data = self.request.recv(1024)
                temp = pickle.loads(data)
                msg_cv = json.loads(temp)
                print(msg_cv)
                if msg_cv['type'] == 0:
                    conn_pool.remove(self.request)
                    self.request.send(data)
                    print('下线了')
                    break
                elif msg_cv['type'] == 1:
                    print('交互')
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "interact"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 2:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "fall"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 3:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "refresh"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 4:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "stranger"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 5:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "angry"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 6:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "disgust"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 7:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "fear"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 8:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "smile"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 9:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "natural"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 10:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "sad"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 11:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "surprise"})
                    self.request.send(pickle.dumps('recieved'))
                elif msg_cv['type'] == 12:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message",
                                                                         "message": "falling"})
                    self.request.send(pickle.dumps('recieved'))
                else:
                    self.request.sendall('[{}] {}'.format(time.ctime(), data.decode('utf-8')).encode('utf-8'))
            except Exception as e:
                print(e)

    def finish(self):
        print('finish')


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('', port), MyServer)
    print('waiting')
    s.serve_forever()

'''

def handle_client():
    while True:
        client, addr = server.accept()
        print(addr)
        conn_pool.append(client)
        t = Thread(target=message_handle, args=(client,))
        t.setDaemon(True)
        t.start()

def message_handle(client):
        while True:
            print('waiting')
            data = client.recv(1024)
            temp=pickle.loads(data)
            msg_cv=json.loads(temp)
            print(msg_cv)
            if msg_cv['type'] == 'exit':
                conn_pool.remove(client)
                client.send(data)
                print('下线了')
                break
            elif msg_cv['type']=='event':
                print('title')
                print(msg_cv['title'])
                if msg_cv['title']=='陌生人出现':
                    print('陌生人出现'+msg_cv['time'])
                    client.send('recieved')
            client.send(data)

def main():
    global server, conn_pool
    server = socketserver.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(10)
    print("服务端已启动，等待客户端连接...")

    t = Thread(target=handle_client)
    t.setDaemon(True)
    t.start()
    while True:
        cmd = input("请输入操作：")
        if cmd == '':
            continue
        if int(cmd) == 1:
            print("--------------------------")
            print("当前连接数：", len(conn_pool))
        if cmd == 'exit':
            exit()


'''
