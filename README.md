<h1 align="center">Pippin Bot Documentation</h1>
Pippin Bot is a chatbot designed for use with the Discord platform. It allows users to interact with the bot through commands and provides various features such as playing music, and more. This documentation will guide you through the installation, configuration, and usage of Pippin Bot.
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
5-pip install -r requirements.txt<br>
6-Create a bot account on the Discord Developer Portal.<br>
7-Add the bot to your Discord server by following the instructions on the Discord Developer Portal.<br>
8-Copy the bot token from the Discord Developer Portal and add it to the config.json file in the Pippin Bot repository.<br>

<h2>#Configuration</h2>
To configure Pippin Bot's behavior, edit the config.json file in the Pippin Bot repository. This file contains various settings such as the bot's prefix, default volume for music playback, and more.

Additionally, you can create custom commands and responses by editing the music_cog.py and help_cog.py files. These files contain examples that can be used as templates for creating your own custom commands and responses.

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

