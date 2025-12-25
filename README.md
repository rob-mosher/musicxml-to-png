# musicxml-to-png

## Purpose

Convert MusicXML files into clean, analyzable PNG visualizations showing:

- Temporal flow (horizontal axis = time)
- Pitch range (vertical axis = low to high)
- Note duration (length of visual bars)
- Instrument families (color-coded by ensemble type)

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

This creates `input.png` in the same directory. Supports both `.xml` and `.mxl` (compressed) MusicXML files.

**Basic Options:**

```bash
# Specify custom output file
python -m musicxml_to_png input.xml -o output.png

# Add custom title
python -m musicxml_to_png input.xml --title "My Composition"

# Disable grid lines
python -m musicxml_to_png input.xml --no-grid

# Minimal mode (no labels, legend, title, or borders)
python -m musicxml_to_png input.xml --minimal

# Show music21 warnings and diagnostics
python -m musicxml_to_png input.xml --verbose
# or
python -m musicxml_to_png input.xml -v
```

**Ensemble Types:**

Select the instrument categorization scheme:

```bash
# Orchestra (default) - strings, winds, brass, percussion
python -m musicxml_to_png input.xml

# Bigband - trumpets, trombones, saxophones, rhythm section
python -m musicxml_to_png input.xml --ensemble bigband
```

**Combining Options:**

```bash
python -m musicxml_to_png input.xml --ensemble bigband --minimal --no-grid -o output.png
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

# Basic conversion
output_path = convert_musicxml_to_png(
    input_path=Path("input.xml"),
    output_path=Path("output.png"),  # Optional
    title="My Composition"  # Optional
)

# With all options
output_path = convert_musicxml_to_png(
    input_path=Path("input.xml"),
    output_path=Path("output.png"),
    title="My Composition",
    show_grid=False,           # Disable grid lines
    minimal=True,              # Remove all labels/borders
    ensemble="bigband"         # Use bigband categorization
)
```

## Tech Stack

- Python (for MusicXML parsing and image generation)
- music21 library (for MusicXML parsing)
- matplotlib (for PNG generation)

## Features

- Parse MusicXML files (`.xml`, `.musicxml`, `.mxl`)
- Extract note events (pitch, duration, start time, instrument)
- High-resolution 2D visualization (time × pitch) with fine-grained grid
- Multiple ensemble types:
  - **Orchestra**: strings, winds, brass, percussion
  - **Bigband**: trumpets, trombones, saxophones, rhythm section
- Color-coded instrument families (distinct palettes per ensemble)
- Customizable visualization:
  - Grid lines (enabled by default, disable with `--no-grid`)
  - Minimal mode (remove all labels, legend, title, borders)
  - Custom titles
  - Verbose mode for debugging (`-v`/`--verbose`)
- Export as high-resolution PNG (300 DPI)

## Future Features

- Auto-detection of ensemble type
- Opacity for dynamics
- Articulation markers
- Configurable color schemes
- Additional ensemble types (jazz combo, chamber, etc.)
