import discord
import structlog
from discord.ext import commands
from structlog.stdlib import BoundLogger

from housemaid.meta import settings

base_log: BoundLogger = structlog.get_logger()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


def main() -> None:
    log = base_log.bind()
    print(f"{settings.app_name} {settings.version}")
    bot.run(token=settings.discord_token)
    log.info("Done ^^")


if __name__ == "__main__":
    main()
