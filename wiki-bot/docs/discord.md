# Discord Bot Setup

This guide walks you through setting up your Discord bot from scratch.

## Prerequisites

- Python 3.x installed
- A Discord account
- An Anthropic API account

## Getting Your Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or select an existing one
3. Navigate to the "Bot" section
4. Click "Reset Token" and copy the token
5. Enable "Message Content Intent" under Privileged Gateway Intents

## Getting Your Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Navigate to API Keys
3. Create a new API key and copy it

## Configuration

Create a `.env` file in the project root with your tokens:
```
DISCORD_TOKEN=your_bot_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Inviting the Bot to Your Server

1. In the Developer Portal, go to "OAuth2" > "URL Generator"
2. Select scopes: `bot`, `applications.commands`
3. Select bot permissions: `Send Messages`, `Use Slash Commands (if available)`
4. Copy the generated URL and open it in your browser
5. Select the server you want to add the bot to and authorize
