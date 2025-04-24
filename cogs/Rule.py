from nextcord.ext import commands
import nextcord

class RuleCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rule(self, ctx, number: int):
        rules = {
            1: {
                "title": "กฎข้อที่ 1: เรื่องที่ทุกคนต้องรู้ ||Things everyone should know||",
                "description": "เจ้าของเซิร์ฟ และ แอดมิน ถูกเสมอ\nOwner and Admin are always right.",
                "color": 0x2ecc71
            },
            2: {
                "title": "กฎข้อที่ 2: เนื้อหาความรุนแรง ||Violent content||",
                "description": "ห้ามส่งคลิปที่มีความรุนแรง ฆตต และอื่นๆ\nDo not send clips containing violence, murder, and others.",
                "color": 0x2ecc71
            },
            3: {
                "title": "กฎข้อที่ 3: ลิ้ง ||Links||",
                "description": "ห้ามส่งลิ้ง แปลกปลอมหรือลิ้งใดๆ ในช่องที่ไม่อนุญาติ\nDo not send suspicious links or any links in unauthorized channels.",
                "color": 0x2ecc71
            },
            4: {
                "title": "กฎข้อที่ 4: สแปม ||Spam||",
                "description": "ห้ามสแปม ข้อความ, วิดีโอ, ลิ้ง\nDo not spam messages, videos, or links.",
                "color": 0x2ecc71
            },
            5: {
                "title": "กฎข้อที่ 5: เหยียดเพศ ||Gender||",
                "description": "ห้ามเหยียดเพศ\nDo not discriminate based on gender.",
                "color": 0x2ecc71
            },
            6: {
                "title": "กฎข้อที่ 6: บูลลี่ ||Bully||",
                "description": "ห้ามบูลลี่\nDo not bully.",
                "color": 0x2ecc71
            },
            7: {
                "title": "กฎข้อที่ 7: เนื้อหา 18+ ||18+ content||",
                "description": "ไม่ส่งข้อความ/ลิงก์/รูป/วิดีโอ NSFW หรือเนื้อหา 18+\nDo not send NSFW messages/links/images/videos or 18+ content.",
                "color": 0x2ecc71
            },
            8: {
                "title": "กฎข้อที่ 8: เกี่ยวกับคำหยาบ ||Profanity||",
                "description": "ใช้คำหยาบได้แต่อย่าแรงเกินไป\nYou may use profanity, but keep it moderate.",
                "color": 0x2ecc71
            },
        }

        rule = rules.get(number)
        if not rule:
            await ctx.send(f"ไม่มีกฎข้อที่ {number} นะคะ!")
            return
        
        embed = nextcord.Embed(
            title=rule["title"],
            description=rule["description"],
            color=rule["color"]
        )
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def warning(self, ctx):
        embed = nextcord.Embed(
            title="ฝ่าฝืนกฎ ||Breaking the Rules||",
            description="นิดเดียว โดนเตือน / ทำบ่อยๆ เตือนแล้วก็ไม่เลิก โดนแบน\nMinor offenses will receive a warning. Repeated violations after warnings will result in a ban.",
            color=0xFF0000
        )
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RuleCommand(bot))
