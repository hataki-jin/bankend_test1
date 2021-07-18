from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()
group_name = 'camera_client'
# channel 内部会自动把 . 转化成 _ 
async_to_sync(channel_layer.group_send)(group_name, {"type": "event.message", "message": "hello ajdskakffjsdfjkadskdg"})
