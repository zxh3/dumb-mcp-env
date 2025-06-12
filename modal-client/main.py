import modal
from dotenv import load_dotenv

load_dotenv()


def main():
    image = modal.Image.from_registry("ryan1997/agent-environment:test-4")

    app = modal.App.lookup("xiaohua-test", create_if_missing=True)

    # uv run python -m uvicorn agent_environment.main:app --host 0.0.0.0 --port 13788
    sandbox = modal.Sandbox.create(
        image=image,
        timeout=50000,
        unencrypted_ports=[13788],
        app=app,
    )
    tunnel = sandbox.tunnels()[13788]
    print(tunnel.url)


if __name__ == "__main__":
    main()
