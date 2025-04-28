from nextcord.ext import commands
import nextcord

class RuleCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rule(self, ctx, number: int):
        rules = {
            1: {
                "title": "กฎข้อที่ 1: เรื่องที่ทุกคนต้องรู้",
                "description": "เจ้าของเซิร์ฟ และ แอดมิน ถูกเสมอ",
                "color": 0x2ecc71
            },
            2: {
                "title": "กฎข้อที่ 2: เนื้อหาความรุนแรง",
                "description": "ห้ามส่งคลิปที่มีความรุนแรง ฆตต และอื่นๆ",
                "color": 0x2ecc71
            },
            3: {
                "title": "กฎข้อที่ 3: ลิ้ง",
                "description": "ห้ามส่งลิ้ง แปลกปลอมหรือลิ้งใดๆ ในช่องที่ไม่อนุญาติ",
                "color": 0x2ecc71
            },
            4: {
                "title": "กฎข้อที่ 4: สแปม",
                "description": "ห้ามสแปม ข้อความ, วิดีโอ, ลิ้ง",
                "color": 0x2ecc71
            },
            5: {
                "title": "กฎข้อที่ 5: เหยียดเพศ",
                "description": "ห้ามเหยียดเพศ",
                "color": 0x2ecc71
            },
            6: {
                "title": "กฎข้อที่ 6: บูลลี่",
                "description": "ห้ามบูลลี่",
                "color": 0x2ecc71
            },
            7: {
                "title": "กฎข้อที่ 7: เนื้อหา 18+",
                "description": "ไม่ส่งข้อความ/ลิงก์/รูป/วิดีโอ NSFW หรือเนื้อหา 18+",
                "color": 0x2ecc71
            },
            8: {
                "title": "กฎข้อที่ 8: เกี่ยวกับคำหยาบ",
                "description": "ใช้คำหยาบได้แต่อย่าแรงเกินไป",
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
            title="ฝ่าฝืนกฎ",
            description="นิดเดียว โดนเตือน/ทำบ่อยๆ เตือนแล้วก็ไม่เลิก โดนแบน",
            color=0xFF0000
        )
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RuleCommand(bot))
