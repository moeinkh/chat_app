import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class Chat(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, 
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username_receiver = text_data_json['receiver']
        username_receiver_group = f'chat_{username_receiver}'
        print(text_data_json)

        async_to_sync(self.channel_layer.group_send)(
            username_receiver_group, 
            {
                'type': 'chat_message',
                'message': text_data_json,
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))