.PHONY: help build up down restart logs shell clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build the Docker image
	docker-compose build

up: ## Start the Jekyll server
	docker-compose up

down: ## Stop the Jekyll server
	docker-compose down

restart: ## Restart the Jekyll server
	docker-compose restart

logs: ## View Jekyll server logs
	docker-compose logs -f

shell: ## Open a shell in the Jekyll container
	docker-compose exec jekyll /bin/bash

clean: ## Clean up Docker resources
	docker-compose down -v
	rm -rf _site .jekyll-cache .sass-cache

rebuild: clean build up ## Clean, rebuild, and start
