from ui import AppUI
from spotify import SpotifyClient

if __name__ == "__main__":
    client = SpotifyClient()
    app_ui = AppUI(client)
    app_ui.run()
