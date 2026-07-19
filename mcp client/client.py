import asyncio

from config import MODEL
from config import MCP_SERVER_URL
from config import OPENAI_API_KEY

from mcp_service import MCPService
from openai_service import OpenAIService


async def main():

    mcp = MCPService(MCP_SERVER_URL)

    await mcp.connect()

    print("Connected to Spring MCP Server")

    tool_response = await mcp.list_tools()

    openai_tools = []

    print("\nAvailable Tools")
    print("----------------")

    for tool in tool_response.tools:

        print(tool.name)

        openai_tools.append(
            {
                "type": "function",
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema
            }
        )

    ai = OpenAIService(
        OPENAI_API_KEY,
        MODEL
    )

    while True:

        question = input("\nQuestion : ").strip()

        if question.lower() == "quit":
            break

        response = ai.chat(
            question,
            openai_tools
        )

        message = response.output[0]

        if message.type == "function_call":

            print(f"\nCalling Tool : {message.name}")

            tool_result = await mcp.call_tool(
                message.name,
                message.arguments
            )

            final = ai.client.responses.create(
                model=MODEL,
                input=[
                    {
                        "role": "user",
                        "content": question
                    },
                    message,
                    {
                        "type": "function_call_output",
                        "call_id": message.call_id,
                        "output": str(tool_result.content)
                    }
                ]
            )

            print("\nAnswer\n")
            print(final.output_text)

        else:

            print("\nAnswer\n")
            print(response.output_text)

    await mcp.close()


if __name__ == "__main__":
    asyncio.run(main())