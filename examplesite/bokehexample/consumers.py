import logging
from bokeh.server.django.consumers import BokehAppWebsocketConsumer


log = logging.getLogger(__name__)


class CustomBokehAppWebsocketConsumer(BokehAppWebsocketConsumer):
    """
    This is meant to illustrate that the Bokeh consumer could be overridden to add custom behavior.
    """

    async def connect(self):
        log.info("CONNECTED")
        super().connect()
