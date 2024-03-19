import os

from env_setup import env_setup
from ui import AppUI
from spotify import SpotifyClient


def main():
    """
    Main function to run the Spotify Analytics application.
    It first checks if the .env file exists, and if not, it runs the env_setup function to create it.
    Then it creates a SpotifyClient and an AppUI and runs the AppUI.
    """
    if not os.path.exists(".env"):
        try:
            env_setup()
        except Exception as e:
            print(f"Failed to set up environment: {e}")
            return

    try:
        client = SpotifyClient()
    except Exception as e:
        print(f"Failed to authenticate with Spotify: {e}")
        return

    app_ui = AppUI(client)
    app_ui.run()


if __name__ == "__main__":
    main()
