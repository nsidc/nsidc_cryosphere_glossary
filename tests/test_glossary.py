"""Test routines for glossary classes"""

import pytest

from pathlib import Path
from src.glossary import Entry, make_entry_path

@pytest.mark.parametrize(
    "test_input,expected",
    [
         (
             ("fish", "gilled animal", "god"),
             ("fish", {1: "gilled animal"}, {1: "god"})
             ),
         (
             ("fish", ["gilled animal"], None),
             ("fish", {1: "gilled animal"}, None)
             ),
         (
             ("fish", ["gilled animal","aquatic vertibrate"], ["God", "Linneas"]),
             ("fish", {1: "gilled animal", 2: "aquatic vertibrate"}, {1: "God", 2: "Linneas"})
             ),
        ]
    )
def test_entry(test_input, expected):
    result = Entry(*test_input)
    print(result)


def test_make_entry_path():
    result = make_entry_path("ablation")
    expected = Path("glossary/ablation.yml")
    assert result == expected
