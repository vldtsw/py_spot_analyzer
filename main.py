import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# create a SpotifyOAuth instance
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        # scope="user-library-read"
    )
)

sp.start_playback(uris=['spotify:track:1f3yAtsJtY87CTmM8RLnxf'])

# def print_favorite_tracks():
#     results = sp.current_user_saved_tracks(limit=50)
#     for idx, item in enumerate(results['items']):
#         track = item['track']
#         print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']} from the album {track['album']['name']}")
#
#
# def print_top_genres():
#     results = sp.current_user_top_artists()
#     genre_dict = {}
#     for item in results['items']:
#         genres = item['genres']
#         for genre in genres:
#             if genre in genre_dict:
#                 genre_dict[genre] += 1
#             else:
#                 genre_dict[genre] = 1
#     total_genres = sum(genre_dict.values())
#     for genre, count in sorted(genre_dict.items(), key=lambda x: x[1], reverse=True):
#         print(f"{genre}: {count / total_genres * 100:.2f}%")
#
#
# def display_info():
#     print("Favorite Tracks:\n")
#     print_favorite_tracks()
#     print("\nTop Genres:\n")
#     print_top_genres()
#
#
# if __name__ == '__main__':
#     display_info()
