import os
import discord
from discord.ext import commands
import neverSleep
import random
import emoji
from discord.utils import get
from datetime import datetime
from time import sleep
from easy_pil import Editor, load_image_async, Font
from discord import File

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="?info ", intents=intents)


@bot.event
async def on_ready():
    # Settting 'Watching' status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="?info help"
        )
    )

    print(emoji.emojize("Ready:red_heart:", variant="emoji_type"))
    em = discord.Embed(
        title="Bot is online ❗",
        description=f"{bot.user.mention} is ready to work use ?info help",
        color=0x3498DB,
    )
    background = Editor("logs2.png")
    logs = File(fp=background.image_bytes, filename="wlc2.jpg")
    await bot.get_channel(987680823388041336).send(file=logs)

    await bot.get_channel(987680823388041336).send(embed=em)


bot.remove_command("help")


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description="Use ?info help <command> for extended information",
        color=0xE74C3C,
    )

    em.add_field(name="Minecraft Server", value="Smp\nIp,\nTutorial,")
    em.add_field(name="Discord server", value="Jokes\nCredits\nChannels\nComp\nRoles")
    em.add_field(name="Moderation", value="Kick\nBan\nMute")

    await ctx.send(embed=em)

    await ctx.send(embed=em)


@help.command(invoke_without_command=True)
async def ip(ctx):
    em = discord.Embed(
        title="IP", description="Gives you the ip of the minecraft server "
    )

    await ctx.send(embed=em)


@help.command(invoke_without_command=True)
async def tutorial(ctx):
    em = discord.Embed(
        title="Tutorial",
        description="Gives you recommended youtube videos which would help you to join the sever",
    )

    await ctx.send(embed=em)


@help.command(invoke_without_command=True)
async def joke(ctx):
    em = discord.Embed(title="Jokes", description="Tells you about your life")

    await ctx.send(embed=em)


@bot.command()
async def jokes(ctx):
    jokes_responses = [
        "Your life",
        "Sone De na yaar",
        "Nahi",
        "My wife told me she'll slam my head on the keyboard if I don't get off the computer. I'm not too worried, I think she's   jokinlkjhfakljn m,.nbziyoao78yv87dfaoyuofaytdf",
        "My wife left a Note on the Fridge saying'It isnt working 'I dont understand what she's trying to say .I opened the fridge and its working fine",
    ]
    await ctx.reply(f"{random.choice(jokes_responses)}")


@bot.command(name="smp")
async def smp_(ctx):
    embed = discord.Embed(
        title="SMP", description="HELLO BABY", color=discord.colour.blue()
    )

    await ctx.send(embed=embed)


@bot.command()
async def credits(ctx):
    embed = discord.Embed(title="hello")
    embed.set_author(
        name="The Eiffel Tower",
        icon_url="https://discord.com/channels/@me/955758430675693569/988108616064204800s",
    )

    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(
            title="Command does not exist ❗ ",
            description="This command is not available right now use '?info help' to know all of my commands",
            color=0xE74C3C,
        )

        msg = await ctx.send(embed=em)
        await ctx.message.delete()
        sleep(2.5)
        await msg.delete()


@bot.command(name="ip")
async def ip_(ctx):
    em = discord.Embed(
        title="IP",
        description="Use this IP to join the Minecraft server",
        color=0x1ABC9C,
    )

    em.add_field(
        name="JAVA☕",
        value="mrtriangleop3.aternos.me:34059",
    )
    em.add_field(
        name="BEDROCK ",
        value="mrtriangleop3.aternos.me:34059",
    )

    msg = await ctx.send(embed=em)
    await ctx.message.delete()
    await ctx.delete(msg)


@bot.command()
async def hi(self, ctx):
    await ctx.send("http://imgur.com/gallery/YiMUiop")


@bot.event
async def on_disconnect(ctx):
    await ctx.bot.get_channel(987680823388041336).send("Bot Dissconected")


@bot.group(invoke_without_command=True)
async def comp(ctx):
    em = discord.Embed(
        title="Competition",
        description="Use ?info help <competition> for extended information",
    )

    em.add_field(name="Ongoing Competition", value="None")
    em.add_field(name="Upcoming Competition", value="chess")

    await ctx.send(embed=em)


@comp.command()
async def Chess(ctx):
    em = discord.embed(
        title="Chess.com",
        description="Chess competition will be conducted on 15.4.22 at 3:00PM IST Winner Will get a pizza from Brended",
        color=FF0000,
    )

    em.add_field(name="**Syntax**", value="?info Upcoming Competition")

    await ctx.send(embed=em)


