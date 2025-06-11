import modal
from dotenv import load_dotenv

load_dotenv()

# modal token set --token-id ak-ip216EiPfTIvIn5EuIH4Ug --token-secret as-jt6q7SR22sQdAORmQc2sxw 

def main():
    image = modal.Image.from_registry('ryan1997/agent-environment:test-4', force_build=True)
    
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