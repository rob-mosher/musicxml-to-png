"""Command-line interface for MusicXML to PNG converter."""

import argparse
import sys
from pathlib import Path

from musicxml_to_png.converter import convert_musicxml_to_png


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert MusicXML files into clean, analyzable PNG visualizations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.xml
  %(prog)s input.xml -o output.png
  %(prog)s input.xml --title "My Composition"
  %(prog)s input.xml --no-grid
  %(prog)s input.xml --minimal
        """,
    )
    
    parser.add_argument(
        "input",
        type=str,
        help="Path to the input MusicXML file",
    )
    
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Path to the output PNG file (default: input filename with .png extension)",
    )
    
    parser.add_argument(
        "-t",
        "--title",
        type=str,
        default=None,
        help="Title for the visualization (default: input filename)",
    )
    
    parser.add_argument(
        "--no-grid",
        action="store_true",
        help="Disable grid lines in the visualization",
    )
    
    parser.add_argument(
        "--minimal",
        action="store_true",
        help="Remove all labels, legend, title, and borders for a clean visualization",
    )
    
    args = parser.parse_args()
    
    # Convert input path to Path object
    input_path = Path(args.input)
    
    # Validate input file exists
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    
    # Validate input file extension
    if input_path.suffix.lower() not in [".xml", ".musicxml", ".mxl"]:
        print(
            f"Warning: Input file doesn't have a standard MusicXML extension: {input_path.suffix}",
            file=sys.stderr,
        )
    
    # Convert output path if provided
    output_path = Path(args.output) if args.output else None
    
    try:
        # Perform conversion
        result_path = convert_musicxml_to_png(
            input_path=input_path,
            output_path=output_path,
            title=args.title if not args.minimal else None,
            show_grid=not args.no_grid,
            minimal=args.minimal,
        )
        print(f"Successfully created visualization: {result_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