@bot.command(name="Chess")
async def Chess_(ctx):
    await ctx.reply(
        "Chess competition will be conducted on 15.4.22 at 3:00PM IST Winner Will get a pizza from Brended",
        color=0x1ABC9C,
    )


@bot.command(aliases=["k"])
@commands.has_permissions(kick_members=True)
async def kick(
    ctx, member: discord.Member, *, reason="No reason provided by the admin"
):
    await member.send("You have been kicked from Eiffel Tower, Because :" + reason)

    await member.kick(reason=reason)


@bot.command(aliases=["b"])
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    banEmbed = discord.Embed(
        title=f"{member.mention}You have been banned from The Eiffel tower",
        description=f"You were banned by an admin{ctx.author.mention}\nReason Provided :"
        + reason,
        color=0xE74C3C,
    )
    await ctx.channel.send(
        f"{member.name} has been banned by {ctx.author.name} because=" + reason
    )

    await member.send(embed=banEmbed)

    await member.ban(reason=reason)


@bot.command(aliases=["c"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f"**{amount}** messages have been deleted")


@bot.command()
async def hello(ctx):
    await ctx.channel.send(
        f"Hello ! Nice to meet  you {ctx.author.mention} how are you all i am {bot.user.mention} "
    )


@bot.event
async def on_raw_reaction_add(payload):
    ourMessageID = 987303228511223862
    YourMessageID = 987314195739574294

    if YourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == "☕":
            role = discord.utils.get(guild.roles, name="Hooman")
            await member.add_roles(role)

        if emoji == "☕":
            role = discord.utils.get(guild.roles, name="Member")
            await member.remove_roles(role)

    if ourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == "💬":
            role = discord.utils.get(guild.roles, name="C++")
            await member.add_roles(role)
        if emoji == "🐍":
            role = discord.utils.get(guild.roles, name="Python")
            await member.add_roles(role)
            await bot.get_channel(980737608349016096).send(
                f"{member.mention} says print('Hello Guys')\n**Hello World**"
            )
        if emoji == "☕":
            role = discord.utils.get(guild.roles, name="java")
            await member.add_roles(role)

        if emoji == "🏳️‍⚧️":
            role = discord.utils.get(guild.roles, name="LGBTQ+")

            await member.add_roles(role)
        if emoji == "♀️":
            role = discord.utils.get(guild.roles, name="Female")
            await member.add_roles(role)
        if emoji == "♂️":
            role = discord.utils.get(guild.roles, name="Male")
            await member.add_roles(role)
        if emoji == "❎":
            role = discord.utils.get(guild.roles, name="18-")
            await member.add_roles(role)
        if emoji == "✅":
            role = discord.utils.get(guild.roles, name="18+")
            await member.add_roles(role)
        if emoji == "🖥":
            role = discord.utils.get(guild.roles, name="Blender")
            await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    ourMessageID = 987303228511223862
    YourMessageID = 987314195739574294

    if YourMessageID == payload.message_id:
        guild = await bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)

        emoji = payload.emoji.name
        if emoji == "☕":
            role = discord.utils.get(guild.roles, name="Hooman")
            await member.remove_roles(role)

    if ourMessageID == payload.message_id:
        guild = await bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)

        emoji = payload.emoji.name
        if emoji == "💬":
            role = discord.utils.get(guild.roles, name="C++")
            await member.remove_roles(role)
        if emoji == "🐍":
            role = discord.utils.get(guild.roles, name="Python")
            await member.remove_roles(role)
        if emoji == "☕":
            role = discord.utils.get(guild.roles, name="java")
            await member.remove_roles(role)

        if emoji == "🏳️‍⚧️":
            role = discord.utils.get(guild.roles, name="LGBTQ+")

            await member.remove_roles(role)
        if emoji == "♀️":
            role = discord.utils.get(guild.roles, name="Female")
            await member.remove_roles(role)
        if emoji == "♂️":
            role = discord.utils.get(guild.roles, name="Male")
            await member.remove_roles(role)
        if emoji == "❎":
            role = discord.utils.get(guild.roles, name="18-")
            await member.remove_roles(role)
        if emoji == "✅":
            role = discord.utils.get(guild.roles, name="18+")
            await member.remove_roles(role)
        if emoji == "🖥":
            role = discord.utils.get(guild.roles, name="Blender")
            await member.remove_roles(role)

    if member is not None:
        await member.remove_roles(role)
    else:
        print("Member not found")


