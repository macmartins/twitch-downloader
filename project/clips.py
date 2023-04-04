import os

import requests
from project.utils import client_id, client_secret
from project.twitch_api import TwitchAPI
from datetime import date

api = TwitchAPI()
api.auth(client_id, client_secret)
today = date.today()

class ClipContent:
    def __init__(self, url, broadcaster_id, broadcaster_name, game_id, title, thumbnail_url, duration, path):
        self.url = url
        self.broadcaster_id = broadcaster_id
        self.broadcaster_name = broadcaster_name
        self.game_id = game_id
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.duration = duration
        self.path = path

    def __str__(self):
        return f'url: {self.url}\nbroadcaster_id: {self.broadcaster_id}\nbroadcaster_name: {self.broadcaster_name}\ncreator_name: {self.creator_name}\ntitle: {self.title}\nthumbnail_url: {self.thumbnail_url}'


class ClipsExtractor:
    def __init__(self):
        self.clips_content = []

    def get_clips(self, clipsURLs):
        for clipURL in clipsURLs:
            clipID = clipURL.split("/clip/")[1]
            params = {
                'id': clipID
            }
            response = requests.get('https://api.twitch.tv/helix/clips', params=params, headers=api.headers).json()
            for clip in response['data']:
                self.clips_content.append(ClipContent(
                    clip['url'],
                    clip['broadcaster_id'],
                    clip['broadcaster_name'],
                    clip['game_id'],
                    clip['title'],
                    clip['thumbnail_url'],
                    clip['duration'],
                    f'files/clips/{today}/{clipsURLs.index(clipURL) + 1}.mp4'
                ))

class ClipsDownloader():
    def __init__(self):
        pass

    @staticmethod
    def download_clip(clip):
        index = clip.thumbnail_url.find('-preview')
        clip_url = clip.thumbnail_url[:index] + '.mp4'

        r = requests.get(clip_url)
        if r.headers['Content-Type'] == 'binary/octet-stream':
            if not os.path.exists(f'files/clips/{today}'): os.makedirs(f'files/clips/{today}')
            with open(clip.path, 'wb') as f:
                f.write(r.content)
        else:
            print(f'Failed to download clip from thumb: {clip.thumbnail_url}')

    def download_clips(self, clips):
        for i in range(len(clips)):
            print(f'Downloading clip {i + 1}/{len(clips)}')
            clip = clips[i]
            self.download_clip(clip)
            self.download_thumbnail(clip, i)

    @staticmethod
    def download_thumbnail(clip, i):
        r = requests.get(clip.thumbnail_url)
        if not os.path.exists(f'files/thumbnails/{today}'): os.makedirs(f'files/thumbnails/{today}')
        try:
            with open(f'files/thumbnails/{today}/{i}.jpg', 'wb') as f:
                f.write(r.content)
        except:
            print(f'Failed to download thumbnail: {clip.thumbnail_url}')