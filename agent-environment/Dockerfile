FROM ghcr.io/astral-sh/uv:python3.12-alpine

RUN apk add --no-cache nodejs npm

COPY . /agent-environment

WORKDIR /agent-environment

RUN uv sync

EXPOSE 1984

CMD ["uv", "run", "python", "-m", "uvicorn", "agent_environment.main:app", "--host", "0.0.0.0", "--port", "1984"]