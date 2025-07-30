from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

ZAPIER_BEARER_TOKEN = os.getenv('ZAPIER_BEARER_TOKEN')

if not ZAPIER_BEARER_TOKEN:
    raise ValueError("ZAPIER_BEARER_TOKEN environment variable is required. Please add it to your .env file.")

client = OpenAI()

# List available tools from the Zapier MCP server
response = client.responses.create(
    model="gpt-4",
    input="List all available tools",
    tool_choice="required",
    tools=[
        {
            "type": "mcp",
            "server_label": "zapier",
            "server_url": "https://mcp.zapier.com/api/mcp/mcp",
            "require_approval": "never",
            "headers": {
                "Authorization": f"Bearer {ZAPIER_BEARER_TOKEN}",
            },
        }
    ],
)

print("Available Zapier Tools:")
print(response)