from channels.generic.websocket import AsyncWebsocketConsumer
import json
connected_users = {}
class CallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        self.socket_id = self.channel_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        # Notify others of new peer
        if self.room_name not in connected_users:
	    connected_users[self.room_name] = {}
        connected_users[self.room_name][self.socket_id] = self.channel_name
	# Send List of peers to new user
	await self.send(text_data=json.dumps({
	'type':'peers',
	'peers': [sid for sid in connceted_users[self.room_name] if sid != self.socket_id]

}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        if self.room_name in connected_users:
	    connected_users[self.room_name].pop(self.socket_id, None)
    
    async def receive(self, text_data):
        data = json.loads(text_data)
	target = data.get('target')
	message = data
        message['sender'] = self.socket_id

	# Send directly to target user
	if target:
	    target_channel = connected_users[self.room_name].get(target)
	    if target_channel:
	        await self.channel_layer.send(target_channel, {
			'type':'send.sdp',
			'message': message
})
	else:
	    # For broadcasting join or chat
	    await self.channel_layer.group_send(self.room_group_name, {
	    'type':'broadcast',
	    'message': message

})
    async def send_sdp(self, event):
        await self.send(text_data=json.dumps(event['message']))

    async def broadcast(self, event):
        if event['message']['sender'] != self.socket_id:
            await self.send(text_data=json.dumps(event['message']))



