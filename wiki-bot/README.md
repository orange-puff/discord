# Discord Bot

A Python-based Discord bot that processes custom slash commands and returns results.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with your tokens:
```
DISCORD_TOKEN=your_bot_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

3. Get your Discord bot token:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application or select an existing one
   - Navigate to the "Bot" section
   - Click "Reset Token" and copy the token
   - Enable "Message Content Intent" under Privileged Gateway Intents

4. Get your Anthropic API key:
   - Go to [Anthropic Console](https://console.anthropic.com/)
   - Navigate to API Keys
   - Create a new API key and copy it

5. Invite the bot to your server:
   - In the Developer Portal, go to "OAuth2" > "URL Generator"
   - Select scopes: `bot`, `applications.commands`
   - Select bot permissions: `Send Messages`, `Read Messages/View Channels`
   - Copy the generated URL and open it in your browser

## Running the Bot

```bash
python bot.py
```

The bot will connect to Discord and be ready to process commands.
