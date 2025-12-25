# musicxml-to-png

## Purpose

Convert MusicXML files into clean, analyzable PNG visualizations showing:

- Temporal flow (horizontal axis = time)
- Pitch range (vertical axis = low to high)
- Note duration (length of visual bars)
- Instrument families (color-coded: strings, winds, brass, percussion)

## Tech Stack

- Python (for MusicXML parsing and image generation)
- music21 library (for MusicXML parsing)
- Pillow or matplotlib (for PNG generation)

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
