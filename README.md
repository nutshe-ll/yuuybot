# yuuybot
Source code for the Discord bot, yuuy bot.

[Add It](https://discord.com/api/oauth2/authorize?client_id=1144560314361315438&permissions=8&scope=bot)


### Creating a Bot and adding to your server

◙ Go to `Discord Developer Portal` by [clicking here](https://discord.com/developers/applications)

◙ Click on to `New Application` and then name your bot what you want.

◙ Select the application, select `OAuth2`

◙ Select `Add Bot` to add a bot to your application.

◙  Then go to `OAuth2` and `URL Generator`to get the bot's invite link

◙ At scopes select `bot` and at `Bot Permissions` you have to select `administrator`

◙ Copy the invite link which is generated on the `Scopes`

◙ Go to bot tab then you'll see `TOKEN` click copy 

◙ Open `main.py` and then paste the token into the `bot.run(TOKEN)`

◙ Make sure you don't give the token to someone else, or they could access your bot
<br>
<br>
<br>
### Installing modules and packages
◙ Install `discord.py` by pasting this code into the terminal:

```py
py -3.6 -m pip install -U discord.py[voice]
```

◙ Next, Install `yt-dlp` by pasting this code into the terminal:

```py
pip instal yt-dlp
```

◙ Now, Install `ffmpeg` by clicking [here](https://ffmpeg.org/download.html)

◙ After that, select one based on your operating system from the three options below

![ffmpeg_installation](https://github.com/nutshe-ll/yuuybot/assets/79253256/3c165f15-fb7c-4d8c-81fc-f38408d25afd)


  - # Installing `ffmpeg` on Windows
    ◙ If you're on Windows, select `Windows builds by gyan.dev`
    
    ![windows_ffmpeg_installation](https://github.com/nutshe-ll/yuuybot/assets/79253256/cb30f63e-7f94-4532-a7da-2c9f8d32ef5f)



    
    ◙ After you selected it, you will be redirected to `https://www.gyan.dev/ffmpeg/builds/`

    ![windows_ffmpeg_installation_gyan_dev](https://github.com/nutshe-ll/yuuybot/assets/79253256/621ae2f1-e96d-4431-959a-2d08f73b2f6b)

    ◙ Select `ffmpeg-git-full.7z`
    
    ◙ After you downloaded it, open the ffmpeg folder and copy `bin`
    
    ◙ Paste the bin to `Local Disk(C:)` and rename it to `ffmpeg`
    
    ◙ After that, open `Edit the system environment variables`
    
    ![environmental_variables](https://github.com/nutshe-ll/yuuybot/assets/79253256/332c1b6a-ec26-4179-9c46-557380980a10)

    ◙ If you get this popup, select `Environment Variables`

    ![environment_variables_popup](https://github.com/nutshe-ll/yuuybot/assets/79253256/a53db330-b083-4e84-b3b3-002757ea57c7)

     ◙ At `System Variables`, select `PATH` and select `Edit`

    ![environment_variables_edit](https://github.com/nutshe-ll/yuuybot/assets/79253256/db4225e8-acad-4d68-8524-1e29566350e1)

    ◙ Now, select `New`, and then set the value to `C:/ffmpeg`

    # You're done installing the modules and packages!


yuuy bot by nutshe-ll\
Discord = akuWibu#9019\
Twitter = @ThousandCringes\
Youtube = omegacringes
