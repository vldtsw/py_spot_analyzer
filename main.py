from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Spotify API client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="user-top-read",
    )
)

top_tracks = sp.current_user_top_tracks(limit=10)["items"]
top_tracks = tuple(
    f"{track['name']} – {', '.join(artist['name'] for artist in track['artists'])}"
    for track in top_tracks
)
print(top_tracks)
