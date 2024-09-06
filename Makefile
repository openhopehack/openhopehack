SHELL := /bin/bash
VENV_DIR := .venv
PYTHON := python3

.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Virtual environment setup
.PHONY: setup-venv
setup-venv: ## Create the virtual environment and install dependencies.
	$(PYTHON) -m venv $(VENV_DIR)
	source $(VENV_DIR)/bin/activate && pip install -r requirements.txt

.PHONY: install
install: setup-venv ## Install the dependencies in the virtual environment.

.PHONY: activate
activate: ## Activate the virtual environment.
	@echo "To activate the virtual environment, run:"
	@echo "source $(VENV_DIR)/bin/activate"

.PHONY: run
run: ## Run the Flask application.
	source $(VENV_DIR)/bin/activate && $(VENV_DIR)/bin/python run.py

.PHONY: clean
clean: ## Remove the virtual environment directory.
	rm -rf $(VENV_DIR)

##@ Utility targets
.PHONY: all
all: setup-venv run ## Set up the environment and run the application.
