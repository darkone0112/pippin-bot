<h1 align="center">Pippin Bot Documentation</h1>
Pippin Bot is a music Bot designed for use with the Discord platform. It allows users to interact with the bot through commands and provides various features such as playing music. This documentation will guide you through the installation, configuration, and usage of Pippin Bot.
<h2>#Prerequisites</h2>
Before installing Pippin Bot, you need to ensure that you have the following prerequisites:

<ul>
  <l1>-Python 3.6 or higher</l1><br>
   <l1>-pip package manager</l1><br>
   <l1>-Git version control system</l1><br>
   <l1>-Installing Pippin Bot</l1><br>
</ul>

<h2>#To install Pippin Bot, follow these steps:</h2>
1-Open a command prompt or terminal window.<br>
2-Clone the Pippin Bot repository using the following command:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git clone https://github.com/darkone0112/pippin-bot.git<br>
3-Change to the cloned directory:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cd pippin-bot<br>
5-Create a bot account on the Discord Developer Portal.<br>
6-Add the bot to your Discord server by following the instructions on the Discord Developer Portal.<br>
7-Copy the bot token from the Discord Developer Portal and add it directly to the code(*harcoding a login token in the raw code is a bad practice and not the best for security you can get your bot banned from discord and github if the token is uploded to internet for example a github repositorie of your own*) or as an env(The way to go ;) )if you are using a linux distro you as ubuntu server you can add the enveriomental variable to the system using export var="the token" if you need it to be permanently upond restarts youu can follow this tutorial https://tecadmin.net/setting-up-environment-variables-on-ubuntu/ <br>
8-Install the discord module for python "sudo pip install discord" (need pip package manager "installed sudo apt install python3.pip")<br>
9-Install the YoutubeDL module for python "sudo pip install youtube_dl"<br>
10-Afet the steps you can try to run the bot using python3 main.py inside the folder(It should start correctly then try to use the bot on the server; at the moment there is a bug in the youtube_dl master branch whe tried to play music you should receive an error fomr the URL extractor, the library is deprecated an receive no more updates, but there is the yt_dlp fork that keep the support so the best option will be just install that module in first place "sudod pip install yt_dlp")<br>
11-You need to install the ffmpeg proccesor in the server (https://ffmpeg.org/download.html)<br>
12-All should be set and ready to launch the bot with python3 main.py (Remember to modified the code to call the correct ENV the cloned code call a "bot ENV")<br>
13-If you are running the bot in a command line only OS as Ubuntu Server you can use tmux to handle multiple consoles cause the bot proccess will block the window the documentation can be found here: https://www.redhat.com/sysadmin/introduction-tmux-linux<br>

<h2>#Usage</h2>
To use Pippin Bot on your Discord server, simply type the bot's prefix followed by a command. For example, if the prefix is set to !, you can play music by typing !play <song name>.
Pippin Bot supports various commands for playing music, generating memes, and more. A list of available commands can be found by typing !help on your Discord server.
        <h3>#Commands</h3>
        /help - Shows this message<br>
        /play - Plays a song from a url or search query (searches youtube)<br>
        /pause - Pauses the current song<br>
        /resume - Resumes the current song<br>
        /skip - Skips the current song<br>
        /queue - Shows the current queue<br>
        /clear - Stops the bot and clears the queue<br>

<h2>#Conclusion</h2>
Congratulations! You have successfully installed, configured, and used Pippin Bot on your Discord server. If you have any questions or feedback, feel free to reach out to the Pippin Bot community or open an issue on the Pippin Bot GitHub repository.

