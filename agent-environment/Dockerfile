FROM ghcr.io/astral-sh/uv:python3.12-alpine

COPY . /agent-environment

WORKDIR /agent-environment

RUN uv sync

EXPOSE 13788

CMD ["uv", "run", "python", "-m", "uvicorn", "agent_environment.main:app", "--host", "0.0.0.0", "--port", "13788"]