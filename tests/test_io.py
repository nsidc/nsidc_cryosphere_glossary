"""Tests glossary io routines"""

from src.io import parse_entry_csv

line = '''ablation,"(1) combined processes (such as sublimation, fusion or melting, evaporation) which remove snow or ice from the surface of a glacier or from a snow-field; also used to express the quantity lost by these processes (2) reduction of the water equivalent of a snow cover by melting, evaporation, wind and avalanches."
'''
expected_entry_csv = {
    "term": "ablation",
    "definition": {
        1: "Combined processes (such as sublimation, fusion or melting, evaporation) which remove snow or ice from the surface of a glacier or from a snow-field; also used to express the quantity lost by these processes.",
        2: "Reduction of the water equivalent of a snow cover by melting, evaporation, wind and avalanches."
        }
    }


def test_parse_entry_csv():
    result = parse_entry_csv(line)
    assert result == expected_entry_csv


#def test_load_csv():
#    
