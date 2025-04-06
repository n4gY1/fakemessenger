from django.contrib import admin

from chat.models import ChatSettings, Chat

# Register your models here.
admin.site.register(ChatSettings)
admin.site.register(Chat)