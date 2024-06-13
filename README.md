# Cryosphere Glossary

This repo contains data and tools for managing the NSIDC Cryosphere Glossary

The glossary data file is in the `data` directory.  The original
glossary download from Drupal is `glossary-export.csv`.  This is
retained as a marker.

The new glossary is a YAML file.  This glossary file has the following
structure.

`term` - the term for the glossary entry
`definition` - the definition this may be a single entry or multiple
entries.  Multiple entries are treated as a sequence/list.
`citation` - A citation for the term.

I could also have short and long/technical definitions.

I need a way to cross reference these.

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

