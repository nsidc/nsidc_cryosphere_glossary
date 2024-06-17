"""Definitions for Glossary and Entry classes"""
from typing import List, Dict, Union
from pathlib import Path
import json


class Entry():
    """Class for glossary entry"""
    
    def __init__(self, term: str,
                 definition: Union[List[str], Dict, str],
                 source: Union[List[str], Dict, str]=None,
                 reference: Union[List[str], Dict, str]=None):
        """Initialize entry"""
        self.term = term
        self.definition = _add_attrs(definition, "definition")
        self.source = _add_attrs(source, "source")
        self.reference = _add_attrs(reference, "reference")

    def __repr__(self):
        return (f"<Entry: term={self.term} "
                f"definition={self.definition} "
                f"source={self.source} "
                f"reference={self.reference}")

    def __str__(self):
        s = f"term: {self.term}\n"
        s += (f"  definition:\n" +
              "\n".join([f"    ({k}): {v}" for k, v in self.definition.items()])) + "\n"
        s += f"  source:\n"
        if self.source is not None:
            s += "\n".join([f"    ({k}): {v}" for k, v in self.source.items()]) + "\n"
        s += f"  reference:\n"
        if self.reference is not None:
            s += "\n".join([f"    ({k}): {v}" for k, v in self.reference.items()]) + "\n"
        return s

    def to_json(self):
        pass

    def add_entry(self):
        pass

    def add_definition(self, definition):
        """Adds a definition to an entry"""
        pass

    def add_source(self, source):
        """Add a source to an entry"""
        pass

    def add_reference(self, reference):
        """Add a reference to an entry"""
        pass

    def to_dict(self):
        """Writes entry as dict"""
        return {
            "term": self.term,
            "definition": self.definition,
            "source": self.source,
            "reference": self.reference,
            }


def _add_attrs(attrs, name):
    if isinstance(attrs, list):
        return {k: v for k, v in enumerate(attrs, 1)}
    elif isinstance(attrs, dict):
        return attrs
    elif isinstance(attrs, str):
        return {1: attrs}
    elif attrs is None:
        return None
    else:
        raise TypeError(f"Expected list or dict for {name} not {type(attrs)}")


class Glossary():
    """Class for handling glossary"""

    def __init__(self, name=""):
        self.name = name
        self.n = 0
        self.entries = {}

    def find(self, term):
        try:
            entry = self.entries[term]
        except:
            print(f"{term} not found in {self.name}")
            return None
        return entry

    def add_entry(self, entry: Entry):
        """Adds an entry to the Glossary"""
        if entry.term in self.entries.keys():
            raise KeyError(f"{entry.term} already exists!\n{self.glossary[entry.term]}")
        # start glossary dict
        self.entries[entry.term] = entry
        self.n += 1

    def terms(self):
        """Lists all terms"""
        return list(self.entries.keys())

    def print_term(self, term):
        """Prints a glossary term"""
        print(self.find(term))

    def to_dict(self):
        """Creates a dictionary from a glossary.

        This is mostly used so that the glossary can be dumped to json
        """
        return {
            "name": self.name,
            "n": self.n,
            "entries": [entry.to_dict() for entry in self.entries.values()]
            }

    def to_json(self, filepath: Union[Path, str], indent=4, clobber=False):
        """Dumps glossary to json format file

        Arguments
        ---------
        filepath : path to write glossary
        indent : indent to make json pretty
        clobber : overwrite file if it exists, otherwise raise FileExists exception

        Returns
        -------
        None
        """
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), fp, indent=indent)


def _create_glossary(glossary_list):
    """Returns a dict of entries"""
    glossary = {}
    for entry in glossary_list:
        glossary[entry.term] = entry
    return glossary
