<div align="center">

# 📟 Img2ASCII CLI

**Turn Pixels into Characters directly in your Terminal**

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Style](https://img.shields.io/badge/Style-Retro-ff00ff?style=for-the-badge)](https://github.com/aliden1z)
[![Author](https://img.shields.io/badge/Author-aliden1z-orange?style=for-the-badge)](https://github.com/aliden1z)

<br>

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Gallery](#-demo)

</div>

---

## 📖 About

**Img2ASCII** is a minimalist Python script that renders images into ASCII art. It brings a retro, hacker-style aesthetic to your modern terminal workflow.

Designed with Linux philosophy in mind: **No GUI, no bloat, just characters.** It supports a wide range of image formats and respects your system's package integrity by using isolated environments.

## ⚡ Features

- **🎨 Multi-Format Support:** Handles `.jpg`, `.png`, `.webp`, `.bmp` and more.
- **📏 Fully Resizable:** Adjust the output width to fit split-screens or 4K monitors.
- **🛡️ System Safe:** Installs dependencies in `/opt`, keeping your global Python environment clean (PEP 668 compliant).
- **🚀 Native Feel:** Works as a global command (`img2ascii`) anywhere in your shell.
- **⚡ Zero Bloat:** Pure Python, pure terminal output.

## 📥 Installation

This project uses a `Makefile` to automate the creation of an isolated virtual environment and a global wrapper script.

### Option 1: Global Install (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/aliden1z/img-to-ascii-cli.git
cd img-to-ascii-cli

# 2. Install using Make (Requires sudo)
sudo make install
```

> **Note:** This method is safe for Arch Linux and other modern distros. It installs dependencies into `/opt/img-to-ascii-cli`, preventing conflicts with system packages.

**To uninstall:**
```bash
sudo make uninstall
```

### Option 2: Local Run

If you want to try it out without installing it system-wide:

```bash
pip install -r requirements.txt
python img2ascii.py
```

## 💻 Usage

Once installed, you can use the `img2ascii` command from any directory.

### 1. Standard Conversion
Pass the image path. The default width is set to **100 characters**.

```bash
img2ascii path/to/image.jpg
```

### 2. Custom Resolution
Pass a second argument to define the width. This is useful for high-res terminals or small split panes.

```bash
# Compact output
img2ascii image.png 50

# High definition (Maximize your terminal font first!)
img2ascii image.png 200
```

### 3. Interactive Mode
Run without arguments to enter the interactive prompt.

```bash
img2ascii
```

## 📸 Demo

<div align="center">
  <img src="screenshot.png" alt="ASCII Art Demo" width="700">
  <br>
  <i>(Example output running in a terminal)</i>
</div>

## 🐧 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <small>Made with ❤️  by <a href="https://github.com/aliden1z">aliden1z</a></small>
</div>
