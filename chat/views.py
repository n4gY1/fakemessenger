import uuid

from django.shortcuts import render, redirect

from chat.forms import ChatSettingsForm, ChatForm
from chat.models import ChatSettings, Chat


# Create your views here.
def create_chat_settings(request):
    template = "chat/create_chat_settings.html"


    form = ChatSettingsForm()

    if request.session.get('tmp') is None:
        session_id = str(uuid.uuid4())
        request.session["tmp"] = session_id
    else:
        session_id = request.session.get("tmp")
        chat_settings = ChatSettings.objects.filter(session_id=session_id).first()

        if chat_settings:
            form = ChatSettingsForm(instance=chat_settings)

    if request.method == "POST":
        session_id = request.session.get("tmp")
        chat_settings = ChatSettings.objects.filter(session_id=session_id).first()

        form = ChatSettingsForm(request.POST,request.FILES,instance=chat_settings)

        if form.is_valid():
            chat_settings = form.save(commit=False)
            chat_settings.session_id=request.session.get("tmp")
            chat_settings.save()
            return redirect("create_chat")

    context = {
        "form":form,
    }



    return render(request,template,context)


def create_chat(request):
    template = "chat/create_chat.html"
    chat_settings=None
    chat_form = ChatForm()

    if request.session.get('tmp') is not None:
        chat_settings = ChatSettings.objects.filter(session_id=request.session.get("tmp")).first()
        if chat_settings is None:
            return redirect("create_chat_settings")
    else:
        return redirect("create_chat_settings")


    session_id = request.session.get("tmp")

    chat_messages = Chat.objects.filter(chat_settings=chat_settings)

    if request.method == "POST":

        chat_form = ChatForm(request.POST)
        if chat_form.is_valid():
            message = chat_form.save(commit=False)
            message.chat_settings = chat_settings
            message.save()
            return redirect("create_chat")




    context = {
        "form" : chat_form,
        "chat_messages":chat_messages
    }
    return render(request, template, context)


def show_fb_message(request):
    template = "chat/show_chat.html"

    chat_settings = None
    if request.session.get('tmp') is not None:
        chat_settings = ChatSettings.objects.filter(session_id=request.session.get("tmp")).first()
        if chat_settings is None:
            return redirect("create_chat_settings")
    else:
        return redirect("create_chat_settings")

    chat_messages_obj = Chat.objects.filter(chat_settings=chat_settings)

    chat_messages = []
    c = chat_messages_obj.count()
    for i in range(c):
        msg = chat_messages_obj[i]
        if i+1 < c:
            next_msg = chat_messages_obj[i+1]
            if next_msg.sender:
                chat_messages.append(
                    {
                        "msg": msg,
                        "last": True
                    }
                )
            else:
                chat_messages.append(
                    {
                        "msg": msg,
                        "last": False
                    }
                )
        else:

            chat_messages.append(
                {
                    "msg": msg,
                    "last": True
                }
            )

        i += 1

    context = {
        "chat_messages": chat_messages,
        "receiver_name":chat_settings.receiver_name,
        "receiver_img":chat_settings.receiver_img
    }
    return render(request, template, context)
