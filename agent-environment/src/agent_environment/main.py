import contextlib

from fastapi import FastAPI
from pydantic import BaseModel
from .mcp_client import client


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


@app.post("/list-tools")
async def list_tools():
    async with client:
        return await client.list_tools()


@app.post("/call-tool")
async def call_tool(request: CallToolRequest):
    async with client:
        return await client.call_tool(request.tool_name, request.tool_args)
