"""Definitions for Glossary and Entry classes"""
from typing import List, Dict, Union
from pathlib import Path
import json
import yaml
import re

# move to config
GLOSSARY_PATH = Path("glossary")
HTML_PATH = Path("html")

class Entry():
    """Class for glossary entry

    An entry must have a term and at least one definition.

    The source is a label in a bibtex file for the source
    of a definitions.

    A reference is an additional citation.

    A synonym is an alternative term.  This may be a term in the glossary.

    see_also entries are expected to be related terms in the glossary.

    Methods
    -------
    from_yaml : loads entry from yaml
                Entry.from_yaml(filepath)
    """
    
    def __init__(self, term: str,
                 definition: Union[List[str], Dict, str],
                 source: Union[List[str], Dict, str]=None,
                 reference: Union[List[str], Dict, str]=None,
                 synonym: Union[List[str]]=[],
                 see_also: Union[List[str]]=[]):
        """Initialize entry"""
        self.term = term.lower()
        self.definition = _add_attrs(definition, "definition")
        self.source = _add_attrs(source, "source")
        self.reference = _add_attrs(reference, "reference")
        self.synonym = synonym
        self.see_also = see_also

    def __repr__(self):
        return (f"<Entry: term={self.term} "
                f"definition={self.definition} "
                f"synonym={self.synonym} "
                f"see_also={self.see_also} "
                f"source={self.source} "
                f"reference={self.reference}")

    def __str__(self):
        s = f"term: {self.term}\n"
        s += (f"  definition:\n" +
              "\n".join([f"    ({k}): {v}" for k, v in self.definition.items()])) + "\n"
        s += f"  synonym:\n"
        if self.synonym != []:
            s += "    " + ",".join([synonym for synonym in self.synonym])
        s += f"  also see:\n"
        if self.see_also != []:
              s += "    " + ",".join([see_also for see_also in self.see_also])
        s += f"  source:\n"
        if self.source is not None:
            s += "\n".join([f"    ({k}): {v}" for k, v in self.source.items()]) + "\n"
        s += f"  reference:\n"
        if self.reference is not None:
            s += "\n".join([f"    ({k}): {v}" for k, v in self.reference.items()]) + "\n"
        return s

    def add_definition(self, definition):
        """Adds a definition to an existing entry"""
        pass

    def add_source(self, source):
        """Add a source to an existing entry"""
        pass

    def add_reference(self, reference):
        """Add a reference to an existing entry"""
        pass

    def to_dict(self):
        """Writes entry as dict

        TODO: Check if this works with updated attributes
        """
        return self.__dict__

    def to_yaml(self, filepath: Union[str, Path], debug: bool=False):
        """Write entry to yaml file

        filepath : path to write entry.
        debug : creates a yaml file and writes to stdout
        """
        if debug:
            print(filepath)
            print(yaml.safe_dump(self.to_dict(), sort_keys=False))
        else:
            with open(filepath, "wt", encoding="utf-8") as f:
                yaml.safe_dump(self.to_dict(), f, sort_keys=False)

    def to_markdown(self, html_path='.', style="simple"):
        """Generates quarto style markdown for entry"""
        s = ""
        s += f"## {self.term.capitalize()}\n"
        if len(self.definition) > 1:
            s += "\n".join([f"{i}. {v}" for i, v in enumerate(self.definition.values(),1)])
        else:
            s += self.definition[1]
        if self.synonym:
            s += f"Synonyms: {", ".join(self.synonym)}\n"
        if self.see_also:
            s += f"See also: {", ".join(self.see_also)}\n"
        return s

    @classmethod
    def from_yaml(cls, filepath: Union[Path, str]):
        """Loads a glossary entry from a yaml"""
        with open(filepath, "r") as f:
            fields = yaml.safe_load(f)
        return cls(**fields)


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


def illegal_entry_path(entry_path: Path) -> bool:
    """Checks that entry path only contains lower-case letters
    and underscores.

    Returns
    -------
    False if path name excluding parents and extension contains
    characters other than a-z and _
    """
    return not re.match(r'^\w+$', entry_path.stem)


