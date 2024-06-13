"""Input and output methods for glossary"""
from typing import List
from pathlib import Path

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
        
