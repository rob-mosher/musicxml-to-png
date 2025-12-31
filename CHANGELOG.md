# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## Fixed

- Connection detection now respects distinct voices within a shared part and inferred voice lanes; connections no longer misroute when multiple voices share one staff.

## [0.6.1] - 2025-12-30

## Changed

- Updated connection defaults: linewidth now 2.5 and curve height factor 2.0 (connections curve upward by default).
- Connection alpha now derives from adjacent note dynamics (adaptive); removed CLI alpha/min-alpha flags to avoid manual opacity tuning, dynamic-driven alpha is covered by new helper tests.

## Fixed

- Transposing instruments are now rendered at concert pitch.

## [0.6.0] - 2025-12-30

### Added

- CLI flag `--transparent` (and library argument `transparent`) to generate PNG output with transparent backgrounds instead of white, enabling overlays on any background color.
- CLI flag `--show-connections` (beta) to visualize connections between adjacent notes using straight lines. Connections are per-instrument and only connect notes on different pitches. Note: This feature is in beta and may have edge cases.

### Changed

- Streamlined README with consistent Basic/Common/Advanced structure across Features, CLI, and Python Library sections for improved clarity and navigation.
- Removed redundant Installation and MusicXML export sections, trusting users to infer setup from standard project files and their notation software documentation.
- Refactored `visualize.py` into composable helpers with explicit sizing/tick/legend steps and introduced `VisualizationConfig`/`VisualizationContext` to make visualization orchestration clearer and reduce "magic" kwargs.
- Converter now builds `VisualizationConfig`, `VisualizationInputs`, and `TimeTickSpec` up front so visualization calls stay declarative and timeline ticks are fully data-driven.
- Fixed bar-slice end-exclusivity regression by passing rebased measure ticks/connections/tick specs through converter to the visualizer.
- Added explicit no-note guard in conversion to raise a clear `ValueError` before plotting.
- Deduplicate connection detection for split segments so long held notes interrupted by shared-pitch overlaps don't emit duplicate connections.
- Connection lines now start from the final split segment of a held note, preventing lines from originating at the first segment's start.
- Connection detection now tolerates small floating-point timing differences when deduplicating split segments.
- When multiple notes start together, only one connection is drawn into the next note start to avoid duplicate lines from simultaneous sources.
- Added `ConnectionConfig` for visual tweaks (alpha fade, linewidth, optional max-gap) and a legend hint for connections.
- Added coverage for connection alpha fading behavior.
- Exposed connection styling controls via CLI flags (`--connection-*`) and library params (max-gap, alpha, fade, linewidth).
- Added CLI and converter regression tests to ensure connection styling flags propagate end-to-end.
- Added optional connection curvature (`--connection-curve-height-factor`) with tests and README docs.

## [0.5.0] - 2025-12-29

### Added

- Default overlap splitting for stacked same-pitch notes so only the truly simultaneous segments use thicker bars.
- CLI flag `--no-overlap-splitting` (and library argument `split_overlaps`) to opt into legacy whole-note stacking; default remains splitting so only truly overlapping segments are thickened.
- Support for staccato articulations by shortening durations (default 40%) with configurable `--staccato-factor` (clamped 0.1–0.9).
- Timeline unit selection for the x-axis (`--timeline-unit {beat,bar,measure}`) to show bar numbers (default) or beats.
- Timeline slicing by bars/measures or beats via `--slice-range start-end` (unit from `--timeline-unit {bar,measure,beat}`) to render focused sections of a score.
  - Slices are 1-indexed and end-exclusive for both bars and beats. (i.e. `1-3` would generate two "units")

### Changed

- Timeline labels are now 1-indexed instead of 0-indexed

## [0.4.0] - 2025-12-29

### Added

- Auto-detect likely ensembles (orchestra/bigband/etc) and prints suggestions when no ensemble specified
- Visualization can display MusicXML rehearsal marks as labeled timeline guides (omit with `--no-rehearsal-marks`)
- CLI flag `--version` to print the tool version (short `-v` remains verbose)
- CLI flag `--no-rehearsal-marks` to suppress rehearsal mark rendering
- CLI flag `--no-legend` to disable legend rendering
- CLI flag `--no-title` to omit the plot title
- CLI flag `--no-output` to exercise the full pipeline without writing a PNG (useful for smoke tests)
- CLI flag `--skip-ensemble-detection` to suppress ensemble auto-detection (e.g., in CI)
- CLI flag `--print-ensemble-confidences` to emit raw ensemble confidences for all candidates on one line (debug/pipelines)
- CLI flag `--time-stretch` to scale timeline width for wider/denser plots
- CLI flag `--fig-width` to set explicit figure width in inches
- CLI flag `--dpi` to control output DPI (default 150, clamped 50-600)

### Changed

- Refactored conversion code into focused modules (`models`, `extract`, `visualize`, `converter` orchestration) for maintainability
- Removed terminal message regarding output when `--no-output` flag present
- Convert "magic numbers" to descriptive names in visualizer

### Fixed

- Aligned part offsets using a shared, canonical measure map to prevent percussion (e.g., timpani) from drifting late when bar durations are missing or inflated; added `test-orchestra-2.mxl` fixture and regression test to lock timing

## [0.3.0] - 2025-12-28

### Added

- Visualization now reflects musical intent more richly: bar opacity responds to dynamics markings/velocities, and bar thickness scales with simultaneous same-pitch stacking (ties already merged). Added regression tests for dynamics capture and pitch overlap tagging.

### Fixed

- Fixed tie handling bug where tied notes over barlines were incorrectly visualized as separate note attacks instead of continuous notes. Tied notes are now properly merged into single NoteEvent objects with combined durations.

### Changed

- Removed redundant Homepage field from pyproject.toml, keeping only Repository since they pointed to the same URL

## [0.2.3] - 2025-12-27

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

[0.6.1]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.6.1
[0.6.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.6.0
[0.5.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.5.0
[0.4.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.4.0
[0.3.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.3.0
[0.2.3]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.3
[0.2.2]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.2
[0.2.1]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.1
[0.2.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.2.0
[0.1.0]: https://github.com/rob-mosher/musicxml-to-png/releases/tag/v0.1.0
