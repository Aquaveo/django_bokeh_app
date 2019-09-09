from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler

from django.conf.urls import url

import sys
sys.path.append("..")

from bokehexample import views

from bokeh.server.django.consumers import WSConsumer, AutoloadJsConsumer
from bokeh.server.django import autoload


bokeh_app = autoload("bokehexample", views.shape_viewer_handler)
kwargs = dict(app_context=bokeh_app.app_context)

bokeh_app_with_variable = autoload(r'^bokehexample/<str:id>/autoload.js$', views.shape_viewer_handler)
kwargs_with_variable = dict(app_context=bokeh_app_with_variable.app_context)

ws_urls = [url(r'^bokehexample/ws$', WSConsumer, kwargs=kwargs),
           url(r'^bokehexample/<str:id>/ws$', WSConsumer, kwargs=kwargs_with_variable)]

http_urls = [url(r'^bokehexample/autoload.js$', AutoloadJsConsumer, kwargs=kwargs),
             url(r'^bokehexample/<str:id>/autoload.js$', AutoloadJsConsumer, kwargs=kwargs_with_variable),
             url(r'', AsgiHandler)]

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(ws_urls)
    ),
    'http': AuthMiddlewareStack(
        URLRouter(http_urls)
    ),
})
