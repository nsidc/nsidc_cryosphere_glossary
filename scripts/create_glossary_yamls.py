"""Generates YAML files for terms in glossary input csv file.  YAML files
are written by default to the glossary directory"""

from pathlib import Path

from src.io import load_glossary_csv

GLOSSARY_CSV = "data/test_glossary.csv"

DEBUG = False

def create_glossary_yamls():

    glossary = load_glossary_csv(GLOSSARY_CSV)
    glossary.to_yaml(clobber=True, debug=DEBUG)


if __name__ == "__main__":
    create_glossary_yamls()
