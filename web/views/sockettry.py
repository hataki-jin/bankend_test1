import socket
import json
import pickle
import time

s = socket.socket()
try:
    s.connect(('192.168.1.185', 8000))
except:
    print("连接失败")
message = {
    "type": "event_message",  # 类里你发送消息的方法名
    "event_type": 1,
}
jsonmsg = json.dumps(message)
s.send(pickle.dumps(jsonmsg))
