import nextcord
from nextcord.ext import commands
from datetime import datetime, timedelta
import asyncio

timeout_users = {}
class TimeoutCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="timeout", description="⏳ กำหนดเวลาหมดสิทธิ์พูดคุยในเซิร์ฟเวอร์ (เป็นวินาที)")
    async def timeout(self, ctx, member: nextcord.Member, duration: int, *, reason: str = "ไม่มีเหตุผล"):
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send("⛔ คุณไม่มีสิทธิ์ใช้งานคำสั่งนี้")
            return
        timeout_until = datetime.utcnow() + timedelta(seconds=duration)
        timeout_users[member.id] = timeout_until
        await member.timeout(timedelta(seconds=duration), reason=reason)
        await ctx.send(f"⏳ {member.mention} ถูกหมดสิทธิ์พูดคุย ({duration} วินาที)")
        log_channel = self.bot.get_channel(1347202924568121349)
        if log_channel:
            embed = nextcord.Embed(
                title="⏳ การหมดสิทธิ์พูดคุย (Timeout)",
                description=f"**{member.mention}** ถูก Timeout โดย {ctx.author.mention}",
                color=0xffa500
            )
            embed.add_field(name="เหตุผล", value=reason, inline=False)
            embed.add_field(name="เวลาหมดอายุ", value=timeout_until.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
            await log_channel.send(embed=embed)
        await self.remove_timeout_after(duration, member, timeout_until)

    async def remove_timeout_after(self, duration, member, timeout_until):
        wait_time = (timeout_until - datetime.utcnow()).total_seconds()
        await asyncio.sleep(wait_time)
        if member.id in timeout_users:
            await member.timeout(None, reason="หมดเวลาการ Timeout")
            del timeout_users[member.id]
            log_channel = self.bot.get_channel(1347202924568121349)
            if log_channel:
                embed = nextcord.Embed(
                    title="⏳ การยกเลิกการ Timeout",
                    description=f"**{member.mention}** การหมดสิทธิ์พูดคุยหมดอายุแล้วและถูกยกเลิก",
                    color=0x00ff00
                )
                await log_channel.send(embed=embed)

def setup(bot):
    bot.add_cog(TimeoutCommand(bot))
