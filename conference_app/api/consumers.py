from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class HostRoom(WebsocketConsumer):



    def connect(self):

        self.accept()

    
    def disconnect(self,close_code):
        # async_to_sync(self.channel_layer.group_discard)('test_channel',self.channel_name)
        self.close()

    def receive(self,text_data):

        text_data = json.loads(text_data)
        print(text_data)
        room_id = text_data['room_id']
        start = text_data['start']
        
        if start: 
            async_to_sync(self.channel_layer.group_add)(room_id,self.channel_name)
            self.send(text_data=json.dumps({'message':'Your room has registered'}))
            return
        else:

            offer_response = 'sample'
            print("HEREE"*20)
            async_to_sync(self.channel_layer.send)('offer',{'type':'offer_responce','data':'n'})
            

        # print(self.channel_name)
        # # a = get_channel_layer()
        # # # out = async_to_sync(a.send)(self.channel_name,{'type':'snd.msg','text':'Hello'})
        # # print(out)
        # self.send(text_data=json.dumps({'message':'received'}))
        # async_to_sync(get_channel_layer().send)('test_channel',{'type':'n','message':'b'})
        # # if text_data['step']==0:
        # #     self.send(text_data=json.dumps({'message':'Second received'}))
        # pass

    def send_offer(self,event):
        self.send(text_data=json.dumps({'message':event['text']}))
        
    