def make_entry_path(term: str,
                    glossary_path: Path=GLOSSARY_PATH,
                    filetype: str="yaml") -> Path:
    """Generates a filepath for a glossary entry

    term : glossary term
    filetype : type of file to create so that correct extension added
    
    returns : returns a Path object
    """
    extensions = {
        "yaml": "yml",
        "csv": "csv",
        "markdown": "md",
        }
    suffix = extensions.get(filetype)
    if not suffix:
        raise KeyError("Unknown filetype")
    entry_path = glossary_path / f"{re.sub(r'[\(\)\']','',re.sub('[ -/]','_',term.lower()))}.{suffix}"
    if illegal_entry_path(entry_path):
        raise ValueError(f"{entry_path.stem} contains illegal character, expected only a-z and _")
    return entry_path

    
class Glossary():
    """Class for handling glossary

    Attributes
    ----------
    name : the name of the glossary
    n : (int) the number of entries in the glossary
    entries : A dictionary of Entry objects with terms as keys
    """

    def __init__(self, name="", n=0, entries={}):
        self.name = name
        self.entries = entries  #self.add_entry(Entry(**entry)) for entry in entries]
        self.n = n

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
            "entries": [entry.to_dict() for term, entry in sorted(self.entries.items())]
            }

    def to_json(self, filepath: Union[Path, str],
                indent=4,
                clobber=False):
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
            json.dump(self.to_dict(), f, indent=indent)

    def print_glossary(self, sort_terms=True):
        print(f"name: {self.name}")
        print(f"n: {self.n}")
        if sort_terms:
            for term, entry in sorted(self.entries.items()):
                print(entry)
        else:
            for entry in self.entries.values():
                print(entry)

    def to_yaml(self, glossary_path: Union[Path,str]=GLOSSARY_PATH,
                clobber: bool=False,
                update: bool=False,
                debug: bool=False,):
        """Dumps glossary as a collection of yaml files

        glossary_path : directory path for yaml files.  Default
                        is GLOSSARY_PATH.
        clobber : overwrite whole glossary in GLOSSARY_PATH
        update : only overwrite entries that have changed
        """
        for term, entry in self.entries.items():
            filepath = make_entry_path(term, glossary_path=glossary_path / term[0],
                                       filetype="yaml")
            if (clobber == False) & filepath.exists():
                warning.warn(f"{filepath} already exists, skipping")
                continue
            if update == True:
                # Is there a way to trigger git?
                raise NotImplemented
            if not filepath.parent.exists():
                filepath.parent.mkdir(parents=True, exist_ok=True)
            entry.to_yaml(filepath, debug=debug)

    def to_markdown(self, path: Union[Path, str]=HTML_PATH, mkdir: bool=False,
                    clobber=False):
        """Generates markdown files for entries

        Arguments
        ---------
        path : path for markdown documents.  Default is html
        mkdir : if True create path if it does not exist
        clobber : if True overwrite markdown file, otherwise only update if yaml updated

        TODO: Only create if older than yaml
        """
        for term, entry in self.entries.items():
            markdown = entry.to_markdown()
            # Add way to index terms
            filepath = make_entry_path(term, glossary_path=path / term[0], filetype="markdown")

            if (not filepath.parent.exists()) & mkdir:
                filepath.parent.mkdir(parents=True, exist_ok=True)
            elif not filepath.parent.exists():
                print(f"{filepath.parent} does not exist, set mkdir=True to create it")
                return

            with open(filepath, "wt") as f:
                f.write(markdown)


    @classmethod
    def from_json(cls, filepath: Union[Path, str]):
        """Loads a glossary from a JSON file"""
        with open(filepath, "r") as f:
            obj = json.load(f)
        name = obj["name"]
        n = obj["n"]
        entries = {entry["term"]: Entry(**entry) for entry in obj["entries"]}
        return cls(name, n, entries)


    @classmethod
    def from_yaml(cls, path: Union[Path, str], name: str="unnamed glossary"):
        """Loads a glossary from YAMLs in path"""
        path = Path(path)
        entries = {}
        n = 0
        for entry_yaml in path.glob("*/*.yml"):
            entry = Entry.from_yaml(entry_yaml)
            entries[entry.term] = entry
            n += 1
        return cls(name, n, entries)
