from fastmcp import Client

config = {
    "mcpServers": {
        "calculator": {
            "url": "https://server.smithery.ai/@githejie/mcp-server-calculator/mcp?api_key=e258c085-8b7e-451f-a826-53e17a3a1766",
            "transport": "streamable-http",
        },
        "youtube": {
            "command": "npx",
            "args": ["-y", "youtube-data-mcp-server"],
            "env": {
                "YOUTUBE_API_KEY": "AIzaSyADfmMxCQReHkYL-CTmv64j3z936w206Ks",
                "YOUTUBE_TRANSCRIPT_LANG": "en",
            },
        },
    }
}


client = Client(config)
