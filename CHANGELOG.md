# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.3] - 2025-12-26

### Changed
- Default ensemble now `ungrouped`, giving every part its own color; CLI help and docs updated accordingly
- Legend construction refactored with helper/config map for ensemble family legends and ungrouped fallback for future ensembles

## [0.2.2] - 2025-12-26

### Changed

- Simplified README by removing redundancy and condensing verbose sections:
  - Merged Vision section into brief intro paragraph
  - Reduced Quick Start examples from 5 to 2
  - Merged Purpose into Features section header
  - Condensed Use Cases from 4 subsections to single sentence
  - Consolidated Usage section to emphasize command form (removed python -m examples)
  - Removed Tech Stack section
  - Moved Roadmap to docs/roadmap.md
  - Reduced README from ~283 to ~205 lines while maintaining all essential information
- Enhanced Quick Start section with practical usage examples showing ensemble selection and option combinations
- Correct minor formatting issues in README

## [0.2.1] - 2025-12-26

### Changed

- Updated README image URL to use version-specific GitHub tag for PyPI compatibility

## [0.2.0] - 2025-12-25

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

[0.2.3]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.3
[0.2.2]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.2
[0.2.1]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.1
[0.2.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.0
[0.1.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.1.0
