import logging
from bokeh.server.django.consumers import BokehAppWebsocketConsumer


log = logging.getLogger(__name__)


class CustomBokehAppWebsocketConsumer(BokehAppWebsocketConsumer):

    async def connect(self):
        log.info("CONNECTED")
        super().connect()
