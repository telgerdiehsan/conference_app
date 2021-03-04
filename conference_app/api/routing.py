from django.urls import re_path
from . import consumers



websocket_urlpatterns = [
	re_path(r'ws/host',consumers.HostRoom),
	re_path(r'ws/join',consumers.JoinRoom)
]

