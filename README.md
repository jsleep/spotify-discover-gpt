# 🎧 Spotify Discover GPT 

In this app, we connect streamlit to the Spotify API and provide controls for searching and getting recommendations for a selected playlist with advanced controls such as:
- Viewing audio feature metadata like tempo, genre, etc.
- Controlling recommendation parameters for attributes like tempo, genre, etc.

In the next iteration, we will use LangChain to automate searching/getting recommedations outside of specifying via visual controls by using natural language queries to convert to proper function inputs.

## setup 
setup an app with Spotify Web API [here](https://developer.spotify.com/dashboard)
set the client_id and client_secret fields in a file name ".env" in the root of the repo.

## installation
- create aand activate a conda environment with python 3.11
- run the following command to install python dependencies:
```
pip install -r requirements.txt
```

## run locally
run the following command:
```
streamlit run streamlit_app.py
```

## Demo App

TBA: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://starter-kit.streamlitapp.com/)