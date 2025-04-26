import nextcord
from nextcord.ext import commands
import DiscordUtils
import datetime

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.invtrck = DiscordUtils.InviteTracker(bot)

        self.guild_id = 1350767999862177812
        self.logs_welcome_id = 1350768587597545545

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"[DEBUG] มีคนเข้าเซิฟ: {member.name}")
        inver = await self.invtrck.fetch_inviter(member)
        channel = self.bot.get_channel(self.logs_welcome_id)
        guild = self.bot.get_guild(self.guild_id)
        total = 0

        for i in await guild.invites():
            if i.inviter == inver:
                total += i.uses

        embedjoin = nextcord.Embed(
            title="ยินดีต้อนรับนะคะ~",
            description=f"## คุณ **{member.mention}** เข้าร่วมเซิฟเวอร์\n## ยืนยันตัวตนได้ที่ <#1350768591271886869> นะ~",
            colour=0x00FF99
        )
        embedjoin.set_image(url="https://i.pinimg.com/originals/d6/6a/d1/d66ad1a0ce0fc09370424075125b06b7.gif")
        embedjoin.timestamp = datetime.datetime.utcnow()
        embedjoin.set_footer(text=" | 𝐖𝐞𝐥𝐥𝐜𝐨𝐦𝐞 | ")
        embedjoin.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)

        await channel.send(embed=embedjoin)

def setup(bot):
    bot.add_cog(WelcomeCog(bot))
    
