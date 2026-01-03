import os
import logging
from claude_client import ClaudeClient


logger = logging.getLogger(__name__)


class WikiAgent:

    def __init__(self):
        self.claude_client = ClaudeClient()

    def send_message(self, query: str) -> str:
        # Create the prompt for Claude
        prompt = f"This is a question about the game Old School RuneScape. Please answer the question concisely and respond with 1 OSRS wiki link to answer the question. Here is the question: {query}"

        logger.info(f"Processing query: {query}")
        return self.claude_client.send_message(prompt)
