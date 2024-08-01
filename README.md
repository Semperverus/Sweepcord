# Sweepcord
Sweepcord is a daemon written in Python that allows you to automatically delete Discord messages older than a set time period. It runs invisibly on your computer and tidies up behind you as you chat.

This project was heavily inspired by [Undiscord](), which was also used as a reference. As such, there will be strong similarities in the code. Undiscord is OSS-licensed under the MIT license.

⚠️ THIS PROJECT IS CURRENTLY A WORK IN PROGRESS ⚠️

## How to Use

As this project is a work in progress, this section is not yet available. However, the intended design will be to allow you to either pass an authorization token to the program via a flag, for example:

`Python sweepcord.py -Authtoken "XXXXXXXXXXXXXXXXXXXX" -Timerange "7d"`

which you could then set up as a scheduled task on Windows or call as a Cron job or a SystemD timer on Linux at a time interval of your choosing.

## Discord's Data Retention Policy

Discord's data retention policy is available [here](https://support.discord.com/hc/en-us/articles/5431812448791-How-long-Discord-keeps-your-information).
As of this writing (2024-07-30), the policy states:
>You may edit or erase content that you post within Discord. For example:
>
>* You can edit or delete any message you have sent or content you have posted if you still have access to the space where you posted it.
>* You can edit or delete a Discord server if you have the permissions needed to do so.
>* You can edit or delete a channel from a Discord server if you have the permissions needed to do so.
>
>Once you delete content, it will no longer be available to other users (though it may take some time to clear cached uploads). Deleted content will also be deleted from Discord’s systems, but we may retain content longer if we have a legal obligation to preserve it as described below.  Public posts may also be retained for 180 days to two years for use by Discord as described in our Privacy Policy (for example, to help us train models that proactively detect content that violates our policies).

Please check the link above this quote to verify that no changes have been made. If any major changes are made, consider this a canary.

This project operates under the assumption that Discord is being truthful. Please be aware that, without independent auditors routinely verifying this, you should take Discord's public-facing policy with a healthy heap of salt. Discord is not a private chat platform.

## Privacy-Friendly Alternatives to Discord
Please see the [DISCORD_ALTERNATIVES.md](./DISCORD_ALTERNATIVES.md) document if you are interested in moving your friend group away from Discord.

## License
Sweepcord is licensed under the GNU General Public License 3.0, available [here](https://support.discord.com/hc/en-us/articles/5431812448791-How-long-Discord-keeps-your-information) and included in this repository as a `LICENSE` file.
