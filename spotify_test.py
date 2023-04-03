import spotipy
import spotipy.util as util
import os
from dotenv import load_dotenv
from spotipy import SpotifyOAuth

load_dotenv()  # loads environment variables from .env file

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope='user-library-read user-modify-playback-state',
    )
)

# Get track URI
track_name = "Stairway to Heaven"  # Replace with your desired song
results = sp.search(q=track_name, limit=1)
track_uri = results['tracks']['items'][0]['uri']

# Play the track
sp.start_playback(uris=[track_uri])
