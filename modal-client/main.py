import modal
from dotenv import load_dotenv

load_dotenv()

PORT = 1984


def main():
    image = modal.Image.from_registry("ryan1997/agent-environment:test-25").entrypoint(
        [
            "sh",
            "-c",
            "cd /agent-environment && uv run python -m uvicorn agent_environment.main:app --host 0.0.0.0 --port 1984",
        ]
    )

    app = modal.App.lookup(
        "xiaohua-test",
        create_if_missing=True,
    )

    sandbox = modal.Sandbox.create(
        image=image,
        timeout=3600 * 3,
        unencrypted_ports=[PORT],
        app=app,
    )
    tunnel = sandbox.tunnels()[PORT]
    print(tunnel.url)


if __name__ == "__main__":
    main()
