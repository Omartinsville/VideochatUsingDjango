from django.shortcuts import render

def room(request, room_name):
    return render(request, 'call/room.html', {'room_name': room_name})

def join_room(request, room_name):
    return render(request, 'call/room.html', {
        'room_name': room_name
    })

                                                                         