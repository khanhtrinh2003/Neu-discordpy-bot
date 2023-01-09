import discord
from discord import app_commands
import typing
from typing import List
import matplotlib.pyplot as plt


#import module

from Data_handling.tkb22_23 import room, hoc_ke
from Notification.noti import news
from Game.game import Game_theo, DoanSo
from Chatbot.chatbot import AI_BOT

TOKEN = '' # Put toke in here
ServerID = "919927035558764574"# Put toke in here

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=ServerID))
        self.synced = True
        print('Bot has connected to Discord!')

bot = abot()
tree = app_commands.CommandTree(bot)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    channel = ["chatbot", "testbot"]
    if message.channel.name in channel :
        await message.channel.send(AI_BOT(message.content))       

# Feature 1
@tree.command(
    name='confess', 
    description='Nhắn tin ẩn danh', 
    guild=discord.Object(id=ServerID)
    )

@app_commands.describe(message='Nhập tin nhắn', file='Gửi hình hoặc file')

async def confess(interaction: discord.Interaction, message: str, file: typing.Optional[discord.Attachment]):
    await interaction.response.send_message('......', ephemeral=True, delete_after=0.000000000000000000000000000000001)
    await interaction.channel.send(f'{message}')
    await interaction.channel.send(file)

    
# Feature 2
@tree.command(
    name='tim_phong', 
    description='Tìm phòng ở NEU',
    guild=discord.Object(id=919927035558764574)
    )

@app_commands.describe(
    days="Nhập thứ trong tuần", 
    period="Nhập tiết học", 
    floors="Nhập tầng học", 
    building="Nhập tòa nhà")

@app_commands.choices(
    days = [
        app_commands.Choice(name="Thứ 2", value="Thứ Hai"),
        app_commands.Choice(name="Thứ 3", value="Thứ Ba"),
        app_commands.Choice(name="Thứ 4", value="Thứ Tư"),
        app_commands.Choice(name="Thứ 5", value="Thứ Năm"),
        app_commands.Choice(name="Thứ 6", value="Thứ Sáu"),
        app_commands.Choice(name="Thứ 7", value="Thứ Bảy"), 
        ],
    
    period = [
        app_commands.Choice(name="Tiết 1-2", value="(1-2)"),
        app_commands.Choice(name="Tiết 3-4", value="(3-4)"),
        app_commands.Choice(name="Tiết 5-6", value="(5-6)"),
        app_commands.Choice(name="Tiết 7-8", value="(7-8)"),
        app_commands.Choice(name="Tiết 9-10", value="(9-10)"),
        ],

    floors=[
        app_commands.Choice(name="Tầng 1", value="1"),
        app_commands.Choice(name="Tầng 2", value="2"),
        app_commands.Choice(name="Tầng 3", value="3"),
        ],

    building=[
        app_commands.Choice(name="Tòa A2", value="A2"),
        app_commands.Choice(name="Tòa B", value="B"),
        app_commands.Choice(name="Tòa C", value="C"),
        app_commands.Choice(name="Tòa D", value="D"),
        ],
)

async def timphong(
    interaction: discord.Interaction, 
    days: app_commands.Choice[str],
    period:app_commands.Choice[str] , 
    building: app_commands.Choice[str], 
    floors: app_commands.Choice[str]
    ):

    res = room(days.value, period.value, building.value, floors.value)
    embedVar = discord.Embed(title="Các phòng có người học", description=res, color=0x15E3E0)
    await interaction.response.send_message(embed=embedVar, ephemeral=True)    

# Feature 3
@tree.command(
    name='hoc_ke', 
    description='Học ké ở NEU',
    guild=discord.Object(id=919927035558764574)
    )

@app_commands.describe()

@app_commands.choices()

async def ke(
    interaction: discord.Interaction, 
    mon: str,
    ):

    res = hoc_ke(mon)
    embedVar = discord.Embed(title="Các lớp có thể học ké:", description=res, color=0x15E3E0)
    await interaction.response.send_message(embed=embedVar, ephemeral=True)    


# Feature 4
@tree.command(
    name='thongbao', 
    description='Thông báo', 
    guild=discord.Object(id=ServerID)
    )

@app_commands.choices(
    thong_tin = [
        app_commands.Choice(name="NEU", value="NEU"),
        app_commands.Choice(name="Kinh tế", value="Kinh tế"),
        app_commands.Choice(name="Economics", value="Economics"),
        ],
    )

@app_commands.describe(thong_tin="Chọn thông tin bạn muốn biết", num="Số lượng thông báo")

async def news(interaction: discord.Interaction, thong_tin : app_commands.Choice[str], num: int):
    await interaction.response.send_message('......', ephemeral=True, delete_after=0.000000000000000000000000000000001)
    await interaction.channel.send(news(thong_tin.value, num))

# Feature 5
@tree.command(
    name='guess', 
    description='Đoán số nằm trong khoản 0->100', 
    guild=discord.Object(id=ServerID)
    )

@app_commands.describe(num="Nhập số")

async def self(interaction: discord.Interaction, num: int):
    await interaction.response.send_message('......', ephemeral=True, delete_after=0.000000000000000000000000000000001)
    await interaction.channel.send(DoanSo(num).play())

# Feature 6
@tree.command(
    name='chien_luoc_nguoi_2', 
    description='Chiến lược tối ưu cho người 2', 
    guild=discord.Object(id=ServerID)
    )

@app_commands.describe(p1="Chọn chiến lược cho người 1", p2="Chọn chiến lược cho người 2")
async def self(interaction: discord.Interaction, p1: float, p2: float):
    await interaction.response.send_message(Game_theo(p1, p2).chien_luoc())
    image = discord.File("test.png")
    Game_theo(p1, p2).minh_hoa()
    plt.savefig("test.png")
    plt.close()
    await interaction.channel.send(file=image)

    image1 = discord.File("test1.png")
    Game_theo(p1, p2).mat_do_loi_nhuan()
    plt.savefig("test1.png")
    plt.close()
    await interaction.channel.send(file=image1)



# Help
@tree.command(
    name='help', 
    description='Trợ giúp', 
    guild=discord.Object(id=ServerID)
    )

async def help(interaction: discord.Interaction):
    embedIn = discord.Embed(title="Welcome To BOTO", description="**Commands:**", color=0x00eeff)
    embedIn.set_author(name="From KT with luv <3", icon_url="")
    embedIn.set_thumbnail(url="https://cdn.discordapp.com/emojis/754600266288070806.png?v=1")
    embedIn.add_field(name="1) '/confess'", value="Nhắn tin ẩn danh", inline=False)
    embedIn.add_field(name="2) '/tim_phong'", value="Tìm các phòng trống ở NEU", inline=False)
    embedIn.add_field(name="3) '/hoc_ke'", value="Học ké NEU", inline=False)
    embedIn.add_field(name="4) '/thongbao'", value="Lấy thông báo", inline=False)
    embedIn.add_field(name="5) '/guess'", value="Chơi đoán số", inline=False)
    embedIn.add_field(name="6) '/keo_bua_bao'", value="Chơi kéo búa bao", inline=False)
    embedIn.set_footer(text="Have a good day :)))")
    await interaction.response.send_message(embed = embedIn)

def generate_response(prompt, temperature):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000, # 4000 is the maximum number of tokens for the davinci 003 GPT3 model
        n=1,
        stop=None,
        temperature=temperature,
    )

    if 'error' in completions:
        return completions['error']['message']
    else:
        message = completions.choices[0].text
    if '!image' in prompt:
        return message
    else:
        return message

bot.run(TOKEN)
