import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from IPython.display import Audio
import random

# Spotify API credentials - Replace with your own credentials
CLIENT_ID = '51babcfa1b8549449d3de94ac58bf158'
CLIENT_SECRET = '295b947504ac474aa26c7831cafb1443'

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_song_recommendations(seed_song_id):
    try:
        # Get audio features of the seed song
        seed_song = spotify.track(seed_song_id)
        seed_song_features = spotify.audio_features([seed_song_id])

        if seed_song_features:
            seed_song_features = seed_song_features[0]

            # Extract relevant features
            seed_features = [
                seed_song_features['acousticness'],
                seed_song_features['danceability'],
                seed_song_features['energy']
            ]

            # Get recommendations based on seed features
            recommendations = spotify.recommendations(seed_tracks=[seed_song_id], seed_genres=[],
                                                      seed_artists=[], limit=50,
                                                      target_acousticness=seed_features[0],
                                                      target_danceability=seed_features[1],
                                                      target_energy=seed_features[2])

            recommended_songs = []
            for track in recommendations['tracks']:
                recommended_songs.append({
                    'title': track['name'],
                    'artist': track['artists'][0]['name'],
                    'preview_url': track['preview_url']
                })

            return recommended_songs

        else:
            return None

    except spotipy.SpotifyException as e:
        print(f'An error occurred: {e}')


# Streamlit app
st.title("Song Recommendation System")

# Input seed song ID
list1 = [1, 2, 3, 4, 5, 6,7]
n=random.choice(list1)



    # t= st.selectbox(
    # "Type or select a movie from the dropdown",
    # ("Motivational","RomCom","Comedy","Action","Happy","Optimistic"))
Motivational= "2J2Z1SkXYghSajLibnQHOa"
Optimistic= "1nInOsHbtotAmEOQhtvnzP"
Happy= "6KgBpzTuTRPebChN0VTyzV"
Dance="0cqRj7pUJDkTCEsJkx8snD"
Refreshing="6SqDyr9nscxtz48GJHOXiR"
Sweet="7xbXQeepclfQNqI3mLPb3c"
Selflove= "42ydLwx4i5V49RXHOozJZq"
if n==1:
    seed_song_id= Happy
elif n==2:
    seed_song_id= Dance
elif n==3:
    seed_song_id= Optimistic
elif n == 4:
    seed_song_id = Refreshing
elif n==5:
    seed_song_id= Sweet
elif n==6:
    seed_song_id= Selflove
elif n==7:
    seed_song_id= Motivational



# Get recommendations when button is clicked
if st.button("Get Recommendations"):
    recommended_songs = get_song_recommendations(seed_song_id)
    if recommended_songs:
        for song in recommended_songs:
            st.write(f'{song["title"]} - {song["artist"]}')
            if song["preview_url"]:
                st.audio(song["preview_url"], format="audio/mp3")
            else:
                st.write("No preview available for this song.")
    else:
        st.write('No recommendations found.')
if __name__ == '__main__':
    def add_bg_from_url():
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background-image: url("https://cdn.dribbble.com/users/4530006/screenshots/14028675/media/81057794f1927a27006957c8d917b8b5.gif");
                 background-attachment: fixed;
                 background-size: cover
             }}
             </style>
             """,
            unsafe_allow_html=True
        )


    add_bg_from_url()
