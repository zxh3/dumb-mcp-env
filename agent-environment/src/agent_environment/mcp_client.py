from fastmcp import Client

config = {
    "mcpServers": {
        # Official MCP Servers from modelcontextprotocol repo
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "sequential-thinking": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
        },
        "memory": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-memory"],
        },
        # TODO: add filesystem server once we have a solution for artifacts ingestion
        # "filesystem": {
        #     "command": "npx",
        #     "args": [
        #         "-y",
        #         "@modelcontextprotocol/server-filesystem",
        #         "/Users/username/Desktop",
        #         "/path/to/other/allowed/dir",
        #     ],
        # },
        # Third party MCP Servers
        "calculator": {"command": "uvx", "args": ["mcp-server-calculator"]},
    }
}


client = Client(config)
