from fastmcp import Client

config = {
    "mcpServers": {
        "exa-search": {
            "url": "https://server.smithery.ai/exa/mcp?api_key=e258c085-8b7e-451f-a826-53e17a3a1766",
            "transport": "streamable-http",
        },
    }
}

client = Client(config)
