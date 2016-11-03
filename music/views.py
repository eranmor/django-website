from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.
# render has httprespnse built in

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

'''
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

'''

def detail(request, album_id):

    # This was the response before connecting to the DB
    # return HttpResponse("<h2>Details for album id: " + str(album_id) + "</h2>")

'''
    try:
        album = Album.objects.get(pk=album_id)
        context = {'album': album}
    except Album.DoesNotExist:
        raise Http404("Sorry, album does not exist")
'''
# Shortcut using get_object_or_404 package
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', context)