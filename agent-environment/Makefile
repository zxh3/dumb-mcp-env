IMAGE_NAME = ryan1997/agent-environment:test-25

.PHONY: dev build push build-and-push

run:
	uv run python -m uvicorn agent_environment.main:app --host 0.0.0.0 --port 1984

build:
	docker build -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

shell:
	docker run -it -p 1984:1984 --rm $(IMAGE_NAME) sh

build-and-push: build push