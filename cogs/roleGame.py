import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Button

gameZone = 1362643842947354724
Mine = 1362644006726668448
FF = 1362644072497418360
Valo = 1362644225992298507
Roblox = 1362647100541763604
ROV = 1362647291315622059
PUBG = 1362647422496538785

class RoleView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(self.create_role_button("GameZone", nextcord.PartialEmoji(name="gamezone", id=1352645240917594163), 1362643842947354724))
        self.add_item(self.create_role_button("Minecraft", nextcord.PartialEmoji(name="mine", id=1352229175964078180), 1362644006726668448))
        self.add_item(self.create_role_button("FreeFire", nextcord.PartialEmoji(name="ff", id=1352228437913374735), 1362644072497418360))
        self.add_item(self.create_role_button("Valorant", nextcord.PartialEmoji(name="valo", id=1352308615444434944), 1362644225992298507))
        self.add_item(self.create_role_button("Roblox", nextcord.PartialEmoji(name="roblox", id=1352227651825303582), 1362647100541763604))
        self.add_item(self.create_role_button("ROV", nextcord.PartialEmoji(name="rov", id=1352228946070212610), 1362647291315622059))
        self.add_item(self.create_role_button("PUBG", nextcord.PartialEmoji(name="pubg", id=1352308413622653058), 1362647422496538785))


    def create_role_button(self, label, emoji, role_id):
        async def callback(interaction: nextcord.Interaction):
            role = interaction.guild.get_role(role_id)
            if not role:
                await interaction.response.send_message("ไม่พบยศ! ตรวจสอบ role_id ด้วยนะ!", ephemeral=True)
                return
            if role in interaction.user.roles:
                await interaction.response.send_message(f"⚠️ คุณมียศ `{role.name}` อยู่แล้ว", ephemeral=True)
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"✅ เพิ่มยศ `{role.name}` เรียบร้อยแล้ว~", ephemeral=True)

        button = Button(label=label, style=nextcord.ButtonStyle.gray, emoji=emoji)
        button.callback = callback
        return button

    @nextcord.ui.button(label="เช็คยศ", style=nextcord.ButtonStyle.gray, emoji="⚙")
    async def check_role(self, button: Button, interaction: nextcord.Interaction):
        role_map = {
            1362643842947354724,
            1362644006726668448,
            1362644072497418360,
            1362644225992298507,
            1362647100541763604,
            1362647291315622059,
            1362647422496538785
        }
        roles = [
            f"{interaction.guild.get_role(role_id).name}"
            for role_id in role_map.items()
            if nextcord.utils.get(interaction.user.roles, id=role_id)
        ]
        role_list = ", ".join(roles) if roles else "ไม่มีบทบาทในนี้"
        await interaction.response.send_message(f"🎮 ยศในนี้ของคุณ: `{role_list}`", ephemeral=True)

class RoleGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rolegame(self, ctx):
        guild = ctx.guild
        icon_url = guild.icon.url if guild.icon else None
        embed = nextcord.Embed(
            title="**ระบบรับยศ __GAME Zone__**",
            description=(
                "`🟢` **รับยศ ช่องหมวดหมู่เกม**\n"
                "- กดปุ่มด้านล่างเพื่อรับยศ\n"
                "- ผู้สร้าง: **Mr Emptiness**\n"
                "- ```discord.gg/x3XkCBswvY```"
            ),
            color=0x780cc5
        )
        if icon_url:
            embed.set_thumbnail(url=icon_url)
        embed.set_image(url="http://upload-image.free.nf/files/1744953596_Untitled10_20250418121914.png")
        embed.set_footer(text=f"รับยศด้วยนะ~")
        await ctx.send(embed=embed, view=RoleView())
        try:
            await ctx.message.delete()
        except:
            pass

def setup(bot):
    bot.add_cog(RoleGame(bot))