@bot.command(pass_context=True)
async def roles(ctx):
    embed = discord.Embed(
        title="Please select your preffered ",
        description="Please react to the specified emoji",
        url="https://youtu.be/dQw4w9WgXcQ",
        timestamp=datetime.now(),
        color=0x3498DB,
    )
    embed.add_field(name="Coding", value="🐍 - **Python**\n**Java** -󠁪󠁪☕󠁩󠁤󠁪󠁷\n**C**=💬 ")
    embed.add_field(
        name="Genders", value=" **Male** = ♂️\n**Female** = ♀️\n**LGBTQ+**=🏳️‍⚧️"
    )
    embed.add_field(name="Age", value=" **18-** = ❎\n**18+** = ✅")
    embed.add_field(name="Blender", value="**Blender** = 🖥 ")

    msg = await ctx.send(embed=embed)

    await msg.add_reaction("🐍")
    await msg.add_reaction("☕")
    await msg.add_reaction("💬")
    await msg.add_reaction("♂️")
    await msg.add_reaction("♀️")
    await msg.add_reaction("🏳️‍⚧️")
    await msg.add_reaction("🔞")
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")
    await msg.add_reaction("🖥")


@bot.event
async def on_message(message):
    if message.content == "Aaheli":
        action_responses = [
            "Ek bura sabd uske baren mein aur",
            "Ban hona tereko ?",
            "Kya batten chalri merri female bestie ke baren mein",
        ]

        await message.reply(
            f"{message.author.mention} {random.choice(action_responses)}"
        )

    await bot.process_commands(message)


@bot.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def close(ctx):
    await ctx.channel.send("Closing")
    await bot.close()

    await print("Bot closed")


@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name="Member")
    roles = bot.get_channel(980532187331985428)
    channel = bot.get_channel(980532170982563950)
    wlc_messages[
        f"{member.mention} has joined the community everyone greet them !",
        f"{member.mention} hope so you have brought pizza for us ",
    ]

    welcomeEmbed = discord.Embed(
        title=f"Welcome {member.name}",
        description=f" {member.mention} Welcome to The Eiffel Tower{roles.mention}",
        color=0x206694,
    )

    await bot.get_channel(980532170982563950).send(embed=welcomeEmbed)

    await bot.get_channel(980532164678529025).send(
        f"{member.mention} has joined the server say hi"
    )
    try:
        await member.send(
            f"Welcome to **The Eiffel Tower** {member.name}\nDon't forget to read the rules and take your roles from {roles.mention} have fun !"
        )
    except:
        await member.add_roles(role)
    pos = sum(
        m.joined_at < member.joined_at
        for m in member.guild.members
        if m.joined_at is not None
    )

    if pos == 1:
        te = "st"
    elif pos == 2:
        te = "nd"
    elif pos == 3:
        te = "rd"
    else:
        te = "th"

    background = Editor("wlc2.jpg")
    profile_image = await load_image_async(str(member.avatar_url))

    profile = Editor(profile_image).resize((350, 350)).circle_image()
    poppins = Font.poppins(size=100, variant="bold")

    poppins_small = Font.poppins(size=75, variant="light")

    background.paste(profile, (800, 150))
    background.ellipse((800, 150), 350, 350, outline="gold", stroke_width=4)

    background.text(
        (920, 60),
        f"WELCOME TO{member.guild.name}",
        color="white",
        font=poppins,
        align="center",
    )
    background.text(
        (920, 500),
        f"NAMASKAR {member.name}#{member.discriminator}",
        color="white",
        font=poppins_small,
        align="center",
    )
    background.text(
        (920, 600),
        f"You Are The {pos}{te} Member",
        color="#0BE7F5",
        font=poppins_small,
        align="center",
    )

    file = File(fp=background.image_bytes, filename="wlc2.jpg")
    welcomeEmbed = discord.Embed(
        title=f"Welcome {member.name}",
        description=f" {member.mention} Welcome to The Eiffel Tower{roles.mention}",
        color=0x206694,
    )
    await channel.send(embed=welcomeEmbed)

    await channel.send(file=file)


@bot.event
async def on_member_remove(member):
    await bot.get_channel(986573086386176020).send(
        f"{member.mention} has left the server"
    )


my_secret = os.environ["TOKEN"]
neverSleep.awake("https://Security.mr-triangletria.repl.co", False)
bot.run(my_secret)
