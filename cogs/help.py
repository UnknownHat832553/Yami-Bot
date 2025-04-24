from nextcord.ext import commands
import nextcord

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        embed = nextcord.Embed(
            title="🛠 คำสั่งที่มีอยู่ในบอท",
            description="คำสั่งทั้งหมดที่สามารถใช้ได้ในตอนนี้:",
            color=nextcord.Color.blue()
        )

        embed.add_field(name="!help", value="แสดงหน้านี้แหละ~", inline=False)
        embed.add_field(name="!clear [จำนวน]", value="ลบข้อความในช่องแชท", inline=False)
        embed.add_field(name="!rule [1-8] & !warning", value="บอกกฏ และ บอกว่าทำผิดได้อะไร", inline=False)
        embed.add_field(name="!sendm", value="แสดงหน้าต่างส่งข้อความลับ", inline=False)
        embed.add_field(name="!timeout <@สมาชิก> <ระยะเวลา(วินาที)> [เหตุผล]", value="คนที่โดน Timeout จะถูกทำให้เงียบ", inline=False)
        embed.add_field(name="/allow_link", value="เพิ่มคนที่สามารถส่งลิงก์ได้", inline=False)
        embed.add_field(name="/disallow_link", value="นำสิทธิ์ส่งลิงก์ออก", inline=False)
        embed.add_field(name="!random", value="สุ่มรูปภาพ", inline=False)
        embed.add_field(name="!rolegame", value="ระบบรับยศเกม", inline=False)
        embed.add_field(name="!setstatus", value="ตั้งค่าช่องดูสถานะเซิร์ฟเวอร์", inline=False)
        
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommand(bot))
