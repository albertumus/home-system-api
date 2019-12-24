from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class TemperaturaConsumer(WebsocketConsumer):
    def connect(self):
        self.info = "Temperatura"
        self.sensor = "Temperatura"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.info,
            self.sensor
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.info,
            self.sensor
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.sensor,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))