# Twitch Downloader
Python script to fetch and download twitch clips (and thumbnails) via given URLs in txt file

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed the latest version of Python 3.
- Git installed on your machine.
- A Twitch account.
- A registered application on [dev.twitch.tv](https://dev.twitch.tv/console) with a Twitch API Client ID and Client Secret

If you need help getting credentials from Twitch or Google, you may check the following guides:
- [Twitch API](https://dev.twitch.tv/docs/authentication/register-app)

## Setup
Clone this repository:
```bash
git clone https://github.com/viniciusenari/automated-twitch-clips-youtube-channel
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Create a .env file and add the following variables:
```
CLIENT_SECRET = "your_twitch_client_secret"
CLIENT_ID = "your_twitch_client_id"
```

Fill the clips.txt file with the desired twitch clips URLs:
```
https://www.twitch.tv/loltyler1/clip/AbrasiveCourteousCrowOptimizePrime-PkqLs_upRAwOiqWO
https://www.twitch.tv/xfsn_saber/clip/ApatheticRelentlessPigDancingBanana-vEQpruxkKgl5-aXW
https://www.twitch.tv/caedrel/clip/GiantCooperativeBeanStoneLightning-BM1AlvLv0XmBltCG
https://www.twitch.tv/thebausffs/clip/EnjoyableZanyAdminPeteZarollTie-pO_qMufG36ZIJe6y
https://www.twitch.tv/broxah/clip/PoorPhilanthropicLemurCeilingCat-IP8l77gzwKzjcbAB
https://www.twitch.tv/agurin/clip/EnergeticBigPastaSwiftRage-8v5KuH8kicDYnd1V
https://www.twitch.tv/azzapp/clip/IgnorantShakingHamM4xHeh-pkjOMrwU9ZrRr2es
...
```

## How to Use
To run the bot, open the terminal and navigate to the main.py file's directory. Then type the following command:
```bash
python main.py
```

