# import os
# from dotenv import load_dotenv

# load_dotenv()

# MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")
# ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
# MODEL = "claude-sonnet-4-5"

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")
MODEL = os.getenv("MODEL", "gpt-4.1")