from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

def send(request):
    message = request.POST.get('message', '')
    username = request.POST.get('username', '')
    room_id = request.POST.get('room_id', '')
    image = request.FILES.get('image')  # Get the uploaded image if any

    # Create a new message with the image if it exists
    new_message = Message.objects.create(
        value=message,
        user=username,
        room=room_id,
        image=image  # Pass the image directly to the model
    )
    new_message.save()

    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)

    # Return image URL along with the messages
    messages_data = [{
        "user": message.user, 
        "value": message.value, 
        "date": message.date.strftime('%Y-%m-%d %H:%M:%S'),  # Ensure date is formatted as string
        "image": message.image.url if message.image else None
    } for message in messages]
    return JsonResponse({"messages": messages_data})
