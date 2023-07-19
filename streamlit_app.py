import spotipy
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
import json

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
redirect_uri = 'http://localhost:8501'
scope = 'playlist-read-private playlist-modify-private'

query_params = st.experimental_get_query_params()
sp_oauth = spotipy.oauth2.SpotifyOAuth( client_id, client_secret,redirect_uri,scope=scope, open_browser=False)
spotipy_cache = None

if os.path.exists('.cache'):
    with open('.cache') as f:
        spotipy_cache = json.load(f)

# page 0 auth
if 'code' not in query_params and spotipy_cache is None:
    # login to spotify
    auth_url = sp_oauth.get_authorize_url()
    link = f'[Login to Spotify]({auth_url})'
    st.markdown(link, unsafe_allow_html=True)

if 'code' in query_params:
    access_token = sp_oauth.get_access_token(code=query_params['code'], as_dict=False)
elif 'access_token' in spotipy_cache:
    access_token = spotipy_cache['access_token']

sp = spotipy.Spotify(auth=access_token, auth_manager=sp_oauth)

# page 1 select playlist
st.header('Select a playlist or create a new playlist')
playlists = sp.current_user_playlists()
playlistmap = {}
for playlist in playlists['items']:
    playlistmap[playlist['name']] = playlist['id']

selected_playlist = st.selectbox('my playlists', options=playlistmap, key='playlist_selector')

# select playlist or create new one
title = st.text_input('or create a New Playlist', 'Spotify DiscoverGPT Session')
st.button('create_playlist')

# page 2 show playlist and audio features

# show embed player with playlist
components.html(
    f'''<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/{playlistmap[selected_playlist]}?utm_source=generator&theme=0"
            width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media;
            fullscreen; picture-in-picture" loading="lazy"></iframe>''', height=500)