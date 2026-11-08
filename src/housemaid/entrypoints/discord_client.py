import discord
import structlog
from structlog.stdlib import BoundLogger

from housemaid.meta import settings

base_log: BoundLogger = structlog.get_logger()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


def main() -> None:
    log = base_log.bind()
    print(f"{settings.app_name} {settings.version}")
    client.run(token=settings.discord_token)
    log.info("Done ^^")
