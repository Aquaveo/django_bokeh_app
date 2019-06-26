from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.conf.urls import url
import sys
sys.path.append("..")
from bokehexample.consumers import CustomBokehAppWebsocketConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url(r'^bokehexample/ws$', CustomBokehAppWebsocketConsumer),
        ])
    )
})
