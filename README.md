# Cryosphere Glossary

This repo contains data and tools for managing the NSIDC Cryosphere Glossary

The glossary data file is in the `data` directory.  The original
glossary download from Drupal is `nsidc_cryosphere_glossary.20240601.csv`.  This is
retained as a marker.

The new glossary is a JSON file.  This glossary file has the following
structure.

`term` - the term for the glossary entry
`definition` - the definition this may be a single entry or multiple
entries.  Multiple entries are treated as a sequence/list.
`citation` - A citation for the term.

I could also have short and long/technical definitions.

I need a way to cross reference these.

**Update example**

Example

```
term: ablation
  definition:
    1: |
      All processes that reduce the mass of a glacier.  The main
      processes are melting and calving but processes also include
      sublimation, loss of windblown snow and avalanching.
    2: |
      The mass loss by melting, calving, sublimation, wind, and
      avalanching.
  citation:
    - cogley_et_al_2011
```

## Workflow
`from src.glossary import Glossary`

```
# Load glossary
glossary = Glossary().from_json("/data/nsidc_cryosphere_glossary.json")

# Find a term
glossary.find("ablation")

# Print an entry
glossary.print_term("ablation")
```

**Need tools to update definitions, add sources and references...**

TODO:
- Add github gui update workflow to README
- Move API workflow to separate pages
- create github actions to:
  + render pages
  + generate csv file
- Create simple html pages for display
  + generate _quarto.yml
  + write <term>.md to alphabetized directory structure 

- Add CLI for searching for a term
- Add CLI for updating a term - needs to add and commit to git, and push
  + update definition
  + add definition
  + add source
  + update source
  + add references
  + update references
  + find linked terms
  + output to markdown
  + output to quarto markdown
  + output to latex
- Add CLI to generate updated csv for ingest to Drupal - only needs to be changed terms

