import os
import logging
from anthropic import Anthropic

logger = logging.getLogger(__name__)


class ClaudeClient:
    """Wrapper around the Anthropic Claude client library."""

    def __init__(self, api_key: str | None = None):
        """Initialize the Claude client.

        Args:
            api_key: Anthropic API key. If not provided, will use ANTHROPIC_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

        self.client = Anthropic(api_key=self.api_key)
        logger.debug("Claude client initialized")

    def send_message(
        self,
        message: str,
        model: str = "claude-haiku-4-5",  # "claude-sonnet-4-20250514"
    ) -> str:
        """Send a message to Claude and get a response.

        Args:
            message: The message to send to Claude
            model: The Claude model to use

        Returns:
            The response text from Claude
        """
        logger.debug(f"Sending message to Claude (model: {model})")
        response = self.client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": message}],
        )
        return response.content[0].text
