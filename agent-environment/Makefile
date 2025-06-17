IMAGE_NAME = ryan1997/agent-environment:test-21

.PHONY: dev build push build-and-push



run:
	uv run python -m uvicorn agent_environment.main:app --host 0.0.0.0 --port 1984

build:
	docker build -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

build-and-push: build push