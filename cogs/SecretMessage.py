import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Embed
from nextcord.ui import View, Button, Modal, TextInput, UserSelect
from nextcord import ButtonStyle, TextInputStyle, SelectOption

CHANNEL_ID = 1360658365016965273
ADMIN_LOG_CHANNEL_ID = 1358806674617401514

class AskMessageModal(Modal):
    def __init__(self, target_user):
        super().__init__("ฝากข้อความลับ")
        self.target_user = target_user

        self.msg = TextInput(
            label="ข้อความลับถึงเขา",
            placeholder="พิมพ์ข้อความที่อยากบอก",
            style=TextInputStyle.paragraph,
            required=True
        )
        self.hint = TextInput(
            label="คำใบ้ (ถ้ามี)",
            placeholder="...",
            style=TextInputStyle.short,
            required=False
        )
        self.add_item(self.msg)
        self.add_item(self.hint)

    async def callback(self, interaction: Interaction):
        channel = interaction.client.get_channel(CHANNEL_ID)
        admin_channel = interaction.client.get_channel(ADMIN_LOG_CHANNEL_ID)

        hint_text = self.hint.value if self.hint.value.strip() else " ~~เขาไม่บอกคำใบ้ ❌~~"

        embed = Embed(
            title="💌 มีคนฝากข้อความถึงคุณ!",
            description=f"**ข้อความ:**\n{self.msg.value}",
            color=0x2F3136
        )
        embed.add_field(name="🔍 คำใบ้", value=hint_text, inline=False)
        embed.set_footer(text="SECRET MESSAGE")
        await channel.send(content=self.target_user.mention, embed=embed)

        admin_embed = Embed(
            title="🕵️‍♀️ มีการฝากข้อความลับ",
            description=(f"**ผู้ส่ง:** {interaction.user.mention} (`{interaction.user.id}`)\n"
                         f"**ถึง:** {self.target_user.mention} (`{self.target_user.id}`)"),
            color=0xff4b4b
        )
        admin_embed.add_field(name="📩 ข้อความ", value=self.msg.value, inline=False)
        admin_embed.add_field(name="🧩 คำใบ้", value=hint_text, inline=False)
        admin_embed.set_footer(text="SECRET ADMIN LOGS ONLY")

        if admin_channel:
            await admin_channel.send(embed=admin_embed)

        await interaction.response.send_message("✅ ฝากข้อความเรียบร้อยแล้ว", ephemeral=True)

class SelectTarget(UserSelect):
    def __init__(self):
        super().__init__(
            placeholder="เลือกคนที่อยากฝากบอก",
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction: Interaction):
        selected_user = self.values[0]
        if not selected_user:
            await interaction.response.send_message("❌ ไม่พบผู้ใช้นี้ในเซิร์ฟเวอร์", ephemeral=True)
            return
        await interaction.response.send_modal(AskMessageModal(selected_user))

class SendMessageButton(Button):
    def __init__(self, members):
        super().__init__(label="📩", style=ButtonStyle.primary)
        self.members = members

    async def callback(self, interaction: Interaction):
        view = View(timeout=60)
        view.add_item(SelectTarget())
        await interaction.response.send_message("เลือกคนที่คุณต้องการ~", view=view, ephemeral=True)

class SelectorView(View):
    def __init__(self, members):
        super().__init__(timeout=None)
        self.members = members
        self.add_item(SendMessageButton(self.members))

class SecretMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendm(self, ctx):
        members = ctx.guild.members
        embed = Embed(
            title="ระบบฝากข้อความ",
            description=(
                "## ระบบฝากบอกหากคุณต้องการบอกความในใจ\n"
                "แต่__ไม่อยากให้เขา__รู้ คุณสามารถฝากบอกโดยใช้**คำใบ้**แทนได้\n"
                "🟢 ใช้งานง่าย ๆ:\n"
                "1. กดปุ่ม\n2. เลือกชื่อผู้รับ\n3. ใส่ข้อความเลย\n4. ใส่คำใบ้ (หรือไม่ก็ได้)\n5. กดส่ง\n\n"
            ),
            color=0x2F3136
        )
        embed.set_image(url="https://i.pinimg.com/originals/65/fc/d5/65fcd516737531272067da08d6dd6b15.gif")
        embed.set_footer(text="SECRET MESSAGE")
        await ctx.send(embed=embed, view=SelectorView(members))
        try:
            await ctx.message.delete()
        except:
            pass

def setup(bot):
    bot.add_cog(SecretMessage(bot))
