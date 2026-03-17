# ---- Config ----
BIN_DIR := ./bin
SRC_DIR := ./src
EXT_DIR := $(HOME)/.local/share/gh/extensions

EXTENSIONS := gh-coc gh-ignore gh-langs gh-license

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
	@for ext in $(EXTENSIONS); do \
		echo "Building $$ext..."; \
		go build -o $(BIN_DIR)/$$ext $(SRC_DIR)/$$ext/main.go; \
	done

# ---- Install (local dev via symlink) ----
.PHONY: install
install: build
	@for ext in $(EXTENSIONS); do \
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
