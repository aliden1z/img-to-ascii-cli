# 📟 CLI Image to ASCII Converter

A minimalist Python script that renders images into ASCII art directly in your terminal. No bloat, just characters. Geared towards Linux enthusiasts and CLI lovers.

## ⚡ Features

- **Lightweight:** Zero GUI, pure terminal output.
- **Flexible:** Supports JPG, PNG, WEBP and more.
- **Customizable:** Control the resolution (width) of the output via arguments.
- **Native:** Fits your terminal workflow perfectly.
- **Open Source:** Modify, hack, and share.

## 🛠 Requirements

- Python 3.x
- Pillow Library

## 📥 Installation

Clone the repo and enter the directory:

```bash
git clone https://github.com/KULLANICI_ADIN/img-to-ascii-cli.git
cd img-to-ascii-cli
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 💻 Usage

**1. Standard Mode (Default Width: 100)**
Pass the image path as an argument.
```bash
python main.py image.jpg
```

**2. Custom Resolution (Recommended)**
Pass the width as a second argument to fit your terminal size.
```bash
# Smaller output (for small terminals)
python main.py image.jpg 50

# High definition (maximize your terminal first!)
python main.py image.jpg 200
```

**3. Interactive Mode**
Run without arguments and follow the prompts.
```bash
python main.py
```

## 📸 Demo

![Project Screenshot](screenshot.png)

## 🐧 License

MIT License. Free as in freedom.
Happy Hacking!
