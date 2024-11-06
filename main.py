import requests

API_KEY = 'AIzaSyCzuFXynRJbBYAhOn0Arkxd27LHVK0Wy1M'
CHANNEL_ID = 'UCcmLksNmHmp4gZmZCA1-DHA'

# Fetch playlist ID of uploads
playlist_url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={CHANNEL_ID}&key={API_KEY}"
response = requests.get(playlist_url).json()
upload_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Fetch video descriptions
video_list_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={upload_playlist_id}&maxResults=50&key={API_KEY}"
videos = requests.get(video_list_url).json()

for video in videos['items']:
    description = video['snippet']['description']
    title = video['snippet']['title']
    video_id = video['snippet']['resourceId']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    if "RPM" in description:
        print(f"\nCREDIT FOUND in video: {title}\nLink: {video_url}")
        print('_'*150)
    else:
        print(f"\nNO CREDIT FOUND in video: {title}\nLink: {video_url}")
        print('_' * 150)
