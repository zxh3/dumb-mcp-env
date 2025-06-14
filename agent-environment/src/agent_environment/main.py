import contextlib

from fastapi import FastAPI
from .mcp_client import client
from pydantic import BaseModel


class CallToolRequest(BaseModel):
    tool_name: str
    tool_args: dict


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
async def call_tool(request: CallToolRequest):
    async with client:
        return await client.call_tool(request.tool_name, request.tool_args)
