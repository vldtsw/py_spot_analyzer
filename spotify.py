import spotipy
import os
from dotenv import load_dotenv
from spotipy import SpotifyOAuth


class SpotifyClient:
    def __init__(self):
        # todo: add login prompt instead of using .env
        # check if credentials exist, create if not
        # use urwid or questionary (or regular input)
        load_dotenv()
        scope = "user-library-read"

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                scope=scope,
            )
        )

    def get_account_name(self):
        user = self.sp.current_user()
        return user["display_name"]

    def get_num_liked_tracks(self):
        response = self.sp.current_user_saved_tracks(limit=1)
        return response["total"]
