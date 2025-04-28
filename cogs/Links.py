import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ButtonStyle
from nextcord.ui import Button, View, Modal, TextInput
import qrcode, aiohttp,io
import random, string, time

class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # สร้าง embed + ปุ่ม
    @commands.command()
    async def links(self, ctx):
        embed = nextcord.Embed(
            title="Links Tools",
            description="เลือกเครื่องมือที่ต้องการ",
            color=0x8A2BE2
        )
        embed.set_image(url="http://upload-image.free.nf/files/1745683162_Untitled14_20250426225834.png")
        view = View()

        # ปุ่มที่ 1: ย่อลิ้ง
        shorten_button = Button(label="ย่อลิ้ง", style=ButtonStyle.primary)
        shorten_button.callback = self.shorten_link_modal
        view.add_item(shorten_button)

        # ปุ่มที่ 2: สร้าง QR Code
        qr_button = Button(label="สร้าง QR Code", style=ButtonStyle.secondary)
        qr_button.callback = self.qr_modal
        view.add_item(qr_button)

        await ctx.send(embed=embed, view=view)

    # Modal สำหรับย่อลิ้ง
    async def shorten_link_modal(self, interaction: Interaction):
        class ShortenModal(Modal):
            def __init__(self):
                super().__init__("ย่อลิ้ง URL", timeout=300)
                self.url = TextInput(label="วางลิ้งที่ต้องการย่อ", required=True)
                self.add_item(self.url)

            async def callback(self, interaction: Interaction):
                link = self.url.value
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://tinyurl.com/api-create.php?url={link}") as resp:
                        short_link = await resp.text()
                await interaction.response.send_message(f"`🔗` **ลิ้งที่ย่อแล้ว:** ```{short_link}```", ephemeral=True)
        await interaction.response.send_modal(ShortenModal())

    # Modal สำหรับสร้าง QR
    async def qr_modal(self, interaction: Interaction):
        class QRModal(Modal):
            def __init__(self):
                super().__init__("สร้าง QR Code", timeout=300)
                self.url = TextInput(label="วางลิ้งที่ต้องการสร้าง QR", required=True)
                self.add_item(self.url)

            async def callback(self, interaction: Interaction):
                link = self.url.value
                qr = qrcode.make(link)
                buffer = io.BytesIO()
                qr.save(buffer, format="PNG")
                buffer.seek(0)

                random_text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
                timestamp = int(time.time())
                file = nextcord.File(buffer, filename=f"{random_text}_{timestamp}.png")
                await interaction.response.send_message(content="นี่คือ QR Code ของคุณ", file=file, ephemeral=True)
        await interaction.response.send_modal(QRModal())

def setup(bot):
    bot.add_cog(Links(bot))
