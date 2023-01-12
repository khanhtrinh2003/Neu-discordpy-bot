import discord
from discord import app_commands
import typing
from typing import List
import matplotlib.pyplot as plt


#import module

from Schedule.tkb22_23 import room, hoc_ke
from Notification.noti import news
from Game.game import Game_theo, DoanSo
from Chatbot.chatbot import AI_BOT, Code, Image, Chat

TOKEN = '' # Put toke in here
ServerID = "919927035558764574"# Put serverid

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await tree.sync()
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
    )

@app_commands.describe(message='Nhập tin nhắn', file='Gửi hình hoặc file')

async def confess(interaction: discord.Interaction, message: str, file: typing.Optional[discord.Attachment]):    
    if interaction.guild.id in ServerID:
        await interaction.response.send_message('......', ephemeral=True, delete_after=0.000000000000000000000000000000001)
        await interaction.channel.send(f'{message}')
        await interaction.channel.send(file)

    
# Feature 2
@tree.command(
    name='tim_phong', 
    description='Tìm phòng ở NEU',
    
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
    if interaction.guild.id in ServerID:
        res = room(days.value, period.value, building.value, floors.value)
        embedVar = discord.Embed(title="Các phòng có người học", description=res, color=0x15E3E0)
        await interaction.response.send_message(embed=embedVar, ephemeral=True)    

# Feature 3
@tree.command(
    name='hoc_ke', 
    description='Học ké ở NEU',
    
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
    
    )

@app_commands.describe(num="Nhập số")

async def self(interaction: discord.Interaction, num: int):
    await interaction.response.send_message('......', ephemeral=True, delete_after=0.000000000000000000000000000000001)
    await interaction.channel.send(DoanSo(num).play())

# Feature 6
@tree.command(
    name='chien_luoc', 
    description='Chiến lược', 
    
    )

@app_commands.describe(p="Chọn chiến lược")
async def self(interaction: discord.Interaction, p: float):
    rep = Game_theo(p,interaction.user).mat_do_loi_nhuan()

    if rep=="Đã ghi nhận dữ liệu":
        await interaction.response.send_message(f"Đã ghi nhận dữ liệu của {interaction.user}")
    else:
        with open("test.png", "rb") as fh:
            await interaction.response.send_message(file = discord.File(fh, filename="test.png"))

# Feature 7
@tree.command(
    name='code', 
    description='Giải đáp về code', 
    
    )

@app_commands.describe(tin_nhan="Nhập tin nhắn")

async def self(interaction: discord.Interaction, tin_nhan: str):
    await interaction.response.send_message(tin_nhan, ephemeral=True) 
    await interaction.channel.send(Code(tin_nhan))

# Feature 7
@tree.command(
    name='image', 
    description='Hình ảnh', 
    
    )

@app_commands.describe(tin_nhan="Nhập tin nhắn")

async def self(interaction: discord.Interaction, tin_nhan: str):
    await interaction.response.send_message(tin_nhan, ephemeral=True) 
    await interaction.channel.send(Image(tin_nhan))

# Feature 8
@tree.command(
    name='chat', 
    description='Chat với Bot', 
    
    )

@app_commands.describe(tin_nhan="Nhập tin nhắn")

async def self(interaction: discord.Interaction, tin_nhan: str):
    await interaction.response.send_message(tin_nhan, ephemeral=True)    
    await interaction.channel.send(Chat(tin_nhan))

bot.run(TOKEN)
