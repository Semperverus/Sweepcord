#Sweepcord is licensed under the GNU General Public License 3.0, which you can find a copy of here: https://www.gnu.org/licenses/gpl-3.0.en.html
#Original Author: Semperverus
import requests
import datetime
import json

authToken = None
header = {'Authorization': authToken}

def get_messages(guild_id, channel_id):
    if(guild_id == "@me"):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages/"
    else:
        url = f"https://discord.com/api/v9/guilds/{guild_id}/messages/"

def delete_message(channel_id, message_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"

def get_guilds(user_id = "@me"):
    url = f"https://discord.com/api/v9/users/{user_id}/guilds"

def get_guild_channels(guild_id):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"