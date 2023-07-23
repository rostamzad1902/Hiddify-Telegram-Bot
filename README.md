# Hiddify Management Telegram Bot

By using this bot you can manage your hiddify panel from telegram.

We in BETA version, and we are working on it to make it better so please report any bugs or issues you find.

Please note that this bot is <b>not official</b> and is not affiliated with hiddify in any way.

some of the features are:
- [x] add users
- [x] remove users
- [x] edit users
- [x] show users list
- [x] search users (by name, config , uuid)
- [x] show users info (name, traffic, date, etc)
- [x] show user configs and subscription links
- [x] get backup of your panel
- [x] show server status (ram, cpu, disk)
- [x] and more...

## Installation

- #### clone the repo and cd into it

      git clone https://github.com/B3H1Z/Hiddify-Telegram-Bot.git
      cd Hiddify-Telegram-Bot

- #### install the requirements

      pip install -r requirements.txt
- #### now run config.py and fill in the required fields to generate a config.json file

      python3 config.py

- #### required fields are:

1. `Admin Telegram Number ID` : get it from [User info bot](https://t.me/userinfobot) (Example: `123456789`)
2. `Telgram Bot Token` : get it from [BotFather](https://t.me/BotFather) (
   Example: `1234567890:ABCdEfGhIjKlMnOpQrStUvWxYz`)
3. `Hiddify Panel URL` : the url of your hiddify panel (
   Example: `https://panel.example.com/7frgemkvtE0/78854985-68dp-425c-989b-7ap0c6kr9bd4`) <b>exactly like this
   pattern!</b>
4. `Bot Language` : options are `en` and `fa` [default is `fa`]


- ### now run the bot in background using nohup

      nohup python3 hiddifyTelegramBot.py &

  Now you can use the bot in telegram by `/start` command


## Commands
- ### to stop the bot use this command

      pkill -9 -f hiddifyTelegramBot.py
- ### to restart the bot use this command

      pkill -9 -f hiddifyTelegramBot.py && nohup python3 hiddifyTelegramBot.py &
- ### to update the bot use this command

      pkill -9 -f hiddifyTelegramBot.py && git pull && nohup python3 hiddifyTelegramBot.py &
- ### to get the bot log use this command

      cat log.txt
- ### to get the bot config use this command

      cat config.json

## Screenshots
some screenshots of the bot:
- <img src="https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/screenshots/Keyboard.PNG?raw=True" width=50% height=50%>
  
- <img src="https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/screenshots/UsersList.PNG?raw=True" width=50% height=50%>
- <img src="https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/screenshots/UserInfo.PNG?raw=True" width=50% height=50%>
- <img src="https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/screenshots/ConfigAndSub.PNG?raw=True" width=50% height=50%>
- <img src="https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/screenshots/Search.PNG?raw=True" width=50% height=50%>
- <img src="https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/screenshots/AddUser.PNG?raw=True" width=50% height=50%>
- <img src="https://github.com/B3H1Z/Hiddify-Telegram-Bot/blob/main/screenshots/BackupAndStartus.PNG?raw=True" width=50% height=50%>