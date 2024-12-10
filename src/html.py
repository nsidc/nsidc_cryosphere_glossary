"""Functions to create HTML glossary pages

Load entry YAML files
Create a list of terms
Create individual pages - has options to create full pages with refs etc as well as simple pages including just terms.

"""

from pathlib import Path

from src.glossary import Glossary

MKDIR = True

def make_letter_index(terms):
    """Generates an index of terms by first letter"""
    first_letters = set([term[0] for term in terms])
    index = {letter: [term for term in terms if term.startswith(letter)]
             for letter in letter_index}
    return index


def build_html(glossary_path, verbose=False):
    """Builds html pages for glossary"""

    if verbose: print(f"Loading glossary from {glossary_path}")
    glossary = Glossary.from_yaml(glossary_path)

    # Collect or sort terms
#    filepath = {term: make_entry_path(term, glossary_path=Path("html",term[0]), filetype="markdown") for term in terms}
    
    # Make index pages for each letter of alphabet
    # Consists or sorted list of terms with links to markdown page
    
    # Generate _quarto.yml
    
    if verbose: print(f"Generating entry markdown files")
    # Add links to terms
    # Put in directories organized by first letter to allow auto content creation
    # 
    glossary.to_markdown(mkdir=MKDIR)


if __name__ == "__main__":
    verbose = True
    build_html("glossary", verbose=verbose)
