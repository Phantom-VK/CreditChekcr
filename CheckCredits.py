import requests


def getResponse(api_key, channel_id):
    # Fetch playlist ID of uploads
    playlist_url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={api_key}"
    response = requests.get(playlist_url).json()
    upload_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Fetch video descriptions
    video_list_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={upload_playlist_id}&maxResults=50&key={api_key}"
    videos = requests.get(video_list_url).json()

    return videos


def checkVideos(videos):
    videos_list = []
    channel_name = ""
    index = 1
    for video in videos['items']:
        channel_name = video['snippet']['channelTitle']
        video_details = {}
        description = video['snippet']['description']
        video_details["Sr.No."] = index
        index += 1
        video_details["Title"] = video['snippet']['title']
        video_id = video['snippet']['resourceId']['videoId']
        video_details["Date"], video_details["Time"] = video['snippet']["publishedAt"].split("T")
        video_details["URL"] = f"https://www.youtube.com/watch?v={video_id}"

        if "RPM" in description:
            video_details["Credits"] = "FOUND"
        else:
            video_details["Credits"] = "NOT FOUND"
        videos_list.append(video_details)
    return videos_list, channel_name


