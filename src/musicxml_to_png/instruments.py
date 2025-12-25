"""Instrument family classification and color mapping."""

from typing import Optional

# Instrument families
FAMILY_STRINGS = "strings"
FAMILY_WINDS = "winds"
FAMILY_BRASS = "brass"
FAMILY_PERCUSSION = "percussion"
FAMILY_UNKNOWN = "unknown"

# Color palette for each instrument family
COLORS = {
    FAMILY_STRINGS: "#2E7D32",  # Green
    FAMILY_WINDS: "#1976D2",    # Blue
    FAMILY_BRASS: "#F57C00",    # Orange
    FAMILY_PERCUSSION: "#C2185B",  # Pink/Magenta
    FAMILY_UNKNOWN: "#757575",  # Gray
}

# MIDI program numbers mapped to instrument families
# General MIDI Standard Program Numbers
MIDI_PROGRAM_FAMILIES = {
    # Piano (1-8) - treat as strings-like
    1: FAMILY_STRINGS,  # Acoustic Grand Piano
    2: FAMILY_STRINGS,  # Bright Acoustic Piano
    3: FAMILY_STRINGS,  # Electric Grand Piano
    4: FAMILY_STRINGS,  # Honky-tonk Piano
    5: FAMILY_STRINGS,  # Electric Piano 1
    6: FAMILY_STRINGS,  # Electric Piano 2
    7: FAMILY_STRINGS,  # Harpsichord
    8: FAMILY_STRINGS,  # Clavi
    
    # Chromatic Percussion (9-16)
    9: FAMILY_PERCUSSION,   # Celesta
    10: FAMILY_PERCUSSION,  # Glockenspiel
    11: FAMILY_PERCUSSION,  # Music Box
    12: FAMILY_PERCUSSION,  # Vibraphone
    13: FAMILY_PERCUSSION,  # Marimba
    14: FAMILY_PERCUSSION,  # Xylophone
    15: FAMILY_PERCUSSION,  # Tubular Bells
    16: FAMILY_PERCUSSION,  # Dulcimer
    
    # Organ (17-24) - treat as winds-like
    17: FAMILY_WINDS,  # Drawbar Organ
    18: FAMILY_WINDS,  # Percussive Organ
    19: FAMILY_WINDS,  # Rock Organ
    20: FAMILY_WINDS,  # Church Organ
    21: FAMILY_WINDS,  # Reed Organ
    22: FAMILY_WINDS,  # Accordion
    23: FAMILY_WINDS,  # Harmonica
    24: FAMILY_WINDS,  # Tango Accordion
    
    # Guitar (25-32) - strings
    25: FAMILY_STRINGS,  # Acoustic Guitar (nylon)
    26: FAMILY_STRINGS,  # Acoustic Guitar (steel)
    27: FAMILY_STRINGS,  # Electric Guitar (jazz)
    28: FAMILY_STRINGS,  # Electric Guitar (clean)
    29: FAMILY_STRINGS,  # Electric Guitar (muted)
    30: FAMILY_STRINGS,  # Overdriven Guitar
    31: FAMILY_STRINGS,  # Distortion Guitar
    32: FAMILY_STRINGS,  # Guitar harmonics
    
    # Bass (33-40) - strings
    33: FAMILY_STRINGS,  # Acoustic Bass
    34: FAMILY_STRINGS,  # Electric Bass (finger)
    35: FAMILY_STRINGS,  # Electric Bass (pick)
    36: FAMILY_STRINGS,  # Fretless Bass
    37: FAMILY_STRINGS,  # Slap Bass 1
    38: FAMILY_STRINGS,  # Slap Bass 2
    39: FAMILY_STRINGS,  # Synth Bass 1
    40: FAMILY_STRINGS,  # Synth Bass 2
    
    # Strings (41-48)
    41: FAMILY_STRINGS,  # Violin
    42: FAMILY_STRINGS,  # Viola
    43: FAMILY_STRINGS,  # Cello
    44: FAMILY_STRINGS,  # Contrabass
    45: FAMILY_STRINGS,  # Tremolo Strings
    46: FAMILY_STRINGS,  # Pizzicato Strings
    47: FAMILY_STRINGS,  # Orchestral Harp
    48: FAMILY_STRINGS,  # Timpani
    
    # Ensemble (49-56) - mostly strings
    49: FAMILY_STRINGS,  # String Ensemble 1
    50: FAMILY_STRINGS,  # String Ensemble 2
    51: FAMILY_STRINGS,  # SynthStrings 1
    52: FAMILY_STRINGS,  # SynthStrings 2
    53: FAMILY_WINDS,    # Choir Aahs
    54: FAMILY_WINDS,    # Voice Oohs
    55: FAMILY_WINDS,    # Synth Voice
    56: FAMILY_BRASS,    # Orchestra Hit
    
    # Brass (57-64)
    57: FAMILY_BRASS,  # Trumpet
    58: FAMILY_BRASS,  # Trombone
    59: FAMILY_BRASS,  # Tuba
    60: FAMILY_BRASS,  # Muted Trumpet
    61: FAMILY_BRASS,  # French Horn
    62: FAMILY_BRASS,  # Brass Section
    63: FAMILY_BRASS,  # SynthBrass 1
    64: FAMILY_BRASS,  # SynthBrass 2
    
    # Reed (65-72) - winds
    65: FAMILY_WINDS,  # Soprano Sax
    66: FAMILY_WINDS,  # Alto Sax
    67: FAMILY_WINDS,  # Tenor Sax
    68: FAMILY_WINDS,  # Baritone Sax
    69: FAMILY_WINDS,  # Oboe
    70: FAMILY_WINDS,  # English Horn
    71: FAMILY_WINDS,  # Bassoon
    72: FAMILY_WINDS,  # Clarinet
    
    # Pipe (73-80) - winds
    73: FAMILY_WINDS,  # Piccolo
    74: FAMILY_WINDS,  # Flute
    75: FAMILY_WINDS,  # Recorder
    76: FAMILY_WINDS,  # Pan Flute
    77: FAMILY_WINDS,  # Blown Bottle
    78: FAMILY_WINDS,  # Shakuhachi
    79: FAMILY_WINDS,  # Whistle
    80: FAMILY_WINDS,  # Ocarina
    
    # Synth Lead (81-88) - treat as winds
    81: FAMILY_WINDS,  # Lead 1 (square)
    82: FAMILY_WINDS,  # Lead 2 (sawtooth)
    83: FAMILY_WINDS,  # Lead 3 (calliope)
    84: FAMILY_WINDS,  # Lead 4 (chiff)
    85: FAMILY_WINDS,  # Lead 5 (charang)
    86: FAMILY_WINDS,  # Lead 6 (voice)
    87: FAMILY_WINDS,  # Lead 7 (fifths)
    88: FAMILY_WINDS,  # Lead 8 (bass + lead)
    
    # Synth Pad (89-96) - treat as strings
    89: FAMILY_STRINGS,  # Pad 1 (new age)
    90: FAMILY_STRINGS,  # Pad 2 (warm)
    91: FAMILY_STRINGS,  # Pad 3 (polysynth)
    92: FAMILY_STRINGS,  # Pad 4 (choir)
    93: FAMILY_STRINGS,  # Pad 5 (bowed)
    94: FAMILY_STRINGS,  # Pad 6 (metallic)
    95: FAMILY_STRINGS,  # Pad 7 (halo)
    96: FAMILY_STRINGS,  # Pad 8 (sweep)
    
    # Synth Effects (97-104) - treat as unknown
    97: FAMILY_UNKNOWN,  # FX 1 (rain)
    98: FAMILY_UNKNOWN,  # FX 2 (soundtrack)
    99: FAMILY_UNKNOWN,  # FX 3 (crystal)
    100: FAMILY_UNKNOWN,  # FX 4 (atmosphere)
    101: FAMILY_UNKNOWN,  # FX 5 (brightness)
    102: FAMILY_UNKNOWN,  # FX 6 (goblins)
    103: FAMILY_UNKNOWN,  # FX 7 (echoes)
    104: FAMILY_UNKNOWN,  # FX 8 (sci-fi)
    
    # Ethnic (105-112) - mixed
    105: FAMILY_WINDS,  # Sitar
    106: FAMILY_STRINGS,  # Banjo
    107: FAMILY_STRINGS,  # Shamisen
    108: FAMILY_STRINGS,  # Koto
    109: FAMILY_STRINGS,  # Kalimba
    110: FAMILY_STRINGS,  # Bag pipe
    111: FAMILY_WINDS,  # Fiddle
    112: FAMILY_STRINGS,  # Shanai
    
    # Percussive (113-120) - percussion
    113: FAMILY_PERCUSSION,  # Tinkle Bell
    114: FAMILY_PERCUSSION,  # Agogo
    115: FAMILY_PERCUSSION,  # Steel Drums
    116: FAMILY_PERCUSSION,  # Woodblock
    117: FAMILY_PERCUSSION,  # Taiko Drum
    118: FAMILY_PERCUSSION,  # Melodic Tom
    119: FAMILY_PERCUSSION,  # Synth Drum
    120: FAMILY_PERCUSSION,  # Reverse Cymbal
    
    # Sound Effects (121-128) - percussion/unknown
    121: FAMILY_PERCUSSION,  # Guitar Fret Noise
    122: FAMILY_PERCUSSION,  # Breath Noise
    123: FAMILY_PERCUSSION,  # Seashore
    124: FAMILY_PERCUSSION,  # Bird Tweet
    125: FAMILY_PERCUSSION,  # Telephone Ring
    126: FAMILY_PERCUSSION,  # Helicopter
    127: FAMILY_PERCUSSION,  # Applause
    128: FAMILY_PERCUSSION,  # Gunshot
}

