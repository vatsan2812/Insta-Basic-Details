from django.shortcuts import render
import requests
from django.http import HttpResponse

from .models import Greeting
import instaloader




# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")
    # r = requests.get('https://peaceful-gunnison-77284.herokuapp.com/')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    loader = instaloader.Instaloader()
    loader.load_session_from_file("_sri.vat.san_","mysession")
    profile = instaloader.Profile.from_username(loader.context,"_sri.vat.san_")
    followers = profile.get_followers()
    followees = profile.get_followees()
    
    namestr = "Profile Name " + "_sri.vat.san_" + " \n"
    followeestr = "Followees " + str(followees.count) + " \n"
    followerstr = "Followers " + str(followers.count) + " \n"

    
    return HttpResponse('<pre>' + namestr + followerstr + followeestr + '</pre>')

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



