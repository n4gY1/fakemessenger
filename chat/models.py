from django.db import models

# Create your models here.
class ChatSettings(models.Model):
    session_id = models.CharField(max_length=150,unique=True)
    receiver_img = models.ImageField(upload_to="receiver_pictures",blank=True,default="profile_pict.png")
    receiver_name = models.CharField(max_length=150,blank=False)
    created_at = models.DateTimeField(auto_now=True)
    dark_mode = models.BooleanField(default=True)


class Chat(models.Model):
    chat_settings = models.ForeignKey(to=ChatSettings,on_delete=models.CASCADE)
    sender = models.BooleanField(default=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
