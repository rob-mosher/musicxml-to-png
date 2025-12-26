# musicxml-to-png

A tool for human-AI musical collaboration

<div align="center">
  <img src="https://raw.githubusercontent.com/rob-mosher/musicxml-to-png/v0.2.1/docs/images/screenshot.png" alt="Example visualization showing MusicXML converted to PNG" width="100%" style="max-width: 1200px;">
</div>

## Vision

MusicXML is rich and expressive for human-facing notation software, but challenging for AI systems to "see" structurally. This tool bridges that gap by converting MusicXML files into visual representations that both humans and AI can analyze together.

Why this matters:

- **AI doesn't natively "speak" MusicXML** (yet - that's the ultimate goal!)
- **Visual representations reveal structure** - harmonic motion, orchestration choices, form, texture
- **Shared visual language** enables human-AI collaboration on musical analysis and composition

This tool is designed for composers, arrangers, educators, and anyone exploring human-AI collaboration in music.

## Quick Start
```bash
# Install
pip install musicxml-to-png

# Use
musicxml-to-png your-score.mxl
```

See [Installation](#installation) for development setup.

## Purpose

Convert MusicXML files into clean, analyzable PNG visualizations showing:

- **Temporal flow** (horizontal axis = time)
- **Pitch range** (vertical axis = low to high)
- **Note duration** (length of visual bars)
- **Instrument** families (color-coded by ensemble type)

## Use Cases

**For human-AI collaboration:**

- Analyze orchestration patterns with AI assistance
- Compare multiple arrangements visually
- Identify voice leading and harmonic motion
- Explore how instrument families interact over time

**For AI systems & automation:**

- Convert MusicXML to visual format for AI analysis - AI systems can use this tool in their pipelines to process uploaded scores, even without native MusicXML support
- Enable AI agents to "see" musical structure and provide insights
- Automate batch analysis of large score collections
- Generate visual comparisons across multiple compositions

**For composers & arrangers:**

- Quick visual overview of complex scores
- Identify dense vs. sparse sections
- Check instrument balance and register distribution
- Export visualizations for presentations or teaching

**For educators:**

Teach orchestration principles visually
Compare different composers' approaches
Analyze form and structure at a glance

## Features

- Parse MusicXML files (.xml, .musicxml, .mxl)
- Extract note events (pitch, duration, start time, instrument)
- High-resolution 2D visualization (time × pitch) with fine-grained grid
- Multiple ensemble types:
  - Orchestra: strings, winds, brass, percussion
  - Bigband: trumpets, trombones, saxophones, rhythm section
  - (More ensemble types coming - jazz combo, chamber, etc.)
- Color-coded instrument families (distinct palettes per ensemble)
- Customizable visualization:
  - Grid lines (enabled by default, disable with --no-grid)
  - Minimal mode (remove all labels, legend, title, borders)
  - Custom titles
  - Verbose mode for debugging (-v/--verbose)
- Export as high-resolution PNG (300 DPI)

## Getting Your Music into MusicXML

Most modern notation software can export to MusicXML format. Here are some popular options:

**Desktop Software:**
- **[Dorico](https://www.steinberg.net/dorico/)** - File → Export → MusicXML (or use compressed .mxl format)
- **[Finale](https://www.finalemusic.com/)** - File → Export → MusicXML
- **[LilyPond](https://lilypond.org/)** - Can export via `lilypond --formats=xml`
- **[MuseScore](https://musescore.org/)** (Free, open source) - File → Export → MusicXML
- **[Notion](https://www.presonus.com/products/Notion)** - File → Export → MusicXML
- **[Overture](https://sonicscores.com/overture/)** - File → Export → MusicXML
- **[Sibelius](https://www.avid.com/sibelius)** - File → Export → MusicXML

**Web-Based:**
- **[Flat.io](https://flat.io/)** - File → Export → MusicXML
- **[Noteflight](https://www.noteflight.com/)** - File → Export → MusicXML

For detailed export instructions, please refer to your notation software's documentation. Most software supports both uncompressed `.mxl` and compressed `.xml` formats - this tool handles both!

## Python Setup

This project requires **Python 3.12**. The `.python-version` file will automatically set this if you use `pyenv`, `asdf`, or similar version managers.

Using pyenv:

```bash
pyenv install 3.12  # If not already installed
python --version    # Verify it shows Python 3.12.x
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd musicxml-to-png
   ```

2. Set up Python environment:
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Install package in development mode
   pip install -e .
   ```

**Note:** Activate the virtual environment (source venv/bin/activate) each time you work on the project. You'll see (venv) in your prompt when active.

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

## Roadmap

**Current:**

- ✅ Orchestra and bigband ensemble modes
- ✅ Minimal and grid visualization options
- ✅ High-resolution PNG export (300 DPI)

**Near-term:**

- Auto-detection of ensemble type
- Additional ensemble types (jazz combo, chamber, wind ensemble)
- Opacity for dynamics
- Articulation markers

**Long-term vision:**

- AI systems that natively "speak" MusicXML - the ultimate goal
- Animation showing temporal unfolding
- Integration with compositional AI tools
- Configurable color schemes and visual styles
- Integration with apps to display music visually

## Contributing

This project emerged from human-AI collaborative exploration of musical structure. Contributions, ideas, and feedback are welcome!

**Philosophy:** This tool exists to enable human-AI collaboration, not to replace human musical intuition. The goal is to create shared visual language that helps both humans and AI systems understand musical architecture more deeply.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Built through collaborative iteration between human musical expertise and AI technical assistance. Created to bridge the gap between MusicXML (machine-readable but visually dense) and visual analysis (human-friendly and AI-parseable).

Special thanks to: The music21 project for their excellent MusicXML parsing library.