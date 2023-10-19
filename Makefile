SHELL = /bin/bash
.SHELLFLAGS = -euo pipefail -c

REGISTRY := "$${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com"
REPOSITORY := $${REPO}
TAG := "$${BITBUCKET_COMMIT}"
LATEST_TAG := "latest"

APP_DIR := app
dev-clean:
	@{\
  		find $(APP_DIR) -type d -name "__pycache__" | xargs -i rm -rf {};\
  		find $(APP_DIR) -type d -name ".pytest_cache" | xargs -i rm -rf {};\
  		find $(APP_DIR) -type f -name ".coverage" | xargs -i rm -rf {};\
	}

dev-lint: dev-clean
	@{\
		blue --safe -l 120 $(APP_DIR) ;\
		flake8 $(APP_DIR) --extend-exclude=dist,build,.venv --show-source --statistics --max-line-length 120 ;\
	}

dev-run:
	@{\
  		cd $(APP_DIR);\
  		uvicorn main:app --host 127.0.0.1 --port 8000 --workers 1;\
	}

infra-stop:
	@{\
  		docker-compose -f docker-compose.yml stop ;\
	}

infra-start: infra-stop
	@{\
		docker-compose -f docker-compose.yml up --remove-orphans ;\
	}

docker-build:
	docker build -t $(REGISTRY)/$(REPOSITORY):$(TAG) .
	docker push $(REGISTRY)/$(REPOSITORY):$(TAG)
	docker tag $(REGISTRY)/$(REPOSITORY):$(TAG) $(REGISTRY)/$(REPOSITORY):latest
	docker push $(REGISTRY)/$(REPOSITORY):latest