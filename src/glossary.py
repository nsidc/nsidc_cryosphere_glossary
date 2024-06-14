"""Definitions for Glossary and Entry classes"""
from typing import List, Dict, Union

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

