from django.shortcuts import render

# Create your views here.
def chat(request, username):
    return render(request, 'chat/index.html', {
        'username': username,
    })