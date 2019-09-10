from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler

from django.conf.urls import re_path

import sys
sys.path.append("..")

from bokehexample import views

from bokeh.server.django.consumers import WSConsumer, AutoloadJsConsumer
from bokeh.server.django import autoload


bokeh_app = autoload("bokehexample", views.shape_viewer_handler)
kwargs = dict(app_context=bokeh_app.app_context)

bokeh_app_with_variable = autoload(r'^bokehexample/(?P<id>[0-9A-Za-z-_.]+)/autoload.js$', views.shape_viewer_handler)
kwargs_with_variable = dict(app_context=bokeh_app_with_variable.app_context)

ws_urls = [re_path(r'^bokehexample/ws$', WSConsumer, kwargs=kwargs),
           re_path(r'^bokehexample/(?P<id>[0-9A-Za-z-_.]+)/ws$', WSConsumer, kwargs=kwargs_with_variable)]

http_urls = [re_path(r'^bokehexample/autoload.js$', AutoloadJsConsumer, kwargs=kwargs),
             re_path(r'^bokehexample/(?P<id>[0-9A-Za-z-_.]+)/autoload.js$', AutoloadJsConsumer,
                     kwargs=kwargs_with_variable),
             re_path(r'', AsgiHandler)]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(ws_urls)
    ),
    'http': AuthMiddlewareStack(
        URLRouter(http_urls)
    ),
})
