"""Input and output methods for glossary"""
from typing import List
from pathlib import Path
import re


def parse_entry_csv(entry):
    term, definition = entry.strip().split(",", maxsplit=1)
    ddef = parse_definition(definition)
    return {"term": term, "definition": ddef}


def parse_definition(s: str) -> dict:
    """Parses a definition and returns a dictionary containing one or more definitions

    TODO: Make sentence case
    """
    p = re.compile(r"\s?\(\d+\)\s?")
    s = s.strip('"')
    return {k: v for k, v in enumerate([a.strip() for a in p.split(s) if (a != '') and (a != ' ')], 1)}


def load_glossary_csv(filepath: Path, header=0, skiprows=0) -> List:
    """Loads a csv file containing a glossary and returns a list of
    glossary items"""
    entries = []
    with open(filepath) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if i <= skiprows:
            continue
        if i == (header + skiprows):
            columns = line.split(",")
        else:
            entries.append(parse_entry_csv(line))

    return entries
