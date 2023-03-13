import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# Create spotipy authentication object
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-top-read"
    )
)

# Get user's top 10 artists
top_artists = sp.current_user_top_artists(limit=10, time_range="medium_term")

# Print the name of the artist and the number of followers
for artist in top_artists["items"]:
    # Fetch detailed artist information
    artist_info = sp.artist(artist["id"])
    print(artist_info["name"], "-", artist_info["followers"]["total"], "followers")
