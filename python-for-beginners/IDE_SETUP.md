# Setup Guide: Python + VS Code

Everything you need before writing your first line of code.

---

## Prerequisites

Before installing anything, check these boxes:

- [ ] You have a laptop or desktop running Windows 10/11, macOS 12+, or Linux
- [ ] You have at least 2 GB of free disk space
- [ ] You have a stable internet connection for the initial downloads
- [ ] You have admin/install permissions on your machine (can install software)

That's it. No prior programming knowledge needed.

---

## Step 1 — Install Python

1. Go to https://www.python.org/downloads/
2. Click the big **Download Python 3.12.x** button — it auto-detects your operating system
3. Run the installer
4. **Windows only:** On the first screen, tick **"Add Python to PATH"** before clicking Install — don't skip this
5. Click **Install Now** and wait for it to finish

### Verify the install

Open a terminal (Terminal on Mac, Command Prompt on Windows) and run:

```bash
python --version
```

You should see `Python 3.12.x`. If that works, you're done.

---

## Step 2 — Install VS Code

1. Go to https://code.visualstudio.com
2. Download the installer for your operating system
3. Run the installer with default settings
4. Open VS Code

---

## Step 3 — Install the Python Extension

1. Open VS Code
2. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS) to open Extensions
3. Search for **Python**
4. Install the one published by **Microsoft** (it has millions of downloads)
5. VS Code will also suggest installing **Pylance** — install that too

---

## Step 4 — Open the Course Folder

1. In VS Code, go to **File → Open Folder**
2. Navigate to and select the `python-for-beginners` folder
3. VS Code will ask you to select a Python interpreter — choose **Python 3.12**

If it doesn't ask automatically:
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
- Type **Python: Select Interpreter**
- Choose Python 3.12 from the list

---

## Step 5 — Read Markdown Files Comfortably

All the course content (READMEs, CONCEPTS, CHEATSHEET) is written in Markdown (`.md` files). By default VS Code shows you the raw text with `#` symbols and `**asterisks**`. Switch to the rendered preview to read it like a proper document.

**How to open the preview:**
- Open any `.md` file (e.g. `README.md`)
- Press `Ctrl+Shift+V` (Windows/Linux) or `Cmd+Shift+V` (macOS)
- A nicely formatted preview opens in a new tab

**Side-by-side view (recommended for studying):**
- Open the `.md` file
- Press `Ctrl+K V` (Windows/Linux) or `Cmd+K V` (macOS)
- The raw file stays on the left, the rendered preview on the right

Use the preview when reading CONCEPTS.md and READMEs. Switch to the raw file only if you need to edit.

---

## Step 6 — Smoke Test

Open the VS Code terminal (`Ctrl+\`` or **Terminal → New Terminal**) and run:

```bash
python modules/module01_getting_started/examples/01_hello_world.py
```

You should see output printed to the terminal. If it works, you're ready to start Module 1.

---

## Recommended VS Code Settings

Press `Ctrl+Shift+P` → type **Open User Settings (JSON)** → paste this inside the `{}`:

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.rulers": [79],
  "editor.wordWrap": "off",
  "python.defaultInterpreterPath": "python3"
}
```

---

## Useful VS Code Shortcuts

| Action | Windows / Linux | macOS |
|--------|----------------|-------|
| Run current file | `F5` | `F5` |
| Open terminal | `` Ctrl+` `` | `` Cmd+` `` |
| Open file | `Ctrl+P` | `Cmd+P` |
| Command palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Comment a line | `Ctrl+/` | `Cmd+/` |
| Indent selection | `Tab` | `Tab` |
| Undo | `Ctrl+Z` | `Cmd+Z` |

---

## Common Setup Problems

**`python` not found after install (Windows)**
- Re-run the Python installer → check "Add Python to PATH" → restart your terminal

**`python` shows version 2.x (macOS)**
- Use `python3` instead, or set up an alias: `alias python=python3` in your `~/.zshrc`

**VS Code doesn't find my Python install**
- Press `Ctrl+Shift+P` → Python: Select Interpreter → click "Enter interpreter path" → paste the path from `which python3`

**Extension not activating**
- Open any `.py` file first — VS Code only activates the Python extension when a Python file is open
