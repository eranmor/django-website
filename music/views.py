from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album


# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))

'''
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

'''


def detail(request, album_id):
    return HttpResponse("<h2>Details for album id: " + str(album_id) + "</h2>")