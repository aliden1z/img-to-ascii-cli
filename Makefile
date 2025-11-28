# CLI Image to ASCII Converter - Installation Script
# Installs dependencies into an isolated virtual environment in /opt

INSTALL_DIR = /opt/img-to-ascii-cli
BIN_DIR = /usr/local/bin
EXEC_NAME = img2ascii

.PHONY: install uninstall

install:
	@echo "🚀 Installing Image to ASCII CLI..."
	
	# 1. Create installation directory and copy source files
	@mkdir -p $(INSTALL_DIR)
	@cp main.py $(INSTALL_DIR)/
	@cp requirements.txt $(INSTALL_DIR)/
	
	# 2. Create an isolated Virtual Environment (Venv)
	@echo "📦 Creating virtual environment and installing dependencies..."
	@python3 -m venv $(INSTALL_DIR)/venv
	
	# 3. Install required libraries into the venv (Pillow etc.)
	@$(INSTALL_DIR)/venv/bin/pip install -q -r $(INSTALL_DIR)/requirements.txt
	
	# 4. Create the global executable wrapper script
	@echo "#!/bin/bash" > $(BIN_DIR)/$(EXEC_NAME)
	@echo "$(INSTALL_DIR)/venv/bin/python $(INSTALL_DIR)/main.py \"\$$@\"" >> $(BIN_DIR)/$(EXEC_NAME)
	
	# 5. Set executable permissions
	@chmod +x $(BIN_DIR)/$(EXEC_NAME)
	
	@echo "✅ Success! Type '$(EXEC_NAME)' to start converting."

uninstall:
	@echo "🗑️ Removing Image to ASCII CLI..."
	@rm -rf $(INSTALL_DIR)
	@rm -f $(BIN_DIR)/$(EXEC_NAME)
	@echo "✅ Uninstalled successfully."
