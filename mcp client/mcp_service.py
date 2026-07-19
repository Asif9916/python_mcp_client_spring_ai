from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


class MCPService:

    def __init__(self, url):
        self.url = url
        self.session = None
        self.exit_stack = AsyncExitStack()

    async def connect(self):

        read_stream, write_stream, _ = await self.exit_stack.enter_async_context(
            streamablehttp_client(self.url)
        )

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )

        await self.session.initialize()

    async def list_tools(self):
        return await self.session.list_tools()

    async def call_tool(self, name, arguments):
        return await self.session.call_tool(name, arguments)

    async def close(self):
        await self.exit_stack.aclose()