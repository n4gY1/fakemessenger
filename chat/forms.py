from django import forms


from chat.models import ChatSettings, Chat


class ChatSettingsForm(forms.ModelForm):
    class Meta:
        model = ChatSettings
        fields = ["receiver_img","receiver_name","dark_mode"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['receiver_img', 'receiver_name']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})



class ChatForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}))
    class Meta:
        model = Chat
        fields = ["sender","message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['message']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
