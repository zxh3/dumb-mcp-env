import contextlib

from fastapi import FastAPI
from .mcp_client import client


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/list_tools")
async def list_tools():
    async with client:
        return await client.list_tools()


@app.post("/call_tool")
async def call_tool(tool_name: str, tool_args: dict):
    async with client:
        return await client.call_tool(tool_name, tool_args)
