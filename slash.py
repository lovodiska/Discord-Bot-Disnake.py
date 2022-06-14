import disnake
from disnake.ext import commands
class SlCommands(commands.Cog):

    """This will be for a ping command."""

    def init(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")
    @commands.slash_command(name="mod_kick",description="Кикает участника[Администрация]") #Register a command, give it a name and description
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

        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg%22)
        embed.set_image(url="https://i.ytimg.com/vi/Y3zZUfP277k/maxresdefault.jpg%22)

        embed.add_field(name="Участник был кикнут по причине:", value=reason, inline=False)
        await inter.response.send_message(embed=embed)
        await member.kick(reason=reason)

    @commands.slash_command(name="mod_ban",description="Банит участника[Администрация]") #Register a command, give it a name and description
    async def mod_ban(inter,member: disnake.Member,reason): #creating def|command
        embed = disnake.Embed(  #creating embed
        title=f"Участник {member} был исключен!",
        description=f"{inter.author.mention} забанил пользователя. Причина указана ниже.",
        color=disnake.Colour.red(),
        )

        embed.set_author(
            name="РаБотяра",
            icon_url="https://i.pinimg.com/originals/6a/66/71/6a66713b29d5a6149ed34a8075287e6f.jpg",
        )
        embed.set_footer(
            text="Was Created//By Mayka/lovodiska",
            icon_url="https://i.pinimg.com/originals/70/fc/8b/70fc8b416e4d0202007b3cc7a035d92a.jpg",
        )

        embed.set_thumbnail(url="https://i.ytimg.com/vi/NHPjJ7JqTYY/maxresdefault.jpg%22)
        embed.set_image(url="https://i.ytimg.com/vi/Y3zZUfP277k/maxresdefault.jpg%22)

        embed.add_field(name="Участник был забанен по причине:", value=reason, inline=False)
        await inter.response.send_message(embed=embed)
        await member.ban(reason=reason)


def setup(bot: commands.Bot):
    bot.add_cog(SlCommands(bot))
    print("Cog SlCom Has Been Loaded")
