import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from rest_framework.decorators import api_view

clients = {}  # 创建客户端列表，存储所有在线客户端


# class CConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # 从给consumer打开WebSocket连接的web/routing.py中的URL路由中获取"room_name"参数
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'client_%s' % self.room_name
#
#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'client_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     async def client_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))


class ClientConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 从给consumer打开WebSocket连接的web/routing.py中的URL路由中获取"client_name"参数
        self.client_name = self.scope['url_route']['kwargs']['client_name']
        self.room_group_name = 'camera_%s' % self.client_name

        print("连接成功")
        print(self.client_name)
        # Join camera group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['test']

        print(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'event_message',
                'message': "chengle"
            }
        )

    # Send event to front-end
    async def event_message(self, event):
        # message = "test websocket message"
        message = event['message']
        print('event_message')
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

# def send_group_msg(client_name, event_type, message):
#     # 从Channels的外部发送消息给Channel
#     """
#     from assets import consumers
#     consumers.send_group_msg('ITNest', {'content': '这台机器硬盘故障了', 'level': 1})
#     consumers.send_group_msg('ITNest', {'content': '正在安装系统', 'level': 2})
#     :param client_name:
#     :param message:
#     :return:
#     """
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         'camera_{}'.format(client_name),  # 构造Channels组名称
#         {
#             "event_type": event_type,
#             "message": message,
#         }
#     )

# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
#
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         # 从给consumer打开WebSocket连接的chat/routing.py中的URL路由中获取"room_name"参数
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
