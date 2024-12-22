import requests


def getResponse(api_key, channel_id):
    # Fetch playlist ID of uploads
    playlist_url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={api_key}"
    response = requests.get(playlist_url).json()
    upload_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Fetch all video descriptions
    videos = []
    next_page_token = None
    while True:
        # Add contentDetails to get video durations
        video_list_url = (
            f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails"
            f"&playlistId={upload_playlist_id}&maxResults=50&key={api_key}"
        )
        if next_page_token:
            video_list_url += f"&pageToken={next_page_token}"

        response = requests.get(video_list_url).json()

        # Fetch video durations in batch
        video_ids = [item['contentDetails']['videoId'] for item in response['items']]
        video_details_url = (
            f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails"
            f"&id={','.join(video_ids)}&key={api_key}"
        )
        duration_response = requests.get(video_details_url).json()

        # Create duration lookup dictionary
        duration_dict = {
            item['id']: item['contentDetails']['duration']
            for item in duration_response['items']
        }

        # Add duration to each video item
        for item in response['items']:
            video_id = item['contentDetails']['videoId']
            item['contentDetails']['duration'] = duration_dict.get(video_id, 'N/A')

        videos.extend(response['items'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos


def parse_duration(duration_str):
    """Convert ISO 8601 duration to minutes"""
    import re
    import isodate
    try:
        duration = isodate.parse_duration(duration_str)
        return int(duration.total_seconds() // 60)
    except:
        return 0


def checkVideos(videos):
    videos_list = []
    channel_name = ""
    index = 1

    for video in videos:
        channel_name = video['snippet']['channelTitle']
        video_details = {}
        description = video['snippet']['description']
        video_details["Sr.No."] = index
        index += 1
        video_details["Title"] = video['snippet']['title']
        video_id = video['snippet']['resourceId']['videoId']
        video_details["Date"], video_details["Time"] = video['snippet']["publishedAt"].split("T")
        video_details["URL"] = f"https://www.youtube.com/watch?v={video_id}"
        video_details["Duration"] = parse_duration(video['contentDetails']['duration'])

        if "RPM" in description:
            video_details["Credits"] = "FOUND"
        else:
            video_details["Credits"] = "NOT FOUND"
        videos_list.append(video_details)

    return videos_list, channel_name
