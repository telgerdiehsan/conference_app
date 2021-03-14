from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class JoinRoom(WebsocketConsumer):

    def connect(self):
        self.accept()

    

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(self.user_id,self.channel_name)

    def receive(self,text_data):
        text_data = json.loads(text_data)

        self.user_id = text_data['user_id']
        room_id = text_data['room_id']
        offer = text_data['offer']
        async_to_sync(self.channel_layer.group_add)(self.user_id,self.channel_name)
        async_to_sync(self.channel_layer.group_send)(room_id,{'type':'send.offer','text':text_data,'user_id':self.user_id})
        self.send(text_data=json.dumps({'message':'offer sent'}))
    def user_response(self,event):
        self.send(text_data=json.dumps({'message':event['text']}))




class HostRoom(WebsocketConsumer):

    def connect(self):
        self.accept()

    
    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_id,self.channel_name)
        self.close()

    def receive(self,text_data):
        print(text_data)
        text_data = json.loads(text_data)
        print(text_data)
        print(text_data.keys())
        print(type(text_data))
        mode = text_data['mode']
        
        if mode == 'start': 
            self.room_id = text_data['room_id']
            async_to_sync(self.channel_layer.group_add)(self.room_id,self.channel_name)
            self.send(text_data=json.dumps({'message':'Your room has registered'}))
            return
        elif mode == 'offer_response':
            response = text_data['data']
            user_id = text_data['user_id']
            async_to_sync(self.channel_layer.group_send)(user_id,{'type':'user.response','text':response})

            
            
            

    def send_offer(self,event):
        self.send(text_data=json.dumps({'message':event['text'],'user_id':event['user_id'],'mode':'offer'}))
        
    