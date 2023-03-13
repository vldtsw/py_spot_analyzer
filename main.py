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
        # scope="playlist-read-private",
    )
)

# Fetch the user's playlists
results = sp.current_user_playlists()

# Print the name of each playlist
for item in results["items"]:
    print(item["name"])
