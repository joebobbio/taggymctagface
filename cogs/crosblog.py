import discord
from discord import Embed, Color
from discord.ext import commands, tasks
import feedparser
import pprint


class CrosBlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = "http://feeds.feedburner.com/GoogleChromeReleases"
        self.prev_data = feedparser.parse(self.url)

        self.watcher.start()

    def cog_unload(self):
        self.watcher.cancel()
        print("STOPPING...")

    
    # the watcher thread
    @tasks.loop(seconds=10)
    async def watcher(self):
        data = feedparser.parse(self.url, etag=self.prev_data.etag, modified=self.prev_data.modified)
        if (data.status == 304):
            await self.check_new_entries(data.entries)
        self.prev_data = data

    async def check_new_entries(self, posts):
        for post in posts:
            tags = [thing["term"] for thing in post["tags"]]
            if "Chrome OS" in tags:
                if "Stable updates" in tags:
                    await self.push_update(post, "Stable updates")
                elif "Beta updates" in tags:
                    await self.push_update(post, "Beta updates")
                elif "Dev updates" in tags:
                    await self.push_update(post, "Dev updates")
                elif "Canary updates" in tags:
                    await self.push_update(post, "Canary updates")
        pass

    async def push_update(self, post, category=None):
        if (category is None):
            channel = self.bot.get_guild(525250440212774912).get_channel(621704381053534257)
            await (channel.send(f'New blog was posted!\n{post.title}\n{post.link}'))
        else:
            channel = self.bot.get_guild(525250440212774912).get_channel(621704381053534257)
            await (channel.send(f'New blog was posted for {category} channel!\n{post.title}\n{post.link}'))

    @watcher.before_loop
    async def before_watcher(self):
        await self.bot.wait_until_ready()
        
def setup(bot):
    bot.add_cog(CrosBlog(bot))