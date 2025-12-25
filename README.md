# musicxml-to-png

## Purpose

Convert MusicXML files into clean, analyzable PNG visualizations showing:

- Temporal flow (horizontal axis = time)
- Pitch range (vertical axis = low to high)
- Note duration (length of visual bars)
- Instrument families (color-coded: strings, winds, brass, percussion)

## Requirements

- Python 3.12 (specified in `.python-version` - works with pyenv, asdf, direnv, etc.)

## Python Version Management

This project uses Python 3.12, specified in the `.python-version` file. If you're using **pyenv**:

1. Install Python 3.12 (if not already installed):
   ```bash
   pyenv install 3.12
   ```

2. The `.python-version` file will automatically tell pyenv to use Python 3.12 when you're in this directory. Verify it's working:
   ```bash
   python --version  # Should show Python 3.12.x
   ```

3. If automatic detection doesn't work, manually set it:
   ```bash
   pyenv local 3.12
   ```

**Other version managers:** The `.python-version` file also works with `asdf`, `direnv`, and other tools that support this standard.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd musicxml-to-png
   ```

2. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

**Note:** Remember to activate the virtual environment (`source venv/bin/activate`) each time you work on the project. You'll see `(venv)` in your terminal prompt when it's active.

## Usage

### Command Line Interface

Convert a MusicXML file to PNG:

```bash
python -m musicxml_to_png input.xml
```

This creates `input.png` in the same directory.

Specify a custom output file:

```bash
python -m musicxml_to_png input.xml -o output.png
```

Add a custom title to the visualization:

```bash
python -m musicxml_to_png input.xml --title "My Composition"
```

After installation, you can also use the `musicxml-to-png` command directly:

```bash
musicxml-to-png input.xml -o output.png
```

### Python Library

Use as a library in your Python code:

```python
from musicxml_to_png import convert_musicxml_to_png
from pathlib import Path

# Convert MusicXML to PNG
output_path = convert_musicxml_to_png(
    input_path=Path("input.xml"),
    output_path=Path("output.png"),  # Optional
    title="My Composition"  # Optional
)
```

## Tech Stack

- Python (for MusicXML parsing and image generation)
- music21 library (for MusicXML parsing)
- matplotlib (for PNG generation)

## Initial Features (v1)

- Parse MusicXML file
- Extract note events (pitch, duration, start time, instrument)
- Map to 2D visualization (time × pitch)
- Color-code by instrument family
- Export as clean PNG

## Future Features

- Opacity for dynamics
- Articulation markers
- Configurable color schemes
