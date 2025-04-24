import nextcord
from nextcord.ext import commands

allowed_users = set()

class LinkControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="allow_link", description="เพิ่มคนที่สามารถส่งลิงก์ได้")
    async def allow_link(self, interaction: nextcord.Interaction, user: nextcord.Member):
        allowed_users.add(user.id)
        await interaction.response.send_message(f'✅ {user.mention} สามารถส่งลิงก์ได้แล้ว!', ephemeral=True)

    @nextcord.slash_command(name="disallow_link", description="นำสิทธิ์ส่งลิงก์ออก")
    async def disallow_link(self, interaction: nextcord.Interaction, user: nextcord.Member):
        allowed_users.discard(user.id)
        await interaction.response.send_message(f'❌ {user.mention} ถูกนำสิทธิ์ออกจากการส่งลิงก์!', ephemeral=True)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if "http" in message.content or "www." in message.content:
            if message.author.id not in allowed_users:
                await message.delete()
                await message.channel.send(f'{message.author.mention} 🚫 คุณไม่มีสิทธิ์ส่งลิงก์!', delete_after=5)

def setup(bot):
    bot.add_cog(LinkControl(bot))
