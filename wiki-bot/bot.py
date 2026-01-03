import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv
from wiki_agent import WikiAgent


COMMAND_NAME = "osrs"
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

intents: discord.Intents = discord.Intents.default()
intents.message_content = True

bot: commands.Bot = commands.Bot(command_prefix="!", intents=intents)
wiki_agent = WikiAgent()


@bot.event
async def on_ready() -> None:
    logger.info(f"{bot.user} has connected to Discord!")
    logger.info(f"Bot is in {len(bot.guilds)} guild(s)")

    # Sync slash commands with Discord
    try:
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")


@bot.tree.command(name=COMMAND_NAME, description="OSRS Wiki command")
async def osrs(interaction: discord.Interaction, query: str):
    """Search or get information from the OSRS Wiki"""
    # Defer the response since Claude API call might take a moment
    await interaction.response.defer()

    try:
        # Get response from Claude
        response = wiki_agent.send_message(query)
        logger.debug(f"Received response from Claude")

        # Send the response back to Discord
        await interaction.followup.send(response)
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        await interaction.followup.send(f"Sorry, I encountered an error: {str(e)}")


if __name__ == "__main__":
    TOKEN: str | None = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN not found in environment variables")
    bot.run(TOKEN)
