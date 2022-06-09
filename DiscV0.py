#import libraries:
import disnake 
from disnake.ext import commands
import datetime
import asyncio
from asyncio import sleep
bot = commands.InteractionBot(test_guilds=[927860255541583872]) #creating variable bot with our server's guild
TOKEN = "your token" #past your token here
@bot.event #creating event on_ready(when the bot started)
async def on_ready():
    print('We have logged as Работяра')
    print("Download...")
    await asyncio.sleep(1)
    print("Download..")
    await asyncio.sleep(1)
    print("Download.")
    await asyncio.sleep(1)
    print("Download...")
    print("Download Complete!")


class slash_commands(): #I created this class for my convenience
    @bot.slash_command(name="mod_kick",description="Кикает участника[Администрация]") #Register a command, give it a name and description
    @commands.has_any_role(958689474257231912,954238941312213082,927860283534368848,928662710168715284,927860746602303498,927860746602303498) #giving limited for use the command
    async def mod_kick(inter,member: disnake.Member,reason): #creating def|command
        embed = disnake.Embed(  #creating embed
        title=f"Участник {member} был исключен!",
        description=f"{inter.author.mention} исключил пользователя. Причина указана ниже.",
        color=disnake.Colour.red(),
        )

        embed.set_author(
            name="РаБотяра",
            icon_url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
            text="Was Created//By Mayka",
            icon_url="https://i.pinimg.com/originals/70/fc/8b/70fc8b416e4d0202007b3cc7a035d92a.jpg",
        )

        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg")
        embed.set_image(url="https://i.ytimg.com/vi/Y3zZUfP277k/maxresdefault.jpg")

        embed.add_field(name="Участник был кикнут по причине:", value=reason, inline=False)
        await inter.response.send_message(embed=embed)
        await member.kick(reason=reason)

    @bot.slash_command(name="mod_ban",description="Блокирует человека[Администрация]")
    @commands.has_any_role(958689474257231912,954238941312213082,927860283534368848,928662710168715284,927860746602303498,927860746602303498)
    async def mod_ban(inter,member: disnake.Member,reason):
        embed = disnake.Embed(
        title=f"Участник {member} был заблокирован!",
        description=f"{inter.author.mention} заблокировал пользователя. Причина указана ниже.",
        color=disnake.Colour.red(),
        )

        embed.set_author(
        name="РаБотяра",
        url="https://disnake.dev/",
        icon_url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
        text="Was Created//By Mayka",
        icon_url="https://i.pinimg.com/originals/70/fc/8b/70fc8b416e4d0202007b3cc7a035d92a.jpg",
        )

        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg")
        embed.set_image(url="http://risovach.ru/upload/2016/05/mem/odinochestvo_113025575_orig_.png")

        embed.add_field(name="Участник был заблокирован по причине:", value=reason, inline=False)
        await inter.response.send_message(embed=embed)
        await member.ban(reason=reason)


    @bot.slash_command(name="warehouse_take",description="добавляет embed с отчетом о взятии чего либо со склада.[Участник]")
    async def warehouse_take(inter,items):
        embed = disnake.Embed(
        title="Отчет о взятии со склада",
        color=disnake.Colour.green(),
        timestamp=datetime.datetime.now(),
        )

        embed.set_author(
        name="Leeroy Family Bot",
        url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
        text="Created by Mayki|Err0rth",
        )

        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg")

        embed.add_field(name=f"Сотрудник:", value=f"{inter.author.mention}", inline=True)
        embed.add_field(name="Дискорд сотрудника:", value=f"{inter.author}", inline=True)
        embed.add_field(name="Действие:", value=f"*Взял*: {items}", inline=False)
        await inter.response.send_message(embed=embed)

    @bot.slash_command(name="warehouse_give",description="добавляет embed с отчетом о сдаче чего либо на склад.[Участник]")
    async def warehouse_give(inter,items):
        embed = disnake.Embed(
        title="Отчет о взятии со склада",
        color=disnake.Colour.green(),
        timestamp=datetime.datetime.now(),
        )

        embed.set_author(
        name="Leeroy Family Bot",
        url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
        text="Created by Mayki|Err0rth",
        )
        
        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg")

        embed.add_field(name=f"Сотрудник:", value=f"{inter.author.mention}", inline=True)
        embed.add_field(name="Дискорд сотрудника:", value=f"{inter.author}", inline=True)
        embed.add_field(name="Действие:", value=f"*Сдал*: {items}", inline=False)
        await inter.response.send_message(embed=embed)


    @bot.slash_command(name="rules", descriprion="Команда для Майки[OwnDevelop]")
    async def aules(inter):
        embed = disnake.Embed(
        title="Изменения в правилах:",
        color=disnake.Colour.red(),
        )

        embed.set_author(
        name="Mitsuo Family Bot",
        url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
        text="Created by Mayki|Err0rth",
        )
        embed.add_field(name=f"UPD:", value="Изменения правил \n Build 1.1", inline=True)
        embed=embed
        await inter.response.send_message(embed=embed)
    @bot.slash_command(name="audit_invite", description="Команда для заполнения кадрового аудита[Recrutier\\Принятие]")
    async def auditinv(inter,member,passport,name):
        embed = disnake.Embed(
        title="Отчет о Принятии сотрудника",
        color=disnake.Colour.purple(),
        timestamp=datetime.datetime.now(),
        )

        embed.set_author(
        name="Leeroy Family Bot",
        url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
        text="Created by Mayki|Err0rth",
        )
        
        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg")
        embed.add_field(name=f"Сотрудник:", value=f"{member}", inline=False)
        embed.add_field(name="Имя сотрудника", value=f"{name}", inline=False)
        embed.add_field(name="Действие:", value=f"*Принятие*", inline=False)
        embed.add_field(name="Номер Паспорта", value=f"{passport}")
        embed.add_field(name="Автор",value=f"{inter.author.mention}")
        await inter.response.send_message(embed=embed)
    @bot.slash_command(name="audit_kick",description="Команда для заполнения кадрового аудита[Recrutier\\Увал]")
    async def audit_kick(inter,member,passport,name,reason):
        embed = disnake.Embed(
        title="Отчет о Увольнении сотрудника",
        color=disnake.Colour.purple(),
        timestamp=datetime.datetime.now(),
        )

        embed.set_author(
        name="Leeroy Family Bot",
        url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
        text="Created by Mayki|Err0rth",
        )
        
        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg")
        embed.add_field(name=f"Сотрудник:", value=f"{member}", inline=False)
        embed.add_field(name="Имя сотрудника", value=f"{name}", inline=False)
        embed.add_field(name="Действие:", value=f"*Увал*", inline=False)
        embed.add_field(name="Номер Паспорта", value=f"{passport}")
        embed.add_field(name="Автор",value=f"{inter.author.mention}")
        embed.add_field(name="Причина", value=f"{reason}", inline=False)
        await inter.response.send_message(embed=embed)
class prefix_commands(): #I'll update it
    pass
bot.run(TOKEN) #bot run