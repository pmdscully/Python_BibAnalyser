# Python_BibAnalyser
Discover which Journals you mostly read and therefore should be aiming to publish in. Uses Bibtexparser library to analyse your bibtex database file(s).

## Set-up:

1. Requirements:
  - Python 2.7 (should work on 3.x)
  - bibtexparser (pip install bibtexparser) 

2. Set-up the bibtex database file path in the config.py: 

```class App:
    __conf = {
        "bibtex_filepath":             "bibtexdb.bib"
    }
```    
## How to Run:

To print list of journal titles by frequency:

```
  python journal_mode_bibtex.py
```
