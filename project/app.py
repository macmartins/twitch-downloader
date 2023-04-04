from project.clips import ClipsExtractor, ClipsDownloader


class App:
    clips_extractor = ClipsExtractor()
    clips_downloader = ClipsDownloader()

    def run(self):
        # Read file
        f = open("clips.txt", "r")
        content = f.read()
        clipsURLs = content.split('\n')

        # Get clips from Twitch
        self.clips_extractor.get_clips(clipsURLs)
        clips = self.clips_extractor.clips_content

        # Download clips
        self.clips_downloader.download_clips(clips)
