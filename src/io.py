"""Input and output methods for glossary"""
from typing import List
from pathlib import Path
import re

from src.glossary import Glossary, Entry


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
    definitions = [as_sentence(a) for a in p.split(s) if (a != '') and (a != ' ')]
    return {k: v for k, v in enumerate(definitions, 1)}


def as_sentence(s):
    """Simple method to convert string to sentence case.

    Arguments
    ---------
    s : string to be converted

    Returns
    -------
    string passed to string method capitalize and period added, if necessary.
    """
    s = s.strip().capitalize()
    if not s.endswith("."):
        s += "."
    return s


def load_glossary_csv(filepath: Path,
                      header: int=0,
                      skiprows: int=0,
                      name: str="") -> List:
    """Loads a csv file containing a glossary and returns a list of
    glossary items"""
    glossary = Glossary()
    
    with open(filepath) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if i <= skiprows:
            continue
        if i == (header + skiprows):
            columns = line.split(",")
        else:
            glossary.add_entry(Entry(**parse_entry_csv(line)))

    return glossary