# Instrument name keywords for classification
INSTRUMENT_NAME_KEYWORDS = {
    FAMILY_STRINGS: [
        "violin", "viola", "cello", "contrabass", "double bass", "bass",
        "guitar", "harp", "piano", "pianoforte", "harpsichord", "clavichord",
        "banjo", "mandolin", "ukulele", "lute", "sitar", "shamisen", "koto",
        "strings", "string", "pizzicato", "tremolo",
    ],
    FAMILY_WINDS: [
        "flute", "piccolo", "recorder", "oboe", "english horn", "cor anglais",
        "clarinet", "bassoon", "contrabassoon", "saxophone", "sax", "soprano",
        "alto", "tenor", "baritone", "bass clarinet", "bassoon", "fagotto",
        "organ", "accordion", "harmonica", "pan flute", "whistle", "ocarina",
        "shakuhachi", "bagpipe", "fiddle",
    ],
    FAMILY_BRASS: [
        "trumpet", "cornet", "trombone", "tuba", "french horn", "horn",
        "euphonium", "baritone", "flugelhorn", "bugle", "brass", "muted",
    ],
    FAMILY_PERCUSSION: [
        "drum", "timpani", "snare", "bass drum", "cymbal", "triangle",
        "tambourine", "marimba", "xylophone", "vibraphone", "glockenspiel",
        "celesta", "gong", "bell", "chime", "woodblock", "clap", "percussion",
        "tom", "hi-hat", "crash", "ride",
    ],
}


def get_instrument_family(
    midi_program: Optional[int] = None,
    instrument_name: Optional[str] = None,
) -> str:
    """
    Determine instrument family from MIDI program number and/or instrument name.
    
    Args:
        midi_program: MIDI program number (1-128)
        instrument_name: Name of the instrument (case-insensitive)
    
    Returns:
        Instrument family string (strings, winds, brass, percussion, or unknown)
    """
    # First, try MIDI program number
    if midi_program is not None and 1 <= midi_program <= 128:
        return MIDI_PROGRAM_FAMILIES.get(midi_program, FAMILY_UNKNOWN)
    
    # Fall back to instrument name matching
    if instrument_name:
        name_lower = instrument_name.lower()
        for family, keywords in INSTRUMENT_NAME_KEYWORDS.items():
            for keyword in keywords:
                if keyword in name_lower:
                    return family
    
    return FAMILY_UNKNOWN


def get_family_color(family: str) -> str:
    """
    Get the color for an instrument family.
    
    Args:
        family: Instrument family string
    
    Returns:
        Hex color code string
    """
    return COLORS.get(family, COLORS[FAMILY_UNKNOWN])

