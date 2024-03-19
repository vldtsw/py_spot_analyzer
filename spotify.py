import spotipy
import os
from dotenv import load_dotenv
from spotipy import SpotifyOAuth


class SpotifyClient:
    def __init__(self):
        load_dotenv()
        scope: str = "user-library-read"

        self.sp: spotipy.Spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                scope=scope,
            )
        )

    def get_account_name(self) -> str:
        user: dict = self.sp.current_user()
        return user["display_name"]

    def get_num_liked_tracks(self) -> int:
        response: dict = self.sp.current_user_saved_tracks(limit=1)
        return response["total"]
