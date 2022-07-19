from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
import json
import urllib.request
from .models import Room,Message
# Inside dictionary have Key and Value ,therefore ,to access value you can use the key
def index(request):
    name = 'Hezron'
    context = {
        'name': name
    }
    return render(request, 'blog/index.html',context)

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    ctx = {
        "amount": amount_of_words,
    }
    return render(request, 'blog/counter.html',ctx)

def objectdb(request):
    features = Feature.objects.all()
    
    return render(request, 'blog/home.html', {'feature':features,})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Already username exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Already email exits')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password is incorrect')
            return redirect('register')
    else:
        return render(request, 'blog/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'blog/post.html', {'pk': pk})

def search(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/3.0/onecall?q='+city+'&appid=4d3fb3efa3d4488c45bb0fbbf671926a').read()
        
        json_data = json.loads(res)
        print(json_data)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinates": str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])     
        }
    else:
        data={}
        city = ""
    return render(request, 'blog/search.html',{'city':city, 'data':data})

def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)

    ctx = {
        'username': username,
        'room_details': room_details,
    }
    return render(request, 'blog/room.html', ctx)

# function is checking if the room 
# and user is existing to the database or 
# crossing checking the existance
def checkview(request):
    room = request.POST['room']
    username =  request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


