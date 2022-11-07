import spotipy
import datetime
from spotipy.oauth2 import SpotifyOAuth
from billboard_scrapper import scrape_chart

def get_spotify_client() -> spotipy.Spotify:
    """ Get Spotify client """
    CLIENT_ID =  "YOUR_CLIENT_ID"
    CLIENT_SECRET =  "YOUR_CLIENT_SECRET"
    REDIRECT_URI = "http://localhost:8888/callback"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=REDIRECT_URI,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET, 
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    return sp

def search_spotify(tracks: list[tuple[str,str]]) -> list[str]:
    """ Search Spotify for song URIs from songs and artists names
     and return a list of URIs """
    tracks_uri = []
    
    for (artist,title) in tracks:
        result = sp.search(q=f"artist:{artist} track:{title}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            tracks_uri.append(uri)
        except IndexError:
            print(f"{artist}: {title} couldn't find in Spotify.")
    return tracks_uri

if __name__ == "__main__":
    # Create Spotify client
    sp = get_spotify_client()

    # Get Spotify user ID 
    user_id = sp.current_user()["id"]

    # Billboard Hot 100 date of searching
    date = input("Type the date (format YYYY-MM-DD) you want to search: ")
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    # Scrape Billboard 100 for list of (artist, song) tuples in a date
    tracks = scrape_chart(date)

    # Get songs URIs
    tracks_uri = search_spotify(tracks)

    # Creating a playlist
    playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100 {date}", public=False)

    # Adding found tracks to the playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=tracks_uri)