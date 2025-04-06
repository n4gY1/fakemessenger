"""
URL configuration for fakemessenger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from chat.views import create_chat_settings, create_chat, show_fb_message
from fakemessenger import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',create_chat_settings,name="create_chat_settings"),
    path('create_chat/',create_chat,name="create_chat"),
    path('show_fb_message/',show_fb_message,name="show_fb_message"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
