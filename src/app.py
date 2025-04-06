import os
import spotipy
import pandas as pd
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
trueno_uri = 'spotify:artist:2x7PC78TmgqpEIjaGAZ0Oz'

spotify = spotipy.Spotify(auth_manager=auth_manager)

results = spotify.artist_top_tracks(trueno_uri)

tracks = []
for result in results['tracks'][:10]:
    track = result['name']
    duration = round(result['duration_ms']/60000,2)
    popularity = result['popularity']
    tracks.append([track,duration,popularity])

df = pd.DataFrame(tracks,columns=['Name', 'Duration', 'Popularity'])

top3 = df.sort_values('Popularity',ascending=False)[:3]
print(top3)

plt.scatter(df['Duration'],df['Popularity'])
plt.title("Trueno")
plt.xlabel('Duration')
plt.ylabel("Popularity")
plt.savefig("trueno_pop.png")

# No hay ninguna relación clara entre la duración y la popularidad de las canciones