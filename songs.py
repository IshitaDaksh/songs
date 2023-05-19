import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials - Replace with your own credentials
CLIENT_ID = '51babcfa1b8549449d3de94ac58bf158'
CLIENT_SECRET = '295b947504ac474aa26c7831cafb1443'

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def search_songs(query, max_results=5):
    try:
        # Search for songs with the given query
        results = spotify.search(q=query, type='track', limit=max_results)
        songs = results['tracks']['items']

        # Extract song details
        song_info = []
        for song in songs:
            info = {
                'title': song['name'],
                'artist': song['artists'][0]['name'],
                'preview_url': song['preview_url']
            }
            song_info.append(info)

        return song_info

    except spotipy.SpotifyException as e:
        st.error(f'An error occurred: {e}')


# Streamlit app
def main():
    st.title('Song Recommendations')
    st.write('Welcome! This app recommends songs based on different categories.')

    # Predefined categories
    categories = {
        'Motivational': 'motivational',
        'Happy': 'happy',
        'Dance': 'dance',
        'Country Music': 'country',
        'Romantic': 'romantic',
        'Self Love': 'self love'
    }

    # Recommendation selection
    selected_category = st.selectbox('Select a category', list(categories.keys()))

    # Show songs button
    if st.button('Show Songs'):
        # Search songs
        songs = search_songs(categories[selected_category])
        if songs:
            for song in songs:
                st.write(f'{song["title"]} - {song["artist"]}')
                st.audio(song["preview_url"])
        else:
            st.warning('No songs found.')


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
    main()