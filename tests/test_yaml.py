"""Test yaml dump and load functionality"""

from src.glossary import Glossary, Entry

entry = Entry(
    term="freeboard",
    definition="The thickness of sea ice protruding above the water level. freeboard and draft comprise total sea ice thickness.",
    source=None,
    reference=None,
    synonym=[],
    see_also=["draft"],
    )

expected = """glossary/freeboard.yml
term: freeboard
definition:
  1: The thickness of sea ice protruding above the water level. freeboard and draft
    comprise total sea ice thickness.
source: null
reference: null
synonym: []
see_also:
- draft"""

def test_to_yaml():
    """Should to_yaml" return a string?"""
    result = entry.to_yaml(filepath="glossary/freeboard.yml", debug=True)
    print(result)
    print(expected)
    assert result == expected
    
