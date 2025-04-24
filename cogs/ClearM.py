from nextcord.ext import commands
import nextcord

class ClearM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=amount)
        embed = nextcord.Embed(
            description=f"ลบข้อความจำนวน `{len(deleted)}` ข้อความแล้ว!",
            color=nextcord.Color.red()
        )
        embed.set_footer(text=f"โดย {ctx.author.display_name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ClearM(bot))
