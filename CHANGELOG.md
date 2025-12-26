# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Comprehensive test suite using pytest:
  - Unit tests for instrument classification (orchestra and bigband ensembles)
  - Unit tests for note extraction and visualization generation
  - CLI interface tests
  - Integration tests with real MusicXML files
  - Test fixtures and configuration

### Changed

- Added hero screenshot to README showcasing example visualization output
- Improved instrument name matching to prioritize longer, more specific keywords (e.g., "bassoon" before "bass")

## [0.1.0] - 2025-12-25

### Added

- Core MusicXML to PNG conversion functionality
- Support for `.xml`, `.musicxml`, and `.mxl` (compressed) file formats
- High-resolution PNG export (300 DPI) with fine-grained grid visualization
- Instrument family classification and color-coding
- Ensemble type support:
  - Orchestra: strings, winds, brass, percussion
  - Bigband: trumpets, trombones, saxophones, rhythm section
- Distinct color palettes for each ensemble type
- CLI interface with comprehensive options:
  - Custom output file paths (`-o`, `--output`)
  - Grid control (`--no-grid`)
  - Minimal visualization mode (`--minimal`)
  - Verbose mode for debugging (`-v`, `--verbose`)
  - Ensemble selection (`--ensemble`)
  - Custom titles (`-t`, `--title`)
- Python library interface for programmatic use
- Comprehensive documentation including:
  - Installation and setup instructions
  - Usage examples for CLI and library
  - Notation software export guide
  - Python version management guide

### Technical

- Python 3.12 support with `.python-version` specification
- Modern Python packaging with `pyproject.toml`
- `src/` layout following Python packaging best practices
- Virtual environment setup and dependency management
- MIT License

[0.1.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.1.0

