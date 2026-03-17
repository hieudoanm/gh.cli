# ---- Config ----
BIN_DIR := ./bin
SRC_DIR := ./src
EXT_DIR := $(HOME)/.local/share/gh/extensions

COMMANDS := coc ignore langs license og
EXTENSIONS := gh-coc gh-ignore gh-langs gh-license gh-og

# ---- Tools ----
FMT := go fmt ./...
VET := go vet ./...

# ---- Default ----
.PHONY: all
all: build

# ---- Quality ----
.PHONY: format vet lint
format:
	$(FMT)

vet:
	$(VET)

lint: format vet

# ---- Build ----
.PHONY: build
build: lint
	@mkdir -p $(BIN_DIR)
	@for command in $(COMMANDS); do \
		echo "Building $$command..."; \
		go build -o $(BIN_DIR)/gh-$$command $(SRC_DIR)/commands/$$command/main.go; \
	done

# ---- Install (local dev via symlink) ----
.PHONY: install
install: build
	@for command in $(COMMANDS); do \
		ext=gh-$$command; \
		echo "Installing $$ext..."; \
		EXT_PATH=$(EXT_DIR)/$$ext; \
		rm -rf $$EXT_PATH; \
		mkdir -p $$EXT_PATH; \
		ln -sf $(PWD)/$(BIN_DIR)/$$ext $$EXT_PATH/$$ext; \
	done

# ---- Uninstall ----
.PHONY: uninstall
uninstall:
	@for ext in $(EXTENSIONS); do \
		echo "Removing $$ext..."; \
		rm -rf $(EXT_DIR)/$$ext; \
	done

# ---- Clean ----
.PHONY: clean
clean:
	rm -rf $(BIN_DIR)
