# What is this repo about?
This is a Telegram bot writen in Python for searching files in Drive. Based on [SearchX-bot](https://github.com/SVR666/SearchX-bot)

# How to deploy?

- Clone this repo:
```
git clone https://github.com/SlamDevs/drive-searchbot searchbot/
cd searchbot
```

### Install requirements

- For Debian based distros
```
sudo apt install python3
sudo snap install docker 
```
- For Arch and it's derivatives:
```
sudo pacman -S docker python
```

## Setting up config file
```
cp config_sample.env config.env
```
- Remove the first line saying:
```
_____REMOVE_THIS_LINE_____=True
```
Fill up rest of the fields. Meaning of each fields are discussed below:
- `BOT_TOKEN`: The telegram bot token that you get from [@BotFather](https://t.me/BotFather)
- `OWNER_ID`: The Telegram user ID (not username) of the owner of the bot
- `AUTHORIZED_CHATS`: (optional) Fill user_id and chat_id (not username) of you want to authorize, Seprate them with space, Examples: `-0123456789 -1122334455 6915401739`.
- `TOKEN_PICKLE_URL`: (optional) Only if you want to load your **token.pickle** externally from an Index Link. Fill this with the direct link of that file.
## Upgrading.

If you are coming from last version where recursive searching was not possible, you must run driveid.py again and delete all previous content, and this time you just have to add Drives (Teamdrive or 'root' for Main Drive). See the section below for more.


## Setting up drive_folder file

- The bot can now search in sub-directories, so you just need to specify the teamdrives you want to use. To use main Drive, you can enter 'root' in the Drive id.
- Add Drive name (anything that you likes), Drive id & Index url (optional) corresponding to each id.
- Run `driveid.py` and follow the screen.
```
python3 driveid.py
```

## Getting Google OAuth API credential file

- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your **credentials.json**.
- Move that file to the root of searchbot, and rename it to credentials.json
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate token file **token.pickle** for Google Drive:
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```

## Deploying on Server
- Start docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t searchbot
```
- Run the image:
```
sudo docker run searchbot
```

## Deploying on Heroku
- Give a star and Fork this repo
- Upload **token.pickle** and **drive_folder** to your forks, for **token.pickle** you also can upload your **token.pickle** to your Index and put your **token.pickle** link to `TOKEN_PICKLE_URL`.
- Hit the **DEPLOY TO HEROKU** button and follow the further instructions in the screen (**NOTE**: If vars not coming, just change deploy link to your fork, Example: `https://dashboard.heroku.com/new?template=https://github.com/yourgithubname/drive-searchbot`)

<p><a href="https://heroku.com/deploy"> <img src="https://img.shields.io/badge/Deploy%20to%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>

# Credits:

- [`lzzy12`](https://github.com/lzzy12)
- [`SVR666`](https://github.com/SVR666)
