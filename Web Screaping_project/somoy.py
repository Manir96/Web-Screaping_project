from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
def scrape_channel_videos(channel_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the uploads playlist ID for the channel
    channels_response = youtube.channels().list(
        id=channel_id,
        part='contentDetails'
    ).execute()
    uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve all videos from the uploads playlist
    videos = []
    next_page_token = None
    while True:
        playlist_items_response = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos.extend(playlist_items_response['items'])

        next_page_token = playlist_items_response.get('nextPageToken')
        if not next_page_token:
            break

    # Extract the video IDs and generate the video URLs
    video_links = []
    for video in videos:
        video_id = video['snippet']['resourceId']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_links.append(video_url)

    return video_links
def main():
    # Replace 'YOUR_CHANNEL_ID' with the desired YouTube channel ID
    channel_id = 'YOUR_CHANNEL_ID'
    
    # Replace 'YOUR_API_KEY' with your YouTube Data API v3 key
    api_key = 'YOUR_API_KEY'
    
    try:
        video_links = scrape_channel_videos(channel_id, api_key)
        for link in video_links:
            print(link)
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')

if __name__ == '__main__':
    main()
