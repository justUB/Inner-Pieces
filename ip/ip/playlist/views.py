from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.
def playlist(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='5a9865286eba46fea9a51894e3e6f1db',client_secret='76e250e3b57d4b449dacfb3a117b4f03',))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks']
        return render(request,'playlist/playlist.html',{"results":final_result})
    else:
      return render(request,'playlist/playlist.html',)